-- Create a Procedure to Insert Orders into initial_orders
CREATE OR REPLACE PROCEDURE Create_orders(
    order_year DATE
)
IS
    counter_two NUMBER := 1;
    d_t DATE := order_year;
    ROWCOUNT NUMBER := 0;
BEGIN
    FOR j IN 1..450 LOOP
        SELECT MAX(ORDER_ID) INTO ROWCOUNT FROM initial_orders;

        INSERT INTO initial_orders (
            order_date,
            ship_mode,
            ship_date,
            customer_id,
            postal_id,
            product_id,
            product_price_id,
            product_cost_price,
            product_unit_price,
            product_discount_percentage,
            product_discount_amount,
            product_discounted_unit_price,
            quantity,
            total_discount_amount,
            total_unit_amount,
            gross_profit_unit_amount,
            total_discounted_unit_amount,
            gross_profit_discounted_unit_amount
        )
        WITH
            DISCOUNT AS (
                SELECT ROUND(DBMS_RANDOM.VALUE * 0.02, 2) AS product_discount_percentage FROM dual
            ),
            SHIP_MD AS (
                SELECT TRUNC(DBMS_RANDOM.VALUE * 3 + 1) AS ship_mode_id FROM dual
            ),
            CUSTOMER AS (
                SELECT TRUNC(DBMS_RANDOM.VALUE * 10000 + 1) AS customer_id FROM dual
            ),
            ORDER_DT AS (
                SELECT fulldate FROM calendars WHERE fulldate = d_t
            ),
            SHIP_INFO AS (
                SELECT
                    dt.fulldate AS order_date,
                    c.customer_id,
                    ca.postal_id,
                    s.ship_mode,
                    CASE
                        WHEN s.ship_mode = 'First Class' THEN dt.fulldate + 1
                        WHEN s.ship_mode = 'Second Class' THEN dt.fulldate + 3
                        WHEN s.ship_mode = 'Standard Class' THEN dt.fulldate + 7               
                    END AS ship_date
                FROM ORDER_DT dt
                CROSS JOIN SHIP_MD sm
                CROSS JOIN CUSTOMER c
                CROSS JOIN customer_address ca
                CROSS JOIN ship_modes s
                WHERE c.customer_id = ca.customer_id AND s.ship_mode_id = sm.ship_mode_id
            ),
            PRODUCT AS (
                SELECT
                    p.product_id,
                    p.product_price_id,
                    p.product_unit_price,
                    p.product_cost_price,
                    TRUNC(DBMS_RANDOM.VALUE * 10 + 1) AS quantity
                FROM product_prices p
                JOIN ORDER_DT c ON TO_CHAR(p.pricing_date, 'YYYY') = TO_CHAR(c.fulldate, 'YYYY')
                WHERE p.product_id = TRUNC(DBMS_RANDOM.VALUE * 1850 + 1)
            ),
            ORDER_INFO AS (
                SELECT
                    p.product_id,
                    p.product_price_id,
                    p.product_unit_price,
                    p.product_cost_price,
                    p.quantity,
                    d.product_discount_percentage,
                    d.product_discount_percentage * p.product_unit_price AS product_discount_amount,
                    (p.product_unit_price * p.quantity * d.product_discount_percentage) AS total_discount_amount,
                    (p.product_unit_price - (p.product_unit_price * d.product_discount_percentage)) AS product_discounted_unit_price,
                    p.product_unit_price * p.quantity AS total_unit_amount,
                    ((p.product_unit_price - p.product_cost_price) * p.quantity) AS gross_profit_unit_amount,
                    ((p.product_unit_price * p.quantity) - (p.product_unit_price * p.quantity * d.product_discount_percentage)) AS total_discounted_unit_amount,
                    (((p.product_unit_price - (p.product_unit_price * d.product_discount_percentage)) - p.product_cost_price) * p.quantity) AS gross_profit_discounted_unit_amount
                FROM PRODUCT p
                CROSS JOIN DISCOUNT d
            )
        SELECT
            s.order_date AS order_date,
            s.ship_mode AS ship_mode,
            s.ship_date AS ship_date,
            s.customer_id AS customer_id,
            s.postal_id AS postal_id,
            ord.product_id AS product_id,
            ord.product_price_id AS product_price_id,
            ord.product_cost_price AS product_cost_price,
            ord.product_unit_price AS product_unit_price,
            ord.product_discount_percentage AS product_discount_percentage,
            ord.product_discount_amount AS product_discount_amount,
            ord.product_discounted_unit_price AS product_discounted_unit_price,
            ord.quantity AS quantity,
            ord.total_discount_amount AS total_discount_amount,
            ord.total_unit_amount AS total_unit_amount,
            ord.gross_profit_unit_amount AS gross_profit_unit_amount,
            ord.total_discounted_unit_amount AS total_discounted_unit_amount,
            ord.gross_profit_discounted_unit_amount AS gross_profit_discounted_unit_amount
        FROM SHIP_INFO s
        CROSS JOIN ORDER_INFO ord;

        counter_two := counter_two + 1;

        EXIT WHEN counter_two > 450;
    END LOOP;
END;
/

-- Create Procedure to Insert Orders per Day into Orders Table
CREATE OR REPLACE PROCEDURE Load_orders(
    order_year DATE,
    day_count INT
)
IS
    counter INT := 1;
    d_t DATE := order_year;
BEGIN
    FOR i IN 1..day_count LOOP
        -- Call the Create_orders procedure
        Create_orders(d_t);

        -- Increment counters and date for the next iteration
        counter := counter + 1;
        d_t := d_t + 1; -- Increment by one day
    END LOOP;
END;
/

-- Replace the date with your desired start date assuming you calendars/product_prices table has the dates.
BEGIN
--    Load_orders(DATE '2010-01-01', 365); -- done
--    Load_orders(DATE '2011-01-01', 365); -- done
--    Load_orders(DATE '2012-01-01', 366); -- done
--    Load_orders(DATE '2013-01-01', 365); -- done
--    Load_orders(DATE '2014-01-01', 365); -- done
--    Load_orders(DATE '2015-01-01', 365); -- done
END;
/