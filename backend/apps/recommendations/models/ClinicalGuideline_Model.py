from django.db import models

class ClinicalGuidelineModel(models.Model):
    guideline_id = models.CharField(primary_key=True, max_length=255)
    guideline_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    url = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.guideline_name