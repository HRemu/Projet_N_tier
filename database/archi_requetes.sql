-- Script for architecture of SQL queries on base (not tested)


-- SELECT queries

-- Toutes les villes ayant accueilli un stage (de l'histoire)
SELECT co.country, c.city_name, c.longitude, c.latitude
FROM INTERNSHIP i JOIN CITY c ON i.city_id = c.city_id
JOIN COUNTRY co ON c.country_id = co.country_id;

-- Toutes les villes avec un stage autour de la date {date_val}
SELECT co.country, c.city_name, c.longitude, c.latitude
FROM INTERNSHIP i JOIN CITY c ON i.city_id = c.city_id
JOIN COUNTRY co ON co.country_id = c.country_id
WHERE (i.date_start <= date_val AND i.date_end >= date_val);

-- Tous les etudiants appeles {fname, lname}
SELECT i.city_id, i.date_start, i.date_end, s.fname, s.lname, g.label
FROM INTERNSHIP i JOIN STUDENT s ON i.student_id = s.student_id
JOIN GRADYEAR g ON s.gradyear_id = g.gradyear_id
WHERE (s.fname LIKE '%' + fname + '%' AND s.lname LIKE '%' + lname + '%');

-- Tous les etudiants de la promo {gradyear}
SELECT i.city_id, i.date_start, i.date_end, s.fname, s.lname, g.label
FROM INTERNSHIP i JOIN STUDENT s ON i.student_id = s.student_id
JOIN GRADYEAR g ON s.gradyear_id = g.gradyear_id
WHERE g.label LIKE gradyear;


-- INSERT queries

-- Ajouter un nouvel etudiant {fname, lname, gradyear_id}
INSERT INTO STUDENT (fname, lname, gradyear_id)
VALUES (fname, lname, gradyear_id);

-- Ajouter un nouveau pays {name}
INSERT INTO COUNTRY (name) VALUES (name);

-- Ajouter une nouvelle ville {country_id, name, longitude, latitude}
INSERT INTO CITY (country_id, city_name, longitude, latitude)
VALUES (country_id, name, longitude, latitude);

-- Ajouter un stage d'un etudiant {student_id, city_id, date_start, date_end}
INSERT INTO INTERNSHIP (student_id, city_id, date_start, date_end)
VALUES (student_id, city_id, date_start, date_end);



