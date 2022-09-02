from django.db import models

# Create your models here.

class VoterRegister(models.Model):
    face_id = models.IntegerField()
    voter_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    date = models.DateField(default='2000-12-02')

    def __str__(self):
        return self.voter_name