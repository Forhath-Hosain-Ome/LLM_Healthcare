from django.db import models
from .Patient_Model import PatientModel
from apps.terminology.models.ICD10Code_Model import ICD10CodeModel

class ProblemModel(models.Model):
    problem_id = models.CharField(primary_key=True, max_length=255)
    patient_id = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    condition_name = models.CharField(max_length=30)
    icd10_code_id = models.ForeignKey(ICD10CodeModel, on_delete=models.CASCADE)
    onset_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.patient_id.first_name} created by {self.icd10_code_id}'