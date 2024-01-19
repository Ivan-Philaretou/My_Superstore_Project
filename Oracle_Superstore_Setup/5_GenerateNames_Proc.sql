-- Create a Procedure to Insert Unique Customer Names
CREATE OR REPLACE PROCEDURE InsertCustomers AS
    v_fullName VARCHAR2(100);
    v_rowCount NUMBER;

BEGIN
    -- Call the Oracle-specific function to generate names
    v_fullName := GenerateNames('test');

    -- Check if the full_name already exists
    SELECT COUNT(*) INTO v_rowCount FROM customers WHERE full_name = v_fullName;

    IF v_rowCount = 1 THEN
        -- If the full_name already exists, do nothing (you can add logic as needed)
        NULL;
    ELSE
        -- Insert the new customer
        INSERT INTO customers (first_name, last_name, full_name)
        VALUES (
            SUBSTR(v_fullName, 1, INSTR(v_fullName, ' ') - 1),
            TRIM(SUBSTR(v_fullName, INSTR(v_fullName, ' '))),
            v_fullName
        );
    END IF;
END InsertCustomers;
/

-- Create a Procedure to Generate/Populate Customers Table with 10,000 Customer Names 
CREATE OR REPLACE PROCEDURE LoadCustomers(Amount INT) AS
    counter INT := 1;
    customer_count INT;

BEGIN
    -- Initialize customer_count outside the loop
    SELECT COUNT(DISTINCT customer_id) INTO customer_count FROM customers;

    -- Use customer_count in the loop condition
    WHILE customer_count < 10000 LOOP
        IF counter <= Amount THEN
            -- Call the InsertCustomers procedure 
            InsertCustomers;
            counter := counter + 1;

            -- Update customer_count inside the loop
            SELECT COUNT(DISTINCT customer_id) INTO customer_count FROM customers;
        ELSE
            EXIT;
        END IF; 
    END LOOP;
END LoadCustomers;
/

-- Call the Procedure to Load/Generate Customer Names
BEGIN
    LoadCustomers(20000);
END;
/
