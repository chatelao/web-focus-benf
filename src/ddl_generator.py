from asg import MasterFile, Segment, Field
from type_mapper import map_wf_type_to_pg

class DDLGenerator:
    """
    Generates PostgreSQL DDL (CREATE TABLE) statements from Master File metadata.
    """
    def generate(self, master_file: MasterFile):
        """
        Generates CREATE TABLE statements for all segments in the Master File.
        """
        ddl_statements = []
        for segment in master_file.segments:
            ddl_statements.append(self._generate_create_table(segment))
        return "\n\n".join(ddl_statements)

    def _generate_create_table(self, segment: Segment):
        """
        Generates a single CREATE TABLE statement for a segment.
        """
        table_name = segment.name.upper()
        columns = []
        for field in segment.fields:
            column_name = field.name.upper()
            pg_type = map_wf_type_to_pg(field.format)
            columns.append(f"    {column_name} {pg_type}")

        columns_str = ",\n".join(columns)
        return f"CREATE TABLE {table_name} (\n{columns_str}\n);"
