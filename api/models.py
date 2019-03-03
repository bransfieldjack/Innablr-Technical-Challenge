from django.db import models

class Api(models.Model):
    version = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    lastcommitsha = models.CharField(max_length=50)
