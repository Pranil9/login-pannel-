from django.db import models

# Create your models here.

class Patient(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=25)
    contact = models.IntegerField()
    address = models.CharField(max_length=400)
    reference = models.CharField(max_length=300)

    class Meta:
        db_table = "ptable"


class Appointment(models.Model):
    pname = models.CharField(max_length=25)
    contact = models.IntegerField()
    address = models.CharField(max_length=400)
    reference = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table= "appointment_table"

