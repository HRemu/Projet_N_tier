-- Creates the database from scratch. Fails if db already exists

CREATE DATABASE IF NOT EXISTS stageetudiant;

USE stageetudiant;


CREATE TABLE IF NOT EXISTS GRADYEAR(
   gradyear_id INT AUTO_INCREMENT NOT NULL,
   label VARCHAR(20) NOT NULL,
   PRIMARY KEY ( gradyear_id )
);


CREATE TABLE IF NOT EXISTS STUDENT(
   student_id INT AUTO_INCREMENT NOT NULL,
   fname VARCHAR(50) NOT NULL,
   lname VARCHAR(50) NOT NULL,
   gradyear_id INT NOT NULL,
   PRIMARY KEY( student_id ),
   FOREIGN KEY ( gradyear_id ) REFERENCES GRADYEAR( gradyear_id )
);


CREATE TABLE IF NOT EXISTS COUNTRY(
   country_id INT AUTO_INCREMENT NOT NULL,
   country_name VARCHAR(50) NOT NULL,
   PRIMARY KEY( country_id )
);


CREATE TABLE IF NOT EXISTS CITY(
   city_id INT AUTO_INCREMENT NOT NULL,
   city_name VARCHAR(50) NOT NULL,
   longitude VARCHAR(10) NOT NULL,
   latitude VARCHAR(10) NOT NULL,
   country_id INT NOT NULL,
   PRIMARY KEY ( city_id ),
   FOREIGN KEY ( country_id ) REFERENCES COUNTRY( country_id )
);


CREATE TABLE IF NOT EXISTS INTERNSHIP(
   internship_id INT AUTO_INCREMENT NOT NULL,
   student_id INT NOT NULL,
   city_id INT NOT NULL,
   date_start DATE,
   date_end DATE,
   PRIMARY KEY ( internship_id ),
   FOREIGN KEY ( student_id ) REFERENCES STUDENT( student_id ),
   FOREIGN KEY ( city_id ) REFERENCES CITY( city_id )
);


