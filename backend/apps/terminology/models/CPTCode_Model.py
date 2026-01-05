from django.db import models

class CPTCodeModel(models.Model):
    code_id = models.CharField(primary_key=True, max_length=255)
    cpt_code = models.CharField(max_length=100)
    procedure_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.cpt_code