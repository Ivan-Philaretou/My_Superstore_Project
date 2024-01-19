-- Create Procedure for Calendar to Insert Dates
CREATE OR REPLACE PROCEDURE InsertCalendar(dt DATE)
AS
BEGIN
    INSERT INTO calendars(
        fulldate,
        day,
        month,
        quarter,
        year
    )
    VALUES(
        dt, 
        EXTRACT(DAY FROM dt),
        EXTRACT(MONTH FROM dt),
        TO_NUMBER(TO_CHAR(dt, 'Q')),
        EXTRACT(YEAR FROM dt)
    );
END InsertCalendar;
/

-- Create Procedure for Calendar to Generate Dates
CREATE OR REPLACE PROCEDURE LoadCalendars(
    startDate DATE, 
    day INT
)
AS
    counter INT := 1;
    dt DATE := startDate;
BEGIN
    WHILE counter <= day LOOP
        InsertCalendar(dt);
        counter := counter + 1;
        dt := dt + 1;
    END LOOP;
END LoadCalendars;
/

-- It works 1 year at a time OR 2191 for days = 6 years
-- Note: Make sure the days amount is correct per year
DECLARE
    v_startDate DATE := TO_DATE('2010-01-01', 'YYYY-MM-DD');
BEGIN
    LoadCalendars(v_startDate, 2191);
END;
/