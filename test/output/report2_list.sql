CREATE OR REPLACE PROCEDURE webfocus_procedure()
LANGUAGE plpgsql
AS $$
DECLARE
    v_next_block TEXT;
BEGIN
    v_next_block := 'ENTRY';
    WHILE v_next_block NOT IN ('EXIT', 'DONE') LOOP
        CASE v_next_block
            WHEN 'ENTRY' THEN
            /* EMPLOYEE */
            SELECT ROW_NUMBER() OVER ( ) AS "LIST", ROW_NUMBER() OVER () AS "LIST", LAST_NAME, FIRST_NAME FROM EMPLOYEE;
            v_next_block := 'EXIT';
            WHEN 'EXIT' THEN
                v_next_block := 'DONE';
        END CASE;
    END LOOP;
END;
$$;