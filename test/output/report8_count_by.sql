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
            SELECT DEPARTMENT, COUNT(EMP_ID) FROM EMPLOYEE
            GROUP BY DEPARTMENT
            ORDER BY DEPARTMENT ASC;
            v_next_block := 'EXIT';
            WHEN 'EXIT' THEN
                v_next_block := 'DONE';
        END CASE;
    END LOOP;
END;
$$;
