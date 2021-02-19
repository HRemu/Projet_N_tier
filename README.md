# Projet N-tiers

### Authors

@ArnaudGuibert and @HRemu  


### Summary

This project aims at creating a fullstack application designed to manage students and their internships.  
It was built using Django and MySQL, and only runs on the development server for now.  


### Setting up the technical environment

* MySQL CLI
~~~~sql
CREATE DATABASE stageetudiant;
~~~~

* Command Prompt (in {...}/Django/mysite/)
~~~~
python manage.py makemigrations mysite
python manage.py migrate mysite
python manage.py loaddata mysite.json
python manage.py migrate
~~~~


### Running the application once set up

* Command Prompt (in {...}/Django/mysite/)
~~~~
python manage.py runserver
~~~~
_(then follow the instructions on the cmd)_

