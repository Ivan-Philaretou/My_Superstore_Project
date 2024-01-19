-- Create a Function to Generate a Single Random Name
CREATE OR REPLACE FUNCTION GenerateNames(myname VARCHAR2)
RETURN VARCHAR2
DETERMINISTIC
IS
    v_fullName VARCHAR2(100);
BEGIN
    SELECT test1.first_name || ' ' || test2.last_name INTO v_fullName
    FROM (
        SELECT firstname_id, first_name
        FROM first_names
        WHERE firstname_id BETWEEN 1 AND 135
        ORDER BY DBMS_RANDOM.VALUE
        FETCH FIRST 1 ROW ONLY
    ) test1
    CROSS JOIN (
        SELECT lastname_id, last_name
        FROM last_names
        WHERE lastname_id BETWEEN 1 AND 135
        ORDER BY DBMS_RANDOM.VALUE
        FETCH FIRST 1 ROW ONLY
    ) test2;

    RETURN v_fullName;
END;
/

-- Test the Function Works
SELECT GenerateNames('test') AS Generated_Name FROM DUAL;