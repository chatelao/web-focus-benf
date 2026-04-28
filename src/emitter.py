import os
import ir
import asg
from jinja2 import Environment, FileSystemLoader, select_autoescape

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

                    if not data_type:
                        data_type = 'A' # Default to Alpha

                    if sql_name not in variables:
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
            clean_name = name.lstrip('&')
            # Replace common invalid chars with underscore
            clean_name = clean_name.replace('-', '_').replace('.', '_')
            return f"v_{clean_name}"
        return name

    def _map_type(self, data_type):
        """
        Maps WebFOCUS types to PostgreSQL types.
        """
        mapping = {
            'I': 'INTEGER',
            'F': 'NUMERIC',
            'A': 'TEXT',
            'LOGICAL': 'BOOLEAN'
        }
        return mapping.get(data_type, 'TEXT')

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
                    new_kwargs = kwargs.copy()
                    new_kwargs['aggregate'] = False
                    expanded = self.emit_expression(virtual_fields[expr.name], **new_kwargs)
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
                'CONCAT': '||'
            }
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
                self.virtual_fields[instr.filename][assignment.name] = assignment.expression
            return f"/* DEFINE FILE {instr.filename} ... */"

        elif class_name == 'CompoundLayout':
            return self._emit_compound_layout(instr)

        elif class_name == 'CompoundEnd':
            return "/* COMPOUND END */"

        return f"/* Unsupported instruction: {class_name} */"

    def _emit_compound_layout(self, instr):
        """
        Translates ir.CompoundLayout instruction into SQL comments.
        """
        output = instr.output_command
        output_str = f"{output.output_type}"
        if output.filename:
            output_str += f" {output.filename}"
        if output.format:
            output_str += f" FORMAT {output.format}"

        lines = [f"/* COMPOUND LAYOUT {output_str} */"]
        for stmt in instr.statements:
            line = f"/*   {stmt.name}={stmt.value}"
            if stmt.properties:
                props = [f"{p.name}={p.value}" for p in stmt.properties]
                line += f", {', '.join(props)}"
            line += " */"
            lines.append(line)
        return "\n".join(lines)

    def _emit_report(self, instr):
        """
        Translates ir.Report instruction into a SQL SELECT statement.
        """
        filename = instr.filename
        table_name = self._resolve_table_name(filename)
        alias_map = {filename: table_name}

        # Handle joins
        join_clauses = []
        # Local copy of virtual fields for this report, merged from joined files
        # Map: field_name -> (expression, original_filename)
        report_virtual_fields = {f: (e, filename) for f, e in self.virtual_fields.get(filename, {}).items()}

        for join in instr.joins:
            join_type = "LEFT OUTER JOIN" if join.outer else "JOIN"
            right_table = self._resolve_table_name(join.right_file)
            right_alias = join.join_as if join.join_as else right_table
            alias_map[join.right_file] = right_alias

            # Merge virtual fields from joined file
            if join.right_file in self.virtual_fields:
                for f, e in self.virtual_fields[join.right_file].items():
                    report_virtual_fields[f] = (e, join.right_file)

            # Resolve left field - might need qualification if multiple tables
            left_table_alias = alias_map.get(join.left_file, join.left_file)
            alias_part = f" {right_alias}" if right_alias != right_table else ""

            join_clauses.append(f"{join_type} {right_table}{alias_part} ON {left_table_alias}.{join.left_field} = {right_alias}.{join.right_field}")

        # Get virtual fields for this file
        file_virtual_fields = {f: e for f, (e, fn) in report_virtual_fields.items()}
        select_fields = []
        where_clauses = []
        group_by_fields = []
        order_by_phrases = []

        aggregating_verbs = ['SUM', 'COUNT']
        is_aggregating = False

        # Helper to qualify field names if joins are present
        def qualify_field(fname, source_fn=None):
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

        # Sort commands (BY, ACROSS)
        sort_commands = [c for c in instr.components if c.__class__.__name__ == 'SortCommand']
        for sc in sort_commands:
            field_name = sc.field.name
            sql_field_expr = qualify_field(field_name)
            if field_name in report_virtual_fields:
                 expr, source_fn = report_virtual_fields[field_name]
                 sql_field_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=lambda f: qualify_field(f, source_fn))

            direction = "DESC" if sc.options.get("order") == "HIGHEST" else "ASC"

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

        # Verbs and Fields
        verb_commands = [c for c in instr.components if c.__class__.__name__ == 'VerbCommand']
        for vc in verb_commands:
            if vc.verb in aggregating_verbs:
                is_aggregating = True

            for field_sel in vc.fields:
                if field_sel.name == '*':
                    select_fields.append('*')
                    continue

                field_name = field_sel.name
                sql_expr = qualify_field(field_name)

                # Relational Lifting: Virtual Field Substitution
                is_virtual = field_name in report_virtual_fields
                if is_virtual:
                    expr, source_fn = report_virtual_fields[field_name]
                    sql_expr = self.emit_expression(expr, in_query=True, virtual_fields=file_virtual_fields, qualifier=lambda f: qualify_field(f, source_fn))

                # Prefix operators
                prefix = field_sel.prefix_operators[0] if field_sel.prefix_operators else None
                if prefix:
                    prefix_map = {
                        'AVE': 'AVG',
                        'MIN': 'MIN',
                        'MAX': 'MAX',
                        'SUM': 'SUM',
                        'CNT': 'COUNT',
                        'TOT': 'SUM'
                    }
                    agg_func = prefix_map.get(prefix)
                    if agg_func:
                        sql_expr = f"{agg_func}({sql_expr})"
                elif vc.verb == 'SUM':
                    sql_expr = f"SUM({sql_expr})"
                elif vc.verb == 'COUNT':
                    sql_expr = f"COUNT({sql_expr})"

                if field_sel.alias:
                    sql_expr = f"{sql_expr} AS \"{field_sel.alias}\""
                elif is_virtual:
                    # If it's a virtual field, use its name as alias for the expression
                    sql_expr = f"{sql_expr} AS \"{field_name}\""

                select_fields.append(sql_expr)

        # COMPUTE commands
        compute_commands = [c for c in instr.components if c.__class__.__name__ == 'ComputeCommand']
        for cc in compute_commands:
            sql_expr = self.emit_expression(cc.expression, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field, aggregate=is_aggregating, group_by_fields=group_by_fields)
            if cc.name:
                sql_expr = f"{sql_expr} AS \"{cc.name}\""
            select_fields.append(sql_expr)

        # WHERE and HAVING
        where_clauses = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field) for c in instr.components
                         if c.__class__.__name__ == 'WhereClause' and not c.is_total]
        having_clauses = [self.emit_expression(c.condition, in_query=True, virtual_fields=file_virtual_fields, qualifier=qualify_field, aggregate=is_aggregating, group_by_fields=group_by_fields) for c in instr.components
                          if c.__class__.__name__ == 'WhereClause' and c.is_total]

        if not select_fields:
            select_fields = ['*']

        sql = f"/* {instr.filename} */\nSELECT {', '.join(select_fields)} FROM {table_name}"
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

        sql += ";"
        return sql

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
        """
        if not cfg.entry_block:
            return ""

        blocks_code = []
        for block_name, block in cfg.blocks.items():
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

    def _indent(self, text, spaces):
        """
        Indents the given text by the specified number of spaces.
        """
        prefix = ' ' * spaces
        return '\n'.join(prefix + line if line.strip() else line for line in text.splitlines())
