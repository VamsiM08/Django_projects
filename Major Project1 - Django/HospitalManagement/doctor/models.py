from django.db import models

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    consultation_fee = models.IntegerField()

    def __str__(self):
        return self.doctor_name
