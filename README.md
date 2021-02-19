# Projet N-tiers

### Authors

@ArnaudGuibert and @HRemu  


### Summary

This project aims at creating a fullstack application designed to manage students and their internships.  
It was built using Django and MySQL, and only runs on the development server for now.  


### Setting up the technical environment

~~~~sql
mysql> CREATE DATABASE stageetudiant;
~~~~

```cmd
C:/Users/{...}/Django/mysite> python manage.py makemigrations mysite
C:/Users/{...}/Django/mysite> python manage.py migrate mysite
C:/Users/{...}/Django/mysite> python manage.py loaddata mysite.json
C:/Users/{...}/Django/mysite> python manage.py migrate
```


### Running the application once set up

```cmd
C:/Users/{...}/Django/mysite> python manage.py runserver
```
_(then follow the instructions on the cmd)_

