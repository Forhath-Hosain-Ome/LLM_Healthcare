from django.db import models

class LOINCCodeModel(models.Model):
    code_id = models.CharField(primary_key=True, max_length=255)
    loinc_code = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.loinc_code