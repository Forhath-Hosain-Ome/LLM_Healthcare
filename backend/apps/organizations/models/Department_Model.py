from django.db import models
from .Organization_Model import OrganizationModel

class DepartmentModel(models.Model):
    department_id = models.CharField(primary_key=True)
    org_id = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True, related_name='dep')
    department_name = models.CharField()
    type = models.CharField()