from django.db import models
from apps.patients.models.Patient_Model import PatientModel

class CohortModel(models.Model):
    cohort_id = models.CharField(primary_key=True, max_length=255)
    cohort_name = models.CharField(max_length=100)
    created_by_user_id = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.cohort_name} created by {self.created_by_user_id}'
    
