import pytest
from emitter import PostgresEmitter

def test_emitter_basic_render():
    emitter = PostgresEmitter()
    output = emitter.render('base.sql.j2', procedure_name='test_proc', procedure_body='RAISE NOTICE \'Hello\';')

    assert 'CREATE OR REPLACE PROCEDURE test_proc()' in output
    assert 'RAISE NOTICE \'Hello\';' in output
    assert 'END;' in output

def test_emit_procedure():
    emitter = PostgresEmitter()
    output = emitter.emit_procedure('my_procedure', 'SELECT 1;')

    assert 'CREATE OR REPLACE PROCEDURE my_procedure()' in output
    assert '    SELECT 1;' in output  # Testing indentation
