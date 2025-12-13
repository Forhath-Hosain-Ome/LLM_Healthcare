from django.db import models
from .Unit_Model import UnitModel

class BedModel(models.Model):
    bed_id = models.CharField(primary_key=True)
    unit_id = models.ForeignKey(UnitModel, on_delete=models.SET_NULL, null=True, related_name='bed')
    bed_number = models.CharField()
    status = models.CharField()