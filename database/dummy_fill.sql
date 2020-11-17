-- Erasing entries then re-writing them!
USE stageetudiant;


-- DELETE complete
DELETE FROM INTERNSHIP;
DELETE FROM STUDENT;
DELETE FROM GRADYEAR;
DELETE FROM CITY;
DELETE FROM COUNTRY;


-- RESET auto-increment counter
ALTER TABLE STUDENT AUTO_INCREMENT = 1;
ALTER TABLE GRADYEAR AUTO_INCREMENT = 1;
ALTER TABLE COUNTRY AUTO_INCREMENT = 1;
ALTER TABLE CITY AUTO_INCREMENT = 1;
ALTER TABLE INTERNSHIP AUTO_INCREMENT = 1;


-- INSERT complete
INSERT INTO GRADYEAR(label) VALUES
    ('2010'), ('2011'), ('2012'), ('2013'), ('2014');


INSERT INTO STUDENT(lname, fname, gradyear_id) VALUES
    ('DUCK', 'DEWEY', 1),
    ('DUCK', 'HUEY',  1),
    ('DUCK', 'LOUIE', 2),
    ('BUCKET', 'CHARLIE', 3),
    ('HAMMER', 'CHARLIE', 3),
    ('GIOVANNA', 'GIORNO', 4),
    ('BRANDO', 'DIO', 5),
    ('BIG BAD', 'WOLF', 5);


INSERT INTO COUNTRY(country_name) VALUES
    ('USA'), ('CANADA'), ('GERMANY'), ('ITALY'), ('SOUTH KOREA');


INSERT INTO CITY(city_name, longitude, latitude, country_id) VALUES
    ('WASHINGTON', -77.03637, 38.89511, 1),
    ('LAS VEGAS', -115.13722, 36.17497, 1),
    ('VANCOUVER', -123.11934, 49.24966, 2),
    ('FRANKFURT', 8.68417, 50.11552, 3),
    ('PALERMO', 13.33561, 38.13205, 4),
    ('SEOUL', 126.9784, 37.566, 5);


INSERT INTO INTERNSHIP(student_id, city_id, date_start, date_end) VALUES
    (4, 6, '2018-06-04', '2018-08-16'),
    (7, 4, '2018-06-01', '2018-07-01'),
    (7, 4, '2019-06-03', '2018-08-02'),
    (7, 3, '2019-09-04', '2020-02-21');



