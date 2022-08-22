from django.db import models
import datetime
# Create your models here.

class UserRegister(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    voterid = models.IntegerField()
    dob = models.DateTimeField(default=datetime.datetime.now, blank=True)
    my_image = models.ImageField(upload_to='User')