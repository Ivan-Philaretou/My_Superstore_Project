-- 1. Create a loop for all customer_ids 1 to 10,000
-- 2. Create a random number between 1 and 632 for postal_id
-- 3. Insert these into the customer_address

-- Create a Procedure to Insert and Link all the Customers to a Random Address
CREATE OR REPLACE PROCEDURE LoadCustomer_Address AS
    counter NUMBER := 1;
BEGIN
    WHILE counter <= 10000 LOOP
        INSERT INTO customer_address (postal_id, customer_id)
        VALUES (
            (SELECT postal_id FROM address WHERE postal_id BETWEEN 1 AND 632 ORDER BY DBMS_RANDOM.VALUE FETCH FIRST 1 ROW ONLY),
            counter
        );
        counter := counter + 1;
    END LOOP;
END LoadCustomer_Address;
/

EXEC LoadCustomer_Address;