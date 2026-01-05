from django.db import models

class ICD10CodeModel(models.Model):
    code_id = models.CharField(max_length=255, primary_key=True)
    icd10_code = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.icd10_code