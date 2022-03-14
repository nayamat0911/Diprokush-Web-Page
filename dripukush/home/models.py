from datetime import date
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to="home/home_img")
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
