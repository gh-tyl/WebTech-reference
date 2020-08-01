from django.db import models

# Create your models here.
class ReferenceData(models.Model):
    title = models.TextField
    url = models.TextField