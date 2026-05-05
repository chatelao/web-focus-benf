from db_utils import get_db_connection

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
