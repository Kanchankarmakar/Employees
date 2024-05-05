from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='Unknown')
    department = models.CharField(max_length=100, default='Unknown')
    email = models.EmailField(unique=True)
    dob = models.DateField(default = "2004-02-12")
