from django.db import models
from .Patient_Model import PatientModel

class AllergyModel(models.Model):
    allergy_id = models.CharField(primary_key=True, max_length=255)
    patient_id = models.ForeignKey(PatientModel, on_delete=models.SET_NULL)
    allergen_name = models.CharField(max_length=30)
    reaction_type = models.CharField(max_length=30)
    severity = models.CharField(max_length=30)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.patient_id.first_name} created by {self.severity}'
