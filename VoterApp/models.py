from django.db import models
from django.db.models.deletion import CASCADE
from Dashboard.models import*
from Accounts.models import *
# Create your models here.

class Vote(models.Model):
    candidate_id = models.ForeignKey(CandidateRegister, on_delete=CASCADE)
    userid = models.ForeignKey(VoterRegister, on_delete=CASCADE)
    count = models.CharField(max_length=20)