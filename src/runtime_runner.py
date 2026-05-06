import psycopg2
from db_utils import get_db_connection
from ddl_generator import DDLGenerator
from fixture_loader import FixtureLoader

class RuntimeRunner:
    """
    Executes transpiled PL/pgSQL procedures and captures runtime information,
    including PostgreSQL notices.
    """
    def __init__(self):
        self.conn = None

    def __enter__(self):
        if not self.conn:
            self.conn = get_db_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            self.conn = None

    def setup_schema(self, master_files):
        """
        Generates and executes DDL for the given list of MasterFile objects.
        """
        generator = DDLGenerator()
        if not self.conn:
            with self:
                self._setup_schema_internal(generator, master_files)
        else:
            self._setup_schema_internal(generator, master_files)

    def _setup_schema_internal(self, generator, master_files):
        with self.conn.cursor() as cursor:
            for master in master_files:
                ddl = generator.generate(master)
                cursor.execute(ddl)

    def load_fixtures(self, fixtures_config):
        """
        Populates tables using FixtureLoader.
        fixtures_config: list of (table_name, filepath) tuples.
        """
        loader = FixtureLoader()
        for table_name, filepath in fixtures_config:
            if filepath.endswith('.json'):
                loader.load_json(table_name, filepath)
            elif filepath.endswith('.csv'):
                loader.load_csv(table_name, filepath)

    def run_procedure(self, sql, procedure_name="webfocus_procedure"):
        """
        Executes a SQL string as a PL/pgSQL procedure and returns captured notices.
        """
        if not self.conn:
            with self:
                return self._run_internal(sql, procedure_name)
        return self._run_internal(sql, procedure_name)

    def _run_internal(self, sql, procedure_name):
        notices = []
        # Clear existing notices
        del self.conn.notices[:]

        try:
            with self.conn.cursor() as cursor:
                # 1. Define the procedure
                cursor.execute(sql)

                # 2. Call the procedure
                cursor.execute(f"CALL {procedure_name}();")

                # 3. Capture notices
                for notice in self.conn.notices:
                    # notices in psycopg2 might have trailing newlines or "NOTICE: " prefix
                    clean_notice = notice.strip()
                    if clean_notice.startswith("NOTICE:  "):
                        clean_notice = clean_notice[len("NOTICE:  "):]
                    notices.append(clean_notice)
        except psycopg2.Error as e:
            diag = getattr(e, 'diag', None)
            if diag:
                error_msg = f"PostgreSQL Runtime Error: {diag.message_primary}"
                if diag.message_detail:
                    error_msg += f"\nDetail: {diag.message_detail}"
                if diag.context:
                    error_msg += f"\nContext: {diag.context}"
                if diag.internal_position:
                    error_msg += f"\nPosition: {diag.internal_position}"
                raise Exception(error_msg) from e
            else:
                raise Exception(f"PostgreSQL Runtime Error: {str(e)}") from e

        return notices
