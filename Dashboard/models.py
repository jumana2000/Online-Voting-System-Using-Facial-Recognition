from django.db import models

# Create your models here.

class CandidateRegister(models.Model):
    candidate_id = models.IntegerField()
    candidate_name = models.CharField(max_length=20)
    party_name = models.CharField(max_length=20)
    member_support = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.TextField(max_length=50)
    candidate_photo = models.ImageField(upload_to='candidate_photo')
    party_logo = models.ImageField(upload_to='party_logo')
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.candidate_name



