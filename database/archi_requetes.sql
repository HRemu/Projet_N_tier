-- Script for architecture of SQL queries on base (not tested)



-- SELECT queries


-- Recherche par promo {promo}
SELECT s.fname, s.lname, g.label
FROM STUDENT s JOIN GRADYEAR g ON s.gradyear_id = g.gradyear_id
WHERE (g.label LIKE promo);

-- Requete par ville {city}
SELECT s.fname, s.lname, i.date_start, i.date_end
FROM CITY c JOIN INTERNSHIP i ON c.city_id = i.city_id
JOIN STUDENT s ON i.student_id = s.student_id
WHERE (c.city_name LIKE city);

-- Recherche par nom {prenom, nom}
SELECT s.fname, s.lname, g.label
FROM STUDENT s JOIN GRADYEAR g ON s.gradyear_id = g.gradyear_id
WHERE (s.fname LIKE '%'+prenom+'%' AND s.lname LIKE '%'+nom+'%');

-- Idem avec les stages
SELECT s.fname, s.lname, i.date_start, i.date_end, c.city_name, co.country_name
FROM STUDENT s LEFT JOIN INTERNSHIP i ON s.student_id = i.student_id
JOIN CITY c ON i.city_id = c.city_id JOIN COUNTRY co ON c.country_id = co.country_id
WHERE (s.fname LIKE '%'+prenom+'%' AND s.lname LIKE '%'+nom+'%');



-- INSERT queries


-- Ajouter un etudiant {fname, lname, gradyear_id}
INSERT INTO STUDENT (fname, lname, gradyear_id) VALUES (fname, lname, gradyear_id);

-- Ajouter un pays {name}
INSERT INTO COUNTRY (name) VALUES (name);

-- Ajouter une ville {country_id, name, longitude, latitude}
INSERT INTO CITY (country_id, city_name, longitude, latitude) VALUES (country_id, name, longitude, latitude);

-- Ajouter un stage {student_id, city_id, date_start, date_end}
INSERT INTO INTERNSHIP (student_id, city_id, date_start, date_end) VALUES (student_id, city_id, date_start, date_end);



-- UPDATE queries


-- Changer un etudiant {student_id, nom, prenom}
UPDATE STUDENT s SET s.fname = prenom, s.lname = nom WHERE s.student_id = student_id;

-- Changer une ville {city_id, city_name, longitude, latitude}
UPDATE CITY c SET c.city_name = city_name, c.longitude = longitude, c.latitude = latitude WHERE c.city_id = city_id;

-- Changer un stage {internship_id, city_id, date_start, date_end}
UPDATE INTERNSHIP i SET i.date_start = date_start, i.date_end = date_end, i.city_id = city_id
WHERE i.internship_id = internship_id;



-- DELETE queries


-- Supprimer un stage {internship_id}
DELETE FROM INTERNSHIP WHERE internship_id = internship_id;

