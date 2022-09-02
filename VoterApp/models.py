from django.db import models

# Create your models here.

class Vote(models.Model):
    candidate_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    count = models.CharField(max_length=20)