from django.db import models

# Create your models here.
class PatientLab(models.Model):
    id_number = models.CharField(max_length=200, unique=True)
    patient_name = models.CharField(max_length=200)
    phone_mobile = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    date_of_test = models.CharField(max_length=200)
    lab_number = models.CharField(max_length=200)
    clinic_code = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    ref_range = models.CharField(max_length=200)
    finding = models.CharField(max_length=200)
    result_state = models.CharField(max_length=200)