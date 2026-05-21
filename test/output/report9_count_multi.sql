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
            SELECT COUNT(LAST_NAME), COUNT(DEPARTMENT), COUNT(JOBCODE) FROM EMPLOYEE;
            v_next_block := 'EXIT';
            WHEN 'EXIT' THEN
                v_next_block := 'DONE';
        END CASE;
    END LOOP;
END;
$$;
