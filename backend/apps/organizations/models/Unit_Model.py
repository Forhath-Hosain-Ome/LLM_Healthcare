from django.db import models
from .Department_Model import DepartmentModel

class UnitModel(models.Model):
    unit_id = models.CharField(primary_key=True)
    department_id = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL, null=True, related_name='unit')
    unit_name = models.CharField()
    unit_type = models.CharField()
    bed_count = models.IntegerField()
    