import os
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
        for block in cfg.blocks.values():
            for instr in block.instructions:
                target = getattr(instr, 'target', None)
                if target:
                    sql_name = self._sanitize_name(target)

                    # Try to get data type from instruction, then from source expression
                    data_type = getattr(instr, 'data_type', None)
                    if not data_type and hasattr(instr, 'source'):
                        data_type = getattr(instr.source, 'data_type', None)

                    if not data_type:
                        data_type = 'A' # Default to Alpha

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

    def _discover_vars_in_expr(self, instr, variables):
        """
        Placeholder for discovering variables in expressions if needed.
        Currently assuming SSA renaming has identified all variables as targets.
        """
        pass

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

    def emit_instruction(self, instr):
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
            # Control flow instructions might be handled by a higher-level
            # state machine or block dispatcher, but providing a basic mapping.
            return f"/* JUMP to {instr.target} */"

        elif class_name == 'Branch':
            cond = self.emit_expression(instr.condition)
            return f"/* BRANCH IF {cond} TO {instr.true_target} ELSE {instr.false_target} */"

        return f"/* Unsupported instruction: {class_name} */"
