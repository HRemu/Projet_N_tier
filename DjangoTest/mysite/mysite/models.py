from django.db import models

# Create your models here.

class Gradyear(models.Model):
   gradyear_id  = models.AutoField(primary_key=True) 
   label =models.CharField(max_length=20, null = False)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True) 
    fname = models.CharField(max_length=50, null = False)
    lname =models.CharField(max_length=50, null = False) 
    gradyear_id =models.ForeignKey(Gradyear, on_delete=models.CASCADE)

class Country(models.Model):
    country_id = models.AutoField(primary_key= True)
    country_name =models.CharField(max_length=50, null = False) 


class City(models.Model):
    city_id =models.AutoField(primary_key= True)
    city_name = models.CharField(max_length=50, null = False)
    longitude = models.CharField(max_length=10, null = False)
    latitude =  models.CharField(max_length=10, null = False)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)


class Internship:
    internship_id =models.AutoField(primary_key= True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

