from django.db import models

class OrganizationModel(models.Model):
    org_id = models.CharField(primary_key=True)
    org_name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    bed_count = models.IntegerField(blank=False, null=False)
    state = models.CharField(max_length=30, blank=False, null=False)
    npi_number = models.CharField()