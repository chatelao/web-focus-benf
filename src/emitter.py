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
