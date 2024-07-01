from django.db import models

# Create your models here.



class Employee (models.Model):
    employeeid      = models.CharField(max_length=100) 
    employeename    = models.CharField(max_length=50)
    employeesurname = models.CharField(max_length=50)
    email           = models.CharField(max_length=50)
    phone           = models.CharField(max_length=50)