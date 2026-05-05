import os
import psycopg2
from contextlib import contextmanager

def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database using environment variables.
    Defaults are provided for local development.
    """
    host = os.getenv("PGHOST", "localhost")
    port = os.getenv("PGPORT", "5432")
    dbname = os.getenv("PGDATABASE", "webfocus_test")
    user = os.getenv("PGUSER", "webfocus")
    password = os.getenv("PGPASSWORD", "password")

    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    return conn

@contextmanager
def db_cursor():
    """
    Context manager for database cursor.
    Ensures connection is closed after use.
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
