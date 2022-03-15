from distutils.command.upload import upload
from django.db import models
from members.models import Members, ZoonList, Office

# Create your models here.

class Zoon_Profile(models.Model):
    zoon_name = models.CharField(max_length=100)
    zoon_heading = models.CharField(max_length=300)
    zoon_text = models.CharField(max_length=1000)
    profile_img = models.ImageField(upload_to='zoon/zoon_profile')
    passident_img = models.ImageField(upload_to='zoon/prasident_img')
    secratary_img = models.ImageField(upload_to='zoon/prasident_img')
