-- Make sure you First Loaded the Original Prices from Product_Orig_Price
-- The Prices Increases between 20% to 25% per year If Unit Price < Cost Price Else Prices Increases between 5% to 9%
-- The Costs Increases between 5% to 9% per year
-- These Prices/Costs are super unrealistic

-- Create a Procedure to Insert Prices into Product_Prices
CREATE OR REPLACE PROCEDURE Load_product_prices(
    startDate DATE,
    numYears INT
)
IS
    counter INT := 1;
    counter_two INT := 1;
    dt DATE := startDate;
BEGIN
    FOR i IN 1..numYears LOOP
        FOR j IN 1..1850 LOOP
            INSERT INTO product_prices (
                product_id,
                pricing_date,
                product_name,
                product_unit_price,
                product_cost_price
            )
            SELECT
                p.product_id,
                ADD_MONTHS(dt, 12 * i) AS pricing_date,
                p.product_name,
                ROUND(
                    CASE
                        WHEN p.product_unit_price < p.product_cost_price THEN
                            p.product_unit_price * (1.2 + DBMS_RANDOM.VALUE * 0.05)
                        ELSE
                            p.product_unit_price * (1.05 + DBMS_RANDOM.VALUE * 0.05)
                    END, 2
                ) AS product_unit_price,
                ROUND(p.product_cost_price * (1.05 + DBMS_RANDOM.VALUE * 0.05), 2) AS product_cost_price
            FROM
                product_prices p
            WHERE
                p.pricing_date = dt AND p.product_id = counter_two;

            counter_two := counter_two + 1;

            EXIT WHEN counter_two > 1850; -- 1850 is number of unique products
        END LOOP;

        dt := ADD_MONTHS(dt, 12); -- Increment by 1 year
        counter_two := 1; -- Reset the product_id for the next year
    END LOOP;
END Load_product_prices;
/


-- Example: Load_product_prices('01-JAN-([The year you want] - 1)', 1 [Must be done 1 year at a time]);
-- So, if you want 2011 You need to put '01-JAN-2010'
EXEC Load_product_prices('01-JAN-2010', 1);
EXEC Load_product_prices('01-JAN-2011', 1);
EXEC Load_product_prices('01-JAN-2012', 1);
EXEC Load_product_prices('01-JAN-2013', 1);
EXEC Load_product_prices('01-JAN-2014', 1);
