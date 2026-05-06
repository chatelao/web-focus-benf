import os
import re
import ir
import asg
from type_inferrer import TypeInferrer
from type_mapper import map_wf_type_to_pg
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ir_utils import get_base_name, find_simple_for_loop, find_simple_while_loop

class PostgresEmitter:
    """
    Generates PostgreSQL code from IR using Jinja2 templates.
    """
    def __init__(self, template_dir=None, metadata_registry=None):
        if template_dir is None:
            # Default to src/templates relative to this file
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['sql']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        self.metadata_registry = metadata_registry
        self.virtual_fields = {} # filename -> {field_name: asg.Expression}
        self.active_joins = []

    def emit(self, cfg, procedure_name="webfocus_procedure"):
        """
        Performs full emission of a CFG to a PL/pgSQL function.
        """
        variables = self.get_variables_from_cfg(cfg)
        body = self.emit_cfg(cfg)
        return self.emit_procedure(procedure_name, body, variables)

    def render(self, template_name, **kwargs):
        """
        Renders a template with the given context.
        """
        template = self.env.get_template(template_name)
        return template.render(**kwargs)

    def emit_procedure(self, name, body, variables=None):
        """
        Helper to emit a full PL/pgSQL procedure.
        """
        return self.render('base.sql.j2', procedure_name=name, procedure_body=body, variables=variables)

    def get_variables_from_cfg(self, cfg):
        """
        Discovers all variables in the CFG and maps them to SQL-safe names and types.
        Returns a dictionary of {sql_name: postgres_type}.
        """
        variables = {}
        variables['v_next_block'] = 'TEXT'

        inferrer = TypeInferrer()
        # Pass 1: Repeat type inference until types stabilize or max iterations
        for _ in range(3):
            for block in cfg.blocks.values():
                for instr in block.instructions:
                    # Run type inference on instruction components if they contain ASG nodes
                    if hasattr(instr, 'source') and isinstance(instr.source, asg.ASGNode):
                        dtype = inferrer.visit(instr.source)
                        # Propagate inferred type to target symbol if it's an assignment
                        if isinstance(instr, ir.Assign) and dtype:
                            # instr.target might be a string (SSA name) or an ASG node
                            target_name = instr.target if isinstance(instr.target, str) else getattr(instr.target, 'name', None)
                            if target_name:
                                # We need a way to store this inferred type for future lookups of this variable
                                if not hasattr(inferrer, 'ssa_types'):
                                    inferrer.ssa_types = {}
                                inferrer.ssa_types[target_name] = dtype

                    elif isinstance(instr, ir.Assign) and hasattr(instr, 'data_type') and instr.data_type:
                        # Use explicitly set data_type on the instruction (e.g. from a test or earlier phase)
                        target_name = instr.target if isinstance(instr.target, str) else getattr(instr.target, 'name', None)
                        if target_name:
                            if not hasattr(inferrer, 'ssa_types'):
                                inferrer.ssa_types = {}
                            inferrer.ssa_types[target_name] = instr.data_type

                    if hasattr(instr, 'condition') and isinstance(instr.condition, asg.ASGNode):
                        inferrer.visit(instr.condition)

        # Pass 2: Discover variables and assign types
        for block in cfg.blocks.values():
            for instr in block.instructions:
                targets = []
                if hasattr(instr, 'target'):
                    targets.append(instr.target)
                if hasattr(instr, 'targets'):
                    targets.extend(instr.targets)

                for target in targets:
                    if not target: continue
                    sql_name = self._sanitize_name(target)

                    # Try to get data type from instruction, then from source expression
                    data_type = getattr(instr, 'data_type', None)
                    if not data_type and hasattr(instr, 'source'):
                        data_type = getattr(instr.source, 'data_type', None)

                    # If we have inferred types for SSA variables, use them
                    target_name = target if isinstance(target, str) else getattr(target, 'name', None)
                    if not data_type and hasattr(inferrer, 'ssa_types') and target_name in inferrer.ssa_types:
                        data_type = inferrer.ssa_types[target_name]

                    if sql_name not in variables:
                        if not data_type:
                            data_type = 'A' # Default to Alpha
                        variables[sql_name] = self._map_type(data_type)
                    elif variables[sql_name] in ('TEXT', 'CHAR') and data_type and data_type != 'A':
                        # Upgrade type if we found a more specific one
                        variables[sql_name] = self._map_type(data_type)

                # Also check expressions for variables that might not be assigned (though SSA should handle this)
                self._discover_vars_in_expr(instr, variables)
        return variables

    def _sanitize_name(self, name):
        """
        Converts WebFOCUS/SSA variable names to SQL-safe identifiers.
        Example: &X_1 -> v_X_1
        """
        if isinstance(name, str):
            if name.startswith('v_'):
                return name
            clean_name = name.lstrip('&')
            # Replace common invalid chars with underscore
            clean_name = clean_name.replace('-', '_').replace('.', '_')
            return f"v_{clean_name}"
        return name

    def _map_type(self, data_type):
        return map_wf_type_to_pg(data_type)

    def _discover_vars_in_expr(self, node, variables):
        """
        Recursively discovers variables in instructions and ASG nodes.
        """
        if node is None:
            return

        # If it's an instruction, check its fields
        if hasattr(node, 'source'):
            self._discover_vars_in_expr(node.source, variables)
        if hasattr(node, 'condition'):
            self._discover_vars_in_expr(node.condition, variables)
        if hasattr(node, 'messages'):
            for m in node.messages:
                self._discover_vars_in_expr(m, variables)
        if hasattr(node, 'arguments'):
            for a in node.arguments:
                self._discover_vars_in_expr(a, variables)
        if hasattr(node, 'components'):
            for c in node.components:
                self._discover_vars_in_expr(c, variables)
        if hasattr(node, 'assignments'):
            for a in node.assignments:
                self._discover_vars_in_expr(a, variables)
        if hasattr(node, 'statements'):
            for s in node.statements:
                self._discover_vars_in_expr(s, variables)
        if hasattr(node, 'properties'):
            for p in node.properties:
                self._discover_vars_in_expr(p, variables)
        if hasattr(node, 'value'):
            self._discover_vars_in_expr(node.value, variables)
        if hasattr(node, 'expression'):
            self._discover_vars_in_expr(node.expression, variables)
        if hasattr(node, 'pairs'):
            for val, res in node.pairs:
                self._discover_vars_in_expr(val, variables)
                self._discover_vars_in_expr(res, variables)
        if hasattr(node, 'default_value'):
            self._discover_vars_in_expr(node.default_value, variables)
        if hasattr(node, 'sources') and not isinstance(node, (asg.BinaryOperation, asg.UnaryOperation)):
            # Handle Phi sources or other lists of sources
            for s in node.sources:
                if isinstance(s, str):
                    sql_name = self._sanitize_name(s)
                    if sql_name not in variables:
                        variables[sql_name] = 'TEXT'
                else:
                    self._discover_vars_in_expr(s, variables)

        # If it's an ASG expression node
        class_name = node.__class__.__name__
        if class_name in ('AmperVar', 'Identifier'):
            sql_name = self._sanitize_name(node.name)
            if sql_name not in variables:
                # Default to TEXT if we don't know the type from an assignment
                # In a real compiler, we'd use the TypeInferrer results here.
                variables[sql_name] = getattr(node, 'data_type', 'TEXT')
                if variables[sql_name] not in ('INTEGER', 'NUMERIC', 'TEXT', 'BOOLEAN'):
                    variables[sql_name] = self._map_type(variables[sql_name])

        elif class_name == 'BinaryOperation':
            self._discover_vars_in_expr(node.left, variables)
            self._discover_vars_in_expr(node.right, variables)
        elif class_name == 'UnaryOperation':
            self._discover_vars_in_expr(node.operand, variables)
        elif class_name == 'FunctionCall':
            for arg in node.arguments:
                self._discover_vars_in_expr(arg, variables)
        elif class_name == 'IfExpression':
            self._discover_vars_in_expr(node.condition, variables)
            self._discover_vars_in_expr(node.then_expr, variables)
            self._discover_vars_in_expr(node.else_expr, variables)
        elif class_name == 'BetweenExpression':
            self._discover_vars_in_expr(node.expression, variables)
            self._discover_vars_in_expr(node.lower, variables)
            self._discover_vars_in_expr(node.upper, variables)
        elif class_name == 'InExpression':
            self._discover_vars_in_expr(node.expression, variables)
            for val in node.values:
                self._discover_vars_in_expr(val, variables)
        elif class_name == 'IsMissingExpression':
            self._discover_vars_in_expr(node.expression, variables)

    def emit_expression(self, expr, **kwargs):
        """
        Translates ASG expression nodes to PostgreSQL SQL strings.
        """
        if expr is None:
            return "NULL"

        in_query = kwargs.get('in_query', False)
        virtual_fields = kwargs.get('virtual_fields')
        qualifier = kwargs.get('qualifier')
        aggregate = kwargs.get('aggregate', False)
        group_by_fields = kwargs.get('group_by_fields', [])

        class_name = expr.__class__.__name__

        if class_name == 'Literal':
            if isinstance(expr.value, str):
                # Simple string quoting, might need more robust escaping
                return f"'{expr.value}'"
            return str(expr.value)

        elif class_name == 'AmperVar':
            return self._sanitize_name(expr.name)

        elif class_name == 'Identifier':
            # Fields in SQL are usually handled in the context of a query,
            # but for expressions in procedural logic they might be variables.
            if in_query:
                if virtual_fields and expr.name in virtual_fields:
                    # Recursively emit the virtual field expression.
                    # We expand it WITHOUT internal aggregation, then wrap the result if needed.
                    entry = virtual_fields[expr.name]
                    if isinstance(entry, tuple):
                        expr_val, fmt = entry
                    else:
                        expr_val, fmt = entry, None

                    new_kwargs = kwargs.copy()
                    new_kwargs['aggregate'] = False
                    expanded = self.emit_expression(expr_val, **new_kwargs)

                    if fmt and fmt.upper().startswith('A'):
                        pg_type = self._map_type(fmt)
                        if pg_type.startswith('CHAR'):
                            expanded = f"CAST({expanded} AS {pg_type})"

                    if aggregate:
                        return f"SUM({expanded})"
                    return expanded

                sql_f = qualifier(expr.name) if qualifier else expr.name
                if aggregate and group_by_fields is not None and sql_f not in group_by_fields:
                    return f"SUM({sql_f})"
                return sql_f
            return self._sanitize_name(expr.name)

        elif class_name == 'BinaryOperation':
            left = self.emit_expression(expr.left, **kwargs)
            right = self.emit_expression(expr.right, **kwargs)
            op = expr.operator.upper()

            # Map WebFOCUS operators to SQL
            op_mapping = {
                'EQ': '=',
                'NE': '<>',
                'GT': '>',
                'GE': '>=',
                'LT': '<',
                'LE': '<=',
                'AND': 'AND',
                'OR': 'OR',
                'CONCAT': '||',
                'EXCEEDS': '>',
                'IS LESS THAN': '<',
                'IS MORE THAN': '>',
                'IS GREATER THAN': '>',
                'ISLESSTHAN': '<',
                'ISMORETHAN': '>',
                'ISGREATERTHAN': '>',
                'ISNOT': '<>',
                'IS NOT': '<>'
            }

            if op == 'CONTAINS':
                return f"({left} LIKE '%' || {right} || '%')"
            if op == 'OMITS':
                return f"({left} NOT LIKE '%' || {right} || '%')"

            sql_op = op_mapping.get(op, op)
            return f"({left} {sql_op} {right})"

        elif class_name == 'UnaryOperation':
            operand = self.emit_expression(expr.operand, **kwargs)
            op = expr.operator.upper()
            op_mapping = {
                'NOT': 'NOT ',
            }
            sql_op = op_mapping.get(op, op)
            return f"{sql_op}({operand})"

        elif class_name == 'FunctionCall':
            args = [self.emit_expression(arg, **kwargs) for arg in expr.arguments]
            return f"{expr.function_name}({', '.join(args)})"

        elif class_name == 'IfExpression':
            cond = self.emit_expression(expr.condition, **kwargs)
            then_e = self.emit_expression(expr.then_expr, **kwargs)
            else_e = self.emit_expression(expr.else_expr, **kwargs)
            return f"(CASE WHEN {cond} THEN {then_e} ELSE {else_e} END)"

        elif class_name == 'BetweenExpression':
            expr_val = self.emit_expression(expr.expression, **kwargs)
            lower = self.emit_expression(expr.lower, **kwargs)
            upper = self.emit_expression(expr.upper, **kwargs)
            return f"({expr_val} BETWEEN {lower} AND {upper})"

        elif class_name == 'InExpression':
            expr_val = self.emit_expression(expr.expression, **kwargs)
            if hasattr(expr, 'filename') and expr.filename:
                table_name = self._resolve_table_name(expr.filename)
                return f"({expr_val} IN (SELECT * FROM {table_name}))"
            else:
                values = [self.emit_expression(val, **kwargs) for val in expr.values]
                return f"({expr_val} IN ({', '.join(values)}))"

        elif class_name == 'IsMissingExpression':
            expr_val = self.emit_expression(expr.expression, **kwargs)
            op = "IS NOT NULL" if expr.inverted else "IS NULL"
            return f"({expr_val} {op})"

        elif class_name == 'DecodeExpression':
            expr_val = self.emit_expression(expr.expression, **kwargs)
            when_clauses = []
            for val, res in expr.pairs:
                val_sql = self.emit_expression(val, **kwargs)
                res_sql = self.emit_expression(res, **kwargs)
                when_clauses.append(f"WHEN {val_sql} THEN {res_sql}")

            else_clause = ""
            if expr.default_value:
                default_sql = self.emit_expression(expr.default_value, **kwargs)
                else_clause = f" ELSE {default_sql}"

            return f"(CASE {expr_val} {' '.join(when_clauses)}{else_clause} END)"

        return f"/* Unknown expression: {class_name} */"

    def emit_instruction(self, instr, current_block=None, cfg=None):
        """
        Translates IR instructions to PL/pgSQL statements.
        """
        class_name = instr.__class__.__name__

        if class_name == 'Assign':
            target = self._sanitize_name(instr.target)
            source = self.emit_expression(instr.source)
            return f"{target} := {source};"

        elif class_name == 'Type':
            # -TYPE messages can be complex, for now handle literal components
            parts = []
            for part in instr.messages:
                parts.append(self.emit_expression(part))

            # Concatenate parts for RAISE NOTICE
            if not parts:
                return "RAISE NOTICE '';"

            # Using format string for RAISE NOTICE
            format_str = " || ".join(parts)
            return f"RAISE NOTICE '%', {format_str};"

        elif class_name == 'Jump':
            res = []
            if current_block and cfg:
                target_block = cfg.blocks.get(instr.target)
                if target_block:
                    phi_res = self._emit_phi_resolution(current_block, target_block)
                    if phi_res:
                        res.append(phi_res)
            res.append(f"v_next_block := '{instr.target}';")
            return "\n".join(res)

        elif class_name == 'Branch':
            cond = self.emit_expression(instr.condition)
            true_phi = ""
            false_phi = ""
            if current_block and cfg:
                true_block = cfg.blocks.get(instr.true_target)
                if true_block:
                    true_phi = self._emit_phi_resolution(current_block, true_block)

                false_block = cfg.blocks.get(instr.false_target)
                if false_block:
                    false_phi = self._emit_phi_resolution(current_block, false_block)

            if true_phi or false_phi:
                 # Complex branch with phi resolution
                 code = f"IF {cond} THEN\n"
                 if true_phi:
                     code += self._indent(true_phi, 4) + "\n"
                 code += f"    v_next_block := '{instr.true_target}';\n"
                 code += "ELSE\n"
                 if false_phi:
                     code += self._indent(false_phi, 4) + "\n"
                 code += f"    v_next_block := '{instr.false_target}';\n"
                 code += "END IF;"
                 return code
            else:
                return f"v_next_block := CASE WHEN {cond} THEN '{instr.true_target}' ELSE '{instr.false_target}' END;"

        elif class_name == 'Report':
            return self._emit_report(instr)

        elif class_name == 'Match':
            return self._emit_match(instr)

        elif class_name == 'Call':
            args = [self.emit_expression(arg) for arg in instr.arguments]
            return f"/* CALL {instr.target}({', '.join(args)}) */"

        elif class_name == 'Join':
            self.active_joins.append(instr)
            all_kw = " ALL" if getattr(instr, 'is_all', False) else ""
            return f"/* JOIN {instr.left_file}.{instr.left_field} TO{all_kw} {instr.right_file}.{instr.right_field} */"

        elif class_name == 'JoinClear':
            self.active_joins = []
            return "/* JOIN CLEAR * */"

        elif class_name == 'SetEnv':
            return f"/* SET {instr.parameter} = {instr.value} */"

        elif class_name == 'Define':
            # Store virtual fields for relational lifting
            if instr.filename not in self.virtual_fields:
                self.virtual_fields[instr.filename] = {}
            for assignment in instr.assignments:
                # Store (expression, format)
                self.virtual_fields[instr.filename][assignment.name] = (assignment.expression, assignment.format)
            return f"/* DEFINE FILE {instr.filename} ... */"

        elif class_name == 'HtmlForm':
            if instr.filename:
                return f"/* -HTMLFORM {instr.filename} */"
            else:
                return f"/* -HTMLFORM BEGIN ... -HTMLFORM END */"

        elif class_name == 'Read':
            vars_str = " ". join(instr.variables)
            return f"/* -READ {instr.filename} {vars_str} */"

        elif class_name == 'Write':
            parts = [self.emit_expression(p) for p in instr.messages]
            return f"/* -WRITE {instr.filename} {' || '.join(parts)} */"

        elif class_name == 'Default':
            expr = self.emit_expression(instr.expression)
            return f"/* -DEFAULT {instr.variable} = {expr} */"

        elif class_name == 'CompoundLayout':
            return self._emit_compound_layout(instr)

        elif class_name == 'CompoundEnd':
            return "/* COMPOUND END */"

        return f"/* Unsupported instruction: {class_name} */"

    def _format_layout_value(self, val):
        """Helper to format layout values for comments."""
        if isinstance(val, list):
            return "(" + " ".join(self._format_layout_value(v) for v in val) + ")"
        return str(val)

    def _emit_layout_statements(self, statements, indent=0):
        """Helper to emit layout/style statements as comments."""
        res = []
        indent_str = " " * indent
        for stmt in statements:
            line = f"{indent_str}{stmt.name}={self._format_layout_value(stmt.value)}"
            if hasattr(stmt, 'properties') and stmt.properties:
                props = [f"{p.name}={self._format_layout_value(p.value)}" for p in stmt.properties]
                line += f", {', '.join(props)}"
            res.append(f"/* {line} */")
        return res

    def _emit_output_command(self, output):
        """Helper to emit output commands (HOLD, PCHOLD, etc.) as comments."""
        output_str = f"{output.output_type}"
        if output.filename:
            output_str += f" {output.filename}"
        if output.format:
            output_str += f" FORMAT {output.format}"
        if getattr(output, 'open_close', None):
            output_str += f" {output.open_close}"
        return f"/* {output_str} */"

    def _format_summarize(self, cmd):
        """Helper to format a SummarizeCommand (SUBTOTAL, RECOMPUTE, etc.) as a string."""
        parts = [cmd.verb]
        if cmd.options:
            if cmd.options.get("roll"):
                parts.append("ROLL.")
            prefixes = cmd.options.get("prefixes", [])
            for p in prefixes:
                parts.append(f"{p}.")

        if cmd.field:
            parts.append(cmd.field)

        if cmd.alias:
            parts.append(f"AS '{cmd.alias}'")

        return " ".join(parts)

    def _format_recap(self, cmd):
        """Helper to format a RecapCommand as a string."""
        lines = ["RECAP"]
        for assign in cmd.assignments:
            line = f"  {assign.name}"
            if assign.column_ref:
                col_ref = self.emit_expression(assign.column_ref)
                line += f"({col_ref})"

            if assign.format:
                line += f"/{assign.format}"

            expr = self.emit_expression(assign.expression)
            line += f" = {expr};"

            if assign.alias:
                line += f" AS '{assign.alias}'"
            if assign.indent:
                line += f" INDENT {assign.indent}"
            if assign.noprint:
                line += " NOPRINT"

            lines.append(line)
        return "\n".join(lines)

    def _emit_compound_layout(self, instr):
        """
        Translates ir.CompoundLayout instruction into SQL comments.
        """
        output_cmd_str = self._emit_output_command(instr.output_command)
        # Strip outer /* and */
        output_str = output_cmd_str.strip().lstrip('/*').rstrip('*/').strip()

        lines = [f"/* COMPOUND LAYOUT {output_str} */"]
        lines.extend(self._emit_layout_statements(instr.statements, indent=2))
        return "\n".join(lines)

    def _emit_report(self, instr):
        """
        Translates ir.Report instruction into a SQL SELECT statement.
        """
        filename = instr.filename

        # Check for MERGE command
        merge_cmd = None
        for comp in instr.components:
            if comp.__class__.__name__ == 'OnCommand' and comp.target == 'TABLE':
                for action in comp.actions:
                    if action.__class__.__name__ == 'MergeCommand':
                        merge_cmd = action
                        break
            if merge_cmd: break

        table_name = self._resolve_table_name(filename)
        alias_map = {filename: table_name}

        # Local copy of virtual fields for this report, merged from all possible joined files
        # Map: field_name -> (expression, format, original_filename)
        report_virtual_fields = {}
        if filename in self.virtual_fields:
            for f, (e, fmt) in self.virtual_fields[filename].items():
                report_virtual_fields[f] = (e, fmt, filename)

        # Populate alias map and merged virtual fields
        for join in instr.joins:
            right_table = self._resolve_table_name(join.right_file)
            right_alias = join.join_as if join.join_as else right_table
            alias_map[join.right_file] = right_alias

            if join.right_file in self.virtual_fields:
                for f, (e, fmt) in self.virtual_fields[join.right_file].items():
                    report_virtual_fields[f] = (e, fmt, join.right_file)

        # Analysis phase: identify used files and fields
        used_files = {filename}

        # Map from alias or filename to the original filename
        alias_to_filename = {filename: filename}
        for join in instr.joins:
            alias = join.join_as if join.join_as else join.right_file
            alias_to_filename[alias] = join.right_file
            alias_to_filename[join.right_file] = join.right_file

            # SAFE: Preserve INNER JOINs (non-outer) as they act as filters
            if not join.outer:
                used_files.add(join.right_file)

        def mark_field_used(fname, source_fn=None):
            if not fname: return
            if isinstance(fname, asg.ASGNode):
                self._collect_used_files_in_expr(fname, mark_field_used, source_fn)
                return

            if '.' in fname:
                parts = fname.split('.')
                qual = parts[0]
                if qual in alias_to_filename:
                    # Mark original filename as used
                    used_files.add(alias_to_filename[qual])
                    # Also mark the alias itself as used for dependency chain tracking
                    used_files.add(qual)
            elif source_fn:
                used_files.add(source_fn)
            elif fname in report_virtual_fields:
                expr, fmt, s_fn = report_virtual_fields[fname]
                used_files.add(s_fn)
                self._collect_used_files_in_expr(expr, mark_field_used, s_fn)
            else:
                # Unqualified name.
                # Without metadata, we assume it's the primary file,
                # unless it matches a virtual field which we already handled above.
                used_files.add(filename)

        # Get virtual fields for this file
        file_virtual_fields = {f: (e_fmt[0], e_fmt[1]) for f, e_fmt in report_virtual_fields.items()}

        for comp in instr.components:
            self._collect_used_files_recursive(comp, mark_field_used, used_files)

        # If * was found, we add all potential join targets
        if '*' in used_files:
            for join in instr.joins:
                used_files.add(join.right_file)
                if join.join_as:
                    used_files.add(join.join_as)

        # Ensure all files in a join chain are kept if their dependents are kept
        changed = True
        while changed:
            changed = False
            for join in instr.joins:
                alias = join.join_as if join.join_as else join.right_file
                # If either the filename or the alias is marked as used
                if join.right_file in used_files or alias in used_files:
                    if join.left_file not in used_files:
                        used_files.add(join.left_file)
                        changed = True

        # Build join clauses for used files only
        join_clauses = []
        for join in instr.joins:
            if join.right_file not in used_files:
                continue

            join_type = "LEFT OUTER JOIN" if join.outer else "JOIN"
            right_table = self._resolve_table_name(join.right_file)
            right_alias = alias_map[join.right_file]
            left_table_alias = alias_map.get(join.left_file, join.left_file)
            alias_part = f" {right_alias}" if right_alias != right_table else ""
            join_clauses.append(f"{join_type} {right_table}{alias_part} ON {left_table_alias}.{join.left_field} = {right_alias}.{join.right_field}")

        select_fields = []
        where_clauses = []
        group_by_fields = []
        order_by_phrases = []

        aggregating_verbs = ['SUM', 'COUNT']
        is_aggregating = False

        # Helper to qualify field names if joins are present
        def qualify_field(fname, source_fn=None):
            if not fname: return ""
            if '.' in fname:
                parts = fname.split('.')
                # Qualify with alias if file name is known
                if parts[0] in alias_map:
                    return f"{alias_map[parts[0]]}.{parts[1]}"
                return fname
            if not instr.joins:
                return fname

            # If a source_fn is explicitly provided (e.g. from a virtual field context)
            if source_fn:
                source_alias = alias_map.get(source_fn, source_fn)
                return f"{source_alias}.{fname}"

            # If it's a virtual field, we don't qualify the name itself,
            # but we will need to qualify its contents.
            if fname in report_virtual_fields:
                return fname

            # For now, let's assume it belongs to the primary table if not found in virtual fields.
            return f"{table_name}.{fname}"

        report_comments = []
        hold_command = None

        # Sort commands (BY, ACROSS)
        sort_commands = [c for c in instr.components if c.__class__.__name__ == 'SortCommand']
        for sc in sort_commands:
            field_name = sc.field.name
            sql_field_expr = qualify_field(field_name)
            if field_name in report_virtual_fields:
                 expr, fmt, source_fn = report_virtual_fields[field_name]
                 sql_field_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=lambda f: qualify_field(f, source_fn))

                 # Apply casting if format is Alpha fixed-length
                 if fmt and fmt.upper().startswith('A'):
                     pg_type = self._map_type(fmt)
                     if pg_type.startswith('CHAR'):
                         sql_field_expr = f"CAST({sql_field_expr} AS {pg_type})"

            direction = "DESC" if sc.options.get("order") == "HIGHEST" else "ASC"

            if sc.is_hierarchy:
                report_comments.append(f"/* BY {field_name} HIERARCHY */")

            # Use alias if present in FieldSelection
            display_name = sql_field_expr
            if sc.field.alias:
                display_name = f"{sql_field_expr} AS \"{sc.field.alias}\""
            elif field_name in file_virtual_fields:
                # If it's a virtual field, use its name as alias for the expression
                display_name = f"{sql_field_expr} AS \"{field_name}\""

            if not sc.noprint:
                select_fields.append(display_name)

            group_by_fields.append(sql_field_expr)
            order_by_phrases.append(f"{sql_field_expr} {direction}")

        # Handle PAGE-BREAK and other markers as comments
        for comp in instr.components:
            class_name = comp.__class__.__name__
            if class_name == 'PageBreak':
                report_comments.append("/* PAGE-BREAK */")
            elif class_name == 'SummarizeCommand':
                report_comments.append(f"/* {self._format_summarize(comp)} */")
            elif class_name == 'RecapCommand':
                report_comments.append(f"/* {self._format_recap(comp)} */")
            elif class_name == 'WhenCommand':
                cond = self.emit_expression(comp.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field)
                report_comments.append(f"/* WHEN {cond} */")
            elif class_name == 'ShowCommand':
                report_comments.append(f"/* SHOW {comp.from_direction} {comp.from_value.value} TO {comp.to_direction} {comp.to_value.value} */")
            elif class_name in ('Heading', 'Footing', 'Subhead', 'Subfoot'):
                centered = " CENTER" if getattr(comp, 'centered', False) else ""
                report_comments.append(f"/* {class_name.upper()}{centered} \"{comp.text}\" */")
            elif class_name == 'OutputCommand':
                if comp.output_type == 'HOLD':
                    hold_command = comp
                report_comments.append(self._emit_output_command(comp))
            elif class_name == 'StyleBlock':
                report_comments.append("/* SET STYLE * */")
                report_comments.extend(self._emit_layout_statements(comp.statements, indent=2))
                report_comments.append("/* ENDSTYLE */")
            elif class_name == 'OnCommand':
                for action in comp.actions:
                    action_class = action.__class__.__name__
                    if action_class == 'PageBreak':
                        report_comments.append(f"/* PAGE-BREAK ON {comp.target} */")
                    elif action_class == 'SummarizeCommand':
                        report_comments.append(f"/* ON {comp.target} {self._format_summarize(action)} */")
                    elif action_class == 'RecapCommand':
                        report_comments.append(f"/* ON {comp.target} {self._format_recap(action)} */")
                    elif action_class == 'OutputCommand':
                        if action.output_type == 'HOLD':
                            hold_command = action
                        report_comments.append(f"/* ON {comp.target} {self._emit_output_command(action).lstrip('/*').rstrip('*/').strip()} */")
                    elif action_class == 'StyleBlock':
                        report_comments.append(f"/* ON {comp.target} SET STYLE * */")
                        report_comments.extend(self._emit_layout_statements(action.statements, indent=2))
                        report_comments.append("/* ENDSTYLE */")

        # Aggregation detection
        group_by_names = []
        for sc in sort_commands:
            group_by_names.append(sc.field.name)

        # Verbs and Fields
        verb_commands = [c for c in instr.components if c.__class__.__name__ == 'VerbCommand']
        for vc in verb_commands:
            if vc.verb in aggregating_verbs:
                is_aggregating = True
                break
            # Check if any field has a prefix operator that implies aggregation
            for field_sel in vc.fields:
                if field_sel.prefix_operators:
                    is_aggregating = True
                    break
            if is_aggregating: break

        for vc in verb_commands:
            for field_sel in vc.fields:
                if field_sel.name == '*':
                    select_fields.append('*')
                    continue

                field_name = field_sel.name
                if isinstance(field_name, asg.ASGNode):
                    # For complex expressions, we don't want internal aggregation on every identifier
                    sql_expr = self.emit_expression(field_name, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field, aggregate=False, group_by_fields=group_by_names)
                    is_virtual = False
                else:
                    sql_expr = qualify_field(field_name)
                    is_virtual = field_name in report_virtual_fields

                # Relational Lifting: Virtual Field Substitution
                if is_virtual:
                    expr, fmt, source_fn = report_virtual_fields[field_name]
                    sql_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=lambda f: qualify_field(f, source_fn))

                    # Apply casting if format is Alpha fixed-length
                    if fmt and fmt.upper().startswith('A'):
                        pg_type = self._map_type(fmt)
                        if pg_type.startswith('CHAR'):
                            sql_expr = f"CAST({sql_expr} AS {pg_type})"

                # Prefix operators
                sql_expr = self._apply_prefixes(sql_expr, field_sel.prefix_operators, vc.verb, group_by_fields)

                if field_sel.alias:
                    sql_expr = f"{sql_expr} AS \"{field_sel.alias}\""
                elif is_virtual:
                    # If it's a virtual field, use its name as alias for the expression
                    sql_expr = f"{sql_expr} AS \"{field_name}\""
                elif merge_cmd:
                    # Ensure the column has a predictable name for MERGE
                    alias_name = field_name.split('.')[-1]
                    sql_expr = f"{sql_expr} AS \"{alias_name}\""

                select_fields.append(sql_expr)

        # COMPUTE commands
        compute_commands = [c for c in instr.components if c.__class__.__name__ == 'ComputeCommand']
        for cc in compute_commands:
            sql_expr = self.emit_expression(cc.expression, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field, aggregate=is_aggregating, group_by_fields=group_by_fields)

            # Apply casting if format is Alpha fixed-length
            if cc.format and cc.format.upper().startswith('A'):
                pg_type = self._map_type(cc.format)
                if pg_type.startswith('CHAR'):
                    sql_expr = f"CAST({sql_expr} AS {pg_type})"

            alias = getattr(cc, 'alias', None) or cc.name
            if alias:
                sql_expr = f"{sql_expr} AS \"{alias}\""
            select_fields.append(sql_expr)

        # WHERE and HAVING
        where_clauses = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field) for c in instr.components
                         if c.__class__.__name__ == 'WhereClause' and not c.is_total]
        having_clauses = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field, aggregate=is_aggregating, group_by_fields=group_by_fields) for c in instr.components
                          if c.__class__.__name__ == 'WhereClause' and c.is_total]

        if not select_fields:
            select_fields = ['*']

        if instr.more_clause:
            # Construct a UNION ALL of all data sources first
            source_queries = []

            # 1. Primary file source
            primary_src_fields = []
            # We must include all fields needed by the outer query: BY fields and PRINT/SUM fields
            # Actually, to make UNION ALL work, all branches must have the same columns.
            # We'll use the raw field names (no aggregations) for the inner sources.

            # Identify all unique raw fields needed
            needed_raw_fields = []
            for sc in sort_commands:
                if sc.field.name not in needed_raw_fields:
                    needed_raw_fields.append(sc.field.name)
            for vc in verb_commands:
                for f in vc.fields:
                    if f.name != '*' and f.name not in needed_raw_fields:
                        needed_raw_fields.append(f.name)

            def get_source_select(table_alias, fields, q_func):
                return [f"{q_func(f)} AS \"{f}\"" for f in fields]

            primary_select = get_source_select(table_name, needed_raw_fields, qualify_field)
            p_sql = f"SELECT {', '.join(primary_select)} FROM {table_name}"
            if join_clauses:
                p_sql += "\n" + "\n".join(join_clauses)
            if where_clauses:
                p_sql += "\nWHERE " + " AND ".join(where_clauses)
            source_queries.append(p_sql)

            # 2. MORE FILE sources
            for sub in instr.more_clause.sub_requests:
                sub_t = self._resolve_table_name(sub.filename)
                sub_q_func = lambda f: f"{sub_t}.{f}"
                sub_select = get_source_select(sub_t, needed_raw_fields, sub_q_func)
                s_sql = f"SELECT {', '.join(sub_select)} FROM {sub_t}"
                sub_where = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=sub_q_func)
                             for c in sub.where_clauses]
                if sub_where:
                    s_sql += "\nWHERE " + " AND ".join(sub_where)
                source_queries.append(s_sql)

            union_sql = "\nUNION ALL\n".join(source_queries)

            # Now build the outer query
            # Qualify everything to the "SRC" alias
            outer_qualify = lambda f: f"SRC.\"{f}\""

            outer_select = []
            for sc in sort_commands:
                if not sc.noprint:
                    outer_select.append(f"{outer_qualify(sc.field.name)}" + (f" AS \"{sc.field.alias}\"" if sc.field.alias else ""))

            outer_group_by = [outer_qualify(sc.field.name) for sc in sort_commands]
            for vc in verb_commands:
                for f_sel in vc.fields:
                    if f_sel.name == '*': continue
                    sql_f = outer_qualify(f_sel.name)
                    sql_f = self._apply_prefixes(sql_f, f_sel.prefix_operators, vc.verb, outer_group_by)

                    if f_sel.alias: sql_f = f"{sql_f} AS \"{f_sel.alias}\""
                    outer_select.append(sql_f)

            for cc in compute_commands:
                sql_e = self.emit_expression(cc.expression, in_query=True, virtual_fields=file_virtual_fields, qualifier=outer_qualify, aggregate=is_aggregating, group_by_fields=[])
                alias = getattr(cc, 'alias', None) or cc.name
                outer_select.append(f"{sql_e} AS \"{alias}\"")

            sql = f"/* {instr.filename} with MORE */"
            if report_comments:
                sql += "\n" + "\n".join(report_comments)

            sql += f"\nSELECT {', '.join(outer_select)} FROM (\n"
            sql += self._indent(union_sql, 4)
            sql += "\n) AS SRC"

            if is_aggregating and group_by_fields:
                outer_group_by = [outer_qualify(sc.field.name) for sc in sort_commands]
                sql += "\nGROUP BY " + ", ".join(outer_group_by)

            if having_clauses:
                 # Re-emit having clauses qualified to SRC
                 outer_having = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=outer_qualify, aggregate=is_aggregating, group_by_fields=[]) for c in instr.components
                          if c.__class__.__name__ == 'WhereClause' and c.is_total]
                 sql += "\nHAVING " + " AND ".join(outer_having)

            if order_by_phrases:
                outer_order_by = []
                for sc in sort_commands:
                     direction = "DESC" if sc.options.get("order") == "HIGHEST" else "ASC"
                     outer_order_by.append(f"{outer_qualify(sc.field.name)} {direction}")
                sql += "\nORDER BY " + ", ".join(outer_order_by)

        else:
            # Standard report logic (no MORE)
            sql = f"/* {instr.filename} */"
            if report_comments:
                sql += "\n" + "\n".join(report_comments)
            sql += f"\nSELECT {', '.join(select_fields)} FROM {table_name}"
            if join_clauses:
                sql += "\n" + "\n".join(join_clauses)

            if where_clauses:
                sql += "\nWHERE " + " AND ".join(where_clauses)

            if is_aggregating and group_by_fields:
                sql += "\nGROUP BY " + ", ".join(group_by_fields)

            if having_clauses:
                sql += "\nHAVING " + " AND ".join(having_clauses)

            if order_by_phrases:
                sql += "\nORDER BY " + ", ".join(order_by_phrases)

        if hold_command:
            hold_name = hold_command.filename or "HOLD"
            # Sanitize hold name for SQL table name
            hold_name = hold_name.replace('.', '_').replace('-', '_')

            hold_sql = f"DROP TABLE IF EXISTS {hold_name};\n"
            hold_sql += f"CREATE TEMP TABLE {hold_name} AS\n"
            hold_sql += sql
            sql = hold_sql

        if merge_cmd:
            target_table = self._resolve_table_name(merge_cmd.filename)

            # Build ON condition
            on_conds = []
            for left, right in merge_cmd.matching_clause.conditions:
                # Map TRG and SRC to their respective aliases if used
                # In PostgreSQL MERGE, we can alias target and source.
                on_conds.append(f"({left} = {right})")
            on_clause = " AND ".join(on_conds)

            merge_sql = f"MERGE INTO {target_table} AS TRG\nUSING (\n"
            merge_sql += self._indent(sql, 4) + "\n) AS SRC\n"
            merge_sql += f"ON {on_clause}\n"

            if merge_cmd.when_matched:
                updates = []
                for field, expr in merge_cmd.when_matched.assignments:
                    sql_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field)
                    updates.append(f"\"{field}\" = {sql_expr}")
                merge_sql += "WHEN MATCHED THEN\n  UPDATE SET " + ", ".join(updates) + "\n"

            if merge_cmd.when_not_matched:
                fields = []
                values = []
                for field, expr in merge_cmd.when_not_matched.assignments:
                    sql_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field)
                    fields.append(f"\"{field}\"")
                    values.append(sql_expr)
                merge_sql += "WHEN NOT MATCHED THEN\n  INSERT (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ");"
            else:
                merge_sql += ";"

            return merge_sql

        sql += ";"
        return sql

    def _emit_match(self, instr):
        """
        Translates ir.Match instruction into a SQL SELECT statement using CTEs.
        """
        if not instr.sub_matches:
            return f"/* MATCH FILE {instr.filename} with no sub-matches */"

        def process_match_request(filename, components):
            table_name = self._resolve_table_name(filename)

            select_fields = []
            group_by_fields = []
            value_fields = []

            # BY fields
            for comp in components:
                if comp.__class__.__name__ == 'SortCommand' and comp.sort_type == 'BY':
                    f_name = comp.field.name
                    select_fields.append(f"\"{f_name}\"")
                    group_by_fields.append(f"\"{f_name}\"")

            # Verb fields
            for comp in components:
                if comp.__class__.__name__ == 'VerbCommand':
                    for f_sel in comp.fields:
                        if f_sel.name == '*': continue
                        f_name = f_sel.name
                        if f"\"{f_name}\"" in group_by_fields: continue

                        alias = f_sel.alias or f_name
                        if comp.verb == 'SUM':
                            select_fields.append(f"SUM(\"{f_name}\") AS \"{alias}\"")
                        elif comp.verb == 'COUNT':
                            select_fields.append(f"COUNT(\"{f_name}\") AS \"{alias}\"")
                        else:
                            select_fields.append(f"\"{f_name}\" AS \"{alias}\"")
                        value_fields.append(alias)

            # COMPUTE fields
            for comp in components:
                if comp.__class__.__name__ == 'ComputeCommand':
                    sql_expr = self.emit_expression(
                        comp.expression,
                        in_query=True,
                        virtual_fields=self.virtual_fields.get(filename, {}),
                        qualifier=lambda f: f"\"{f}\"" if '.' not in f else f
                    )
                    alias = getattr(comp, 'alias', None) or comp.name
                    select_fields.append(f"{sql_expr} AS \"{alias}\"")
                    value_fields.append(alias)

            # Where clauses
            where_clauses = []
            for comp in components:
                if comp.__class__.__name__ == 'WhereClause':
                    where_clauses.append(self.emit_expression(
                        comp.condition,
                        in_query=True,
                        virtual_fields=self.virtual_fields.get(filename, {}),
                        qualifier=lambda f: f"\"{f}\"" if '.' not in f else f
                    ))

            sql = f"SELECT {', '.join(select_fields)} FROM {table_name}"
            if where_clauses:
                sql += f" WHERE {' AND '.join(where_clauses)}"
            if group_by_fields:
                sql += f" GROUP BY {', '.join(group_by_fields)}"
            return sql, [f.strip('"') for f in group_by_fields], value_fields

        # CTE definitions
        ctes = []
        sql_first, keys_first, vals_first = process_match_request(instr.filename, instr.components)
        ctes.append(f"T1 AS (\n{self._indent(sql_first, 4)}\n)")

        # Sequential merges
        current_name = "T1"
        current_keys = keys_first
        current_vals = vals_first

        for idx, sub in enumerate(instr.sub_matches):
            source_idx = idx + 2
            sql_sub, keys_sub, vals_sub = process_match_request(sub.filename, sub.components)
            ctes.append(f"T{source_idx} AS (\n{self._indent(sql_sub, 4)}\n)")

            merge_name = f"M{idx + 1}"
            merge_type = "OLD-OR-NEW"
            if sub.after_match:
                merge_type = sub.after_match.merge_type.upper().replace('_', '-')

            # Determine JOIN type and WHERE filter
            join_clause = "FULL OUTER JOIN"
            where_filter = None

            if merge_type == 'OLD-AND-NEW':
                join_clause = "INNER JOIN"
            elif merge_type == 'OLD-NOT-NEW':
                join_clause = "LEFT JOIN"
                where_filter = f"T{source_idx}.\"{keys_sub[0]}\" IS NULL"
            elif merge_type == 'OLD':
                join_clause = "LEFT JOIN"
            elif merge_type == 'NEW-NOT-OLD':
                join_clause = "RIGHT JOIN"
                where_filter = f"{current_name}.\"{current_keys[0]}\" IS NULL"
            elif merge_type == 'NEW':
                join_clause = "RIGHT JOIN"
            elif merge_type == 'OLD-NOR-NEW':
                join_clause = "FULL OUTER JOIN"
                where_filter = f"{current_name}.\"{current_keys[0]}\" IS NULL OR T{source_idx}.\"{keys_sub[0]}\" IS NULL"

            # Build the merge CTE
            merge_sel = []
            for i in range(min(len(current_keys), len(keys_sub))):
                k_curr = current_keys[i]
                k_sub = keys_sub[i]
                merge_sel.append(f"COALESCE({current_name}.\"{k_curr}\", T{source_idx}.\"{k_sub}\") AS \"{k_curr}\"")

            for v in current_vals:
                merge_sel.append(f"{current_name}.\"{v}\"")
            for v in vals_sub:
                merge_sel.append(f"T{source_idx}.\"{v}\"")

            on_conds = []
            for i in range(min(len(current_keys), len(keys_sub))):
                on_conds.append(f"{current_name}.\"{current_keys[i]}\" = T{source_idx}.\"{keys_sub[i]}\"")

            m_sql = f"SELECT {', '.join(merge_sel)}\nFROM {current_name} {join_clause} T{source_idx} ON {' AND '.join(on_conds)}"
            if where_filter:
                m_sql += f"\nWHERE {where_filter}"

            ctes.append(f"{merge_name} AS (\n{self._indent(m_sql, 4)}\n)")

            current_name = merge_name
            current_vals = current_vals + vals_sub
            # Keys remain derived from the first file's naming convention for consistency in the chain

        # Check for HOLD command in components
        hold_command = None
        for comp in instr.components:
            if isinstance(comp, asg.OutputCommand) and comp.output_type == 'HOLD':
                hold_command = comp
                break

        res = ""
        query = "WITH\n" + ",\n".join(ctes) + "\n"
        query += f"SELECT * FROM {current_name}"

        if hold_command:
            hold_name = hold_command.filename or "HOLD"
            hold_name = hold_name.replace('.', '_').replace('-', '_')
            res += f"DROP TABLE IF EXISTS {hold_name};\n"
            res += f"CREATE TEMP TABLE {hold_name} AS\n"
            res += query + ";"
        else:
            res += query + ";"

        return res

    def _resolve_table_name(self, filename):
        """
        Resolves a WebFOCUS filename to a SQL table name.
        """
        if self.metadata_registry:
            master = self.metadata_registry.get_master_file(filename)
            if master:
                return master.name
        return filename

    def emit_block(self, block, cfg):
        """
        Translates a basic block into PL/pgSQL code.
        """
        lines = []
        for instr in block.instructions:
            if isinstance(instr, ir.Phi):
                continue # Phi nodes are handled by predecessors

            lines.append(self.emit_instruction(instr, block, cfg))

        # Handle terminator if not already handled (e.g. fallthrough)
        last_instr = block.instructions[-1] if block.instructions else None
        if not isinstance(last_instr, (ir.Jump, ir.Branch)):
            if block.successors:
                # Assuming single successor for fallthrough or last-block logic
                succ = block.successors[0]
                phi_res = self._emit_phi_resolution(block, succ)
                if phi_res:
                    lines.append(phi_res)
                lines.append(f"v_next_block := '{succ.name}';")
            else:
                lines.append("v_next_block := 'EXIT';")

        return "\n".join(lines)

    def emit_cfg(self, cfg):
        """
        Generates a PL/pgSQL body from a ControlFlowGraph using a block dispatcher.
        Optimizes simple loops into native PL/pgSQL loops.
        """
        if not cfg.entry_block:
            return ""

        # Identify simple loops
        loops = {}
        consumed_blocks = set()
        for b_name in cfg.blocks:
            loop = find_simple_for_loop(cfg, b_name)
            if not loop:
                loop = find_simple_while_loop(cfg, b_name)

            if loop:
                loops[b_name] = loop
                consumed_blocks.update(loop['body_blocks'])
                consumed_blocks.add(loop['closing_block'])

        blocks_code = []
        for block_name, block in cfg.blocks.items():
            if block_name in consumed_blocks:
                continue

            if block_name in loops:
                loop = loops[block_name]
                loop_code = ""

                if loop['type'] == 'FOR':
                    # Emit native FOR loop
                    counter = self._sanitize_name(loop['counter'])
                    start = self.emit_expression(loop['start'])
                    limit = self.emit_expression(loop['limit'])
                    step_val = loop['step']

                    step_clause = ""
                    if isinstance(step_val, asg.Literal) and step_val.value != 1:
                        step_clause = f" BY {step_val.value}"
                    elif not isinstance(step_val, asg.Literal):
                        step_clause = f" BY {self.emit_expression(step_val)}"

                    loop_body_lines = []
                    for b_in_loop in loop['body_blocks']:
                        b = cfg.blocks[b_in_loop]
                        # Emit only instructions, ignoring the terminal jump
                        for instr in b.instructions:
                            loop_body_lines.append(self.emit_instruction(instr, b, cfg))

                    # Also include instructions from closing block BEFORE the increment/jump
                    cb = cfg.blocks[loop['closing_block']]
                    for instr in cb.instructions[:-2]:
                        loop_body_lines.append(self.emit_instruction(instr, cb, cfg))

                    indented_body = self._indent("\n".join(loop_body_lines), 4)
                    loop_code = f"FOR {counter} IN {start}..{limit}{step_clause} LOOP\n{indented_body}\nEND LOOP;\n"
                    loop_code += f"v_next_block := '{loop['after_block']}';"

                elif loop['type'] == 'WHILE':
                    cond = self.emit_expression(loop['condition'])

                    loop_body_lines = []
                    for b_in_loop in loop['body_blocks']:
                        b = cfg.blocks[b_in_loop]
                        # Emit only instructions, ignoring the terminal jump
                        for instr in b.instructions:
                            loop_body_lines.append(self.emit_instruction(instr, b, cfg))

                    # Also include instructions from closing block BEFORE the jump
                    cb = cfg.blocks[loop['closing_block']]
                    for instr in cb.instructions[:-1]:
                        loop_body_lines.append(self.emit_instruction(instr, cb, cfg))

                    indented_body = self._indent("\n".join(loop_body_lines), 4)
                    loop_code = f"WHILE {cond} LOOP\n{indented_body}\nEND LOOP;\n"
                    loop_code += f"v_next_block := '{loop['after_block']}';"

                blocks_code.append(f"        WHEN '{block_name}' THEN\n{self._indent(loop_code, 8)}")
                continue

            block_code = self.emit_block(block, cfg)
            indented_block = self._indent(block_code, 8)
            blocks_code.append(f"        WHEN '{block_name}' THEN\n{indented_block}")

        # Add a default EXIT block handling if not present
        if 'EXIT' not in cfg.blocks:
             blocks_code.append("        WHEN 'EXIT' THEN\n            v_next_block := 'DONE';")

        case_statement = "    CASE v_next_block\n" + "\n".join(blocks_code) + "\n    END CASE;"

        loop_code = f"v_next_block := '{cfg.entry_block.name}';\n"
        loop_code += f"WHILE v_next_block NOT IN ('EXIT', 'DONE') LOOP\n"
        loop_code += case_statement + "\n"
        loop_code += "END LOOP;"

        return loop_code

    def _emit_phi_resolution(self, from_block, to_block):
        """
        Generates copy instructions to resolve Phi nodes when transitioning between blocks.
        """
        res = []
        try:
            pred_index = to_block.predecessors.index(from_block)
        except ValueError:
            return ""

        for instr in to_block.instructions:
            if isinstance(instr, ir.Phi):
                target = self._sanitize_name(instr.target)
                source = self._sanitize_name(instr.sources[pred_index])
                res.append(f"{target} := {source};")

        return "\n".join(res)

    def _collect_used_files_recursive(self, node, mark_field_used, used_files=None):
        if node is None: return
        class_name = node.__class__.__name__

        if class_name == 'VerbCommand':
            for f in node.fields:
                if f.name == '*':
                    # If PRINT * is used, we must keep all files
                    if used_files is not None:
                        used_files.add('*')
                else:
                    mark_field_used(f.name)
        elif class_name == 'SortCommand':
            mark_field_used(node.field.name)
        elif class_name == 'ComputeCommand':
            self._collect_used_files_in_expr(node.expression, mark_field_used)
        elif class_name == 'WhereClause':
            self._collect_used_files_in_expr(node.condition, mark_field_used)
        elif class_name == 'WhenCommand':
            self._collect_used_files_in_expr(node.condition, mark_field_used)
        elif class_name == 'OnCommand':
            for action in node.actions:
                self._collect_used_files_recursive(action, mark_field_used)

    def _collect_used_files_in_expr(self, expr, mark_field_used, source_fn=None):
        if expr is None: return
        class_name = expr.__class__.__name__

        if class_name == 'Identifier':
            mark_field_used(expr.name, source_fn)
        elif class_name == 'BinaryOperation':
            self._collect_used_files_in_expr(expr.left, mark_field_used, source_fn)
            self._collect_used_files_in_expr(expr.right, mark_field_used, source_fn)
        elif class_name == 'UnaryOperation':
            self._collect_used_files_in_expr(expr.operand, mark_field_used, source_fn)
        elif class_name == 'FunctionCall':
            for arg in expr.arguments:
                self._collect_used_files_in_expr(arg, mark_field_used, source_fn)
        elif class_name == 'IfExpression':
            self._collect_used_files_in_expr(expr.condition, mark_field_used, source_fn)
            self._collect_used_files_in_expr(expr.then_expr, mark_field_used, source_fn)
            self._collect_used_files_in_expr(expr.else_expr, mark_field_used, source_fn)
        elif class_name == 'BetweenExpression':
            self._collect_used_files_in_expr(expr.expression, mark_field_used, source_fn)
            self._collect_used_files_in_expr(expr.lower, mark_field_used, source_fn)
            self._collect_used_files_in_expr(expr.upper, mark_field_used, source_fn)
        elif class_name == 'InExpression':
            self._collect_used_files_in_expr(expr.expression, mark_field_used, source_fn)
            for val in expr.values:
                self._collect_used_files_in_expr(val, mark_field_used, source_fn)
        elif class_name == 'IsMissingExpression':
            self._collect_used_files_in_expr(expr.expression, mark_field_used, source_fn)

    def _apply_prefixes(self, sql_expr, prefixes, verb=None, group_by=None):
        """
        Applies WebFOCUS prefix operators to a SQL expression.
        """
        if not prefixes:
            if verb == 'SUM':
                return f"SUM({sql_expr})"
            if verb == 'COUNT':
                return f"COUNT({sql_expr})"
            return sql_expr

        # Normalize prefixes
        prefixes = [p.upper() for p in prefixes]
        is_distinct = 'DST' in prefixes

        # MDN (Median) and MDE (Mode) have special syntax in PostgreSQL
        if 'MDN' in prefixes:
            return f"PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY {sql_expr})"
        if 'MDE' in prefixes:
            return f"MODE() WITHIN GROUP (ORDER BY {sql_expr})"

        # ASQ: average sum of squares
        if 'ASQ' in prefixes:
            distinct_str = "DISTINCT " if is_distinct else ""
            return f"AVG({distinct_str}({sql_expr}) * ({sql_expr}))"

        # Advanced operators using ordered aggregates (compatible with GROUP BY)
        order_by_clause = f"ORDER BY {', '.join(group_by)}" if group_by else ""

        if 'FST' in prefixes:
            if order_by_clause:
                return f"(ARRAY_AGG({sql_expr} {order_by_clause}))[1]"
            return f"MIN({sql_expr})" # Fallback if no sort order
        if 'LST' in prefixes:
            if order_by_clause:
                return f"(ARRAY_AGG({sql_expr} {order_by_clause}))[ARRAY_UPPER(ARRAY_AGG({sql_expr} {order_by_clause}), 1)]"
            return f"MAX({sql_expr})" # Fallback if no sort order
        if 'RNK' in prefixes:
            # Rank usually descending
            base_expr = sql_expr
            if verb == 'SUM' and not any(p in prefixes for p in ['AVE', 'MIN', 'MAX', 'CNT', 'TOT', 'CT']):
                base_expr = f"SUM({sql_expr})"
            elif verb == 'COUNT':
                base_expr = f"COUNT({sql_expr})"

            partition = f"PARTITION BY {', '.join(group_by)}" if group_by else ""
            return f"RANK() OVER ({partition} ORDER BY {base_expr} DESC)"
        if 'PCT' in prefixes or 'RPCT' in prefixes:
            base_expr = sql_expr
            if verb == 'SUM' and not any(p in prefixes for p in ['AVE', 'MIN', 'MAX', 'CNT', 'TOT', 'CT']):
                base_expr = f"SUM({sql_expr})"
            elif verb == 'COUNT':
                base_expr = f"COUNT({sql_expr})"
            return f"({base_expr} * 100.0 / SUM({base_expr}) OVER ())"

        # Mapping for standard aggregates
        prefix_map = {
            'AVE': 'AVG',
            'MIN': 'MIN',
            'MAX': 'MAX',
            'SUM': 'SUM',
            'TOT': 'SUM',
            'CNT': 'COUNT',
            'CT': 'COUNT'
        }

        agg_func = None
        for p in prefixes:
            if p in prefix_map:
                agg_func = prefix_map[p]
                break

        # Standalone DST implies COUNT(DISTINCT ...)
        if not agg_func and is_distinct:
            agg_func = 'COUNT'

        if agg_func:
            distinct_str = "DISTINCT " if is_distinct else ""
            return f"{agg_func}({distinct_str}{sql_expr})"

        return sql_expr

    def _indent(self, text, spaces):
        """
        Indents the given text by the specified number of spaces.
        """
        prefix = ' ' * spaces
        return '\n'.join(prefix + line if line.strip() else line for line in text.splitlines())
