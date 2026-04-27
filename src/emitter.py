import os
from jinja2 import Environment, FileSystemLoader

class PostgresEmitter:
    """
    Handles the emission of PostgreSQL code from IR using Jinja2 templates.
    """
    def __init__(self, template_dir=None):
        if template_dir is None:
            # Default to the templates directory relative to this file
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def emit_procedure(self, procedure_name, parameters, variables, body):
        """
        Renders a PL/pgSQL procedure using the base template.
        """
        template = self.env.get_template('base.sql.j2')
        return template.render(
            procedure_name=procedure_name,
            parameters=parameters,
            variables=variables,
            body=body
        )
