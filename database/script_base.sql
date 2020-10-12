CREATE DATABASE stageetudiant;

USE stageetudiant;


CREATE TABLE GRADYEAR(
   gradyear_id INT AUTO_INCREMENT NOT NULL,
   label VARCHAR(20) NOT NULL,
   PRIMARY KEY ( gradyear_id )
);


CREATE TABLE STUDENT(
   student_id INT AUTO_INCREMENT NOT NULL,
   fname VARCHAR(50) NOT NULL,
   lname VARCHAR(50) NOT NULL,
   gradyear_id INT NOT NULL,
   PRIMARY KEY( student_id ),
   FOREIGN KEY ( gradyear_id ) REFERENCES GRADYEAR( gradyear_id )
);


CREATE TABLE COUNTRY(
   country_id INT AUTO_INCREMENT NOT NULL,
   country_name VARCHAR(50) NOT NULL,
   PRIMARY KEY( country_id )
);


CREATE TABLE CITY(
   city_id INT AUTO_INCREMENT NOT NULL,
   city_name VARCHAR(50) NOT NULL,
   country_id INT NOT NULL,
   PRIMARY KEY ( city_id ),
   FOREIGN KEY ( country_id ) REFERENCES COUNTRY( country_id )
);


CREATE TABLE INTERNSHIP(
   internship_id INT AUTO_INCREMENT NOT NULL,
   student_id INT NOT NULL,
   city_id INT NOT NULL,
   start_date DATE NOT NULL,
   end_date DATE,
   PRIMARY KEY ( internship_id ),
   FOREIGN KEY ( student_id ) REFERENCES STUDENT( student_id ),
   FOREIGN KEY ( city_id ) REFERENCES CITY( city_id )
);


