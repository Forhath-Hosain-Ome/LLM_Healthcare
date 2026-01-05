from django.db import models
from .Cohort_model import CohortModel

class CohortDefinitionModel(models.Model):
    definition_id = models.CharField(primary_key=True, max_length=255)
    cohort_id = models.ForeignKey(CohortModel, on_delete=models.CASCADE)
    filter_criteria = models.CharField(max_length=100)
    filter_value = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cohort_id} created by {self.operator}'
    
