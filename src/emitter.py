import os
import ir
import asg
from jinja2 import Environment, FileSystemLoader, select_autoescape

class PostgresEmitter:
    """
    Generates PostgreSQL code from IR using Jinja2 templates.
    """
    def __init__(self, template_dir=None):
        if template_dir is None:
            # Default to src/templates relative to this file
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['sql']),
            trim_blocks=True,
            lstrip_blocks=True
        )

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

    def emit_expression(self, expr):
        """
        Translates ASG expression nodes to PostgreSQL SQL strings.
        """
        if expr is None:
            return "NULL"

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
            return self._sanitize_name(expr.name)

        elif class_name == 'BinaryOperation':
            left = self.emit_expression(expr.left)
            right = self.emit_expression(expr.right)
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
            operand = self.emit_expression(expr.operand)
            op = expr.operator.upper()
            op_mapping = {
                'NOT': 'NOT ',
            }
            sql_op = op_mapping.get(op, op)
            return f"{sql_op}({operand})"

        elif class_name == 'FunctionCall':
            args = [self.emit_expression(arg) for arg in expr.arguments]
            return f"{expr.function_name}({', '.join(args)})"

        elif class_name == 'IfExpression':
            cond = self.emit_expression(expr.condition)
            then_e = self.emit_expression(expr.then_expr)
            else_e = self.emit_expression(expr.else_expr)
            return f"(CASE WHEN {cond} THEN {then_e} ELSE {else_e} END)"

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

        return f"/* Unsupported instruction: {class_name} */"

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
