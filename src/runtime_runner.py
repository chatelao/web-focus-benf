from db_utils import get_db_connection
from ddl_generator import DDLGenerator
from fixture_loader import FixtureLoader

class RuntimeRunner:
    """
    Executes transpiled PL/pgSQL procedures and captures runtime information,
    including PostgreSQL notices.
    Also handles schema setup and fixture loading.
    """
    def __init__(self):
        self.conn = None
        self.ddl_generator = DDLGenerator()
        self.fixture_loader = FixtureLoader()

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
        Creates tables in the database based on the provided Master Files.
        """
        if not self.conn:
            with self:
                self._setup_schema_internal(master_files)
        else:
            self._setup_schema_internal(master_files)

    def _setup_schema_internal(self, master_files):
        with self.conn.cursor() as cursor:
            for mf in master_files:
                ddl = self.ddl_generator.generate(mf)
                cursor.execute(ddl)
        self.conn.commit()

    def load_fixtures(self, fixtures_config):
        """
        Populates tables with test data.
        fixtures_config is a list of dicts: [{'table_name': '...', 'filepath': '...'}]
        """
        if not self.conn:
            with self:
                self._load_fixtures_internal(fixtures_config)
        else:
            self._load_fixtures_internal(fixtures_config)

    def _load_fixtures_internal(self, fixtures_config):
        with self.conn.cursor() as cursor:
            for config in fixtures_config:
                table_name = config['table_name']
                filepath = config['filepath']
                if filepath.endswith('.json'):
                    self.fixture_loader.load_json(table_name, filepath, cursor=cursor)
                elif filepath.endswith('.csv'):
                    self.fixture_loader.load_csv(table_name, filepath, cursor=cursor)
        self.conn.commit()

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

        return notices
