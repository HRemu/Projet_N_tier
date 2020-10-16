-- Warning : DO NOT RUN THIS if the database already has entries

USE stageetudiant;


INSERT INTO GRADYEAR(label) VALUES
	('CITISE1'), ('CITISE2'), ('FISE1'), ('FISE2'), ('FISE3');


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


INSERT INTO CITY(city_name, country_id) VALUES
    ('WASHINGTON', 1), ('LAS VEGAS', 1), ('VANCOUVER', 2),
    ('FRANKFURT', 3), ('PALERMO', 4), ('SEOUL', 5);