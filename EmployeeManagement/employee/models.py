from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.FloatField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

