from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name} ({self.appointment_date})"
