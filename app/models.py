from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    department = models.CharField(max_length=255)
    employee_status = models.CharField(max_length=255, choices=['Remote Location', 'Contract Employee', 'Full-Time'])

    def __str__(self):
        return self.name
