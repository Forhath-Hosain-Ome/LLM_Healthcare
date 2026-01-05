from django.db import models

class PatientModel(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    men = models.CharField(max_length=20)
    ssn_encrypted = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'