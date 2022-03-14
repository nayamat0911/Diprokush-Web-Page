from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICE=(
        ('Male','Male'),
        ('Female','Female'),
    )
    POST_CATAGORY=(
        ('Excutive Engineer','Excutive Engineer'),
        ('Sub-Divisional Engineer','Sub-Divisional Engineer'),
        ('Assistant Engineer','Assistant Engineer'),
        ('Sub-Assistant Engineer','Sub-Assistant Engineer'),
    )
    BLOOD_GROUP=(
        ('A+','A+'),
        ('A-','A-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
    )
    RELIGION=(
        ('Islam','Islam'),
        ('Hindu','Hindu'),
        ('Buddist','Buddist'),
        ('Chisttran','Chisttran'),
        ('Others','Others'),
    )
    NATIONALITY=(
        ("Bangladeshi","Bangladeshi"),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=100, default='Your Father name:')
    mother_name=models.CharField(max_length=100, default='Your Mother name:')
    birth_date=models.DateField()
    post=models.CharField(max_length=150, choices=POST_CATAGORY)
    blood_group=models.CharField(max_length=5, choices=BLOOD_GROUP)
    gender=models.CharField(max_length=30, choices=GENDER_CHOICE)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=17)
    nationality=models.CharField(max_length=30, choices=NATIONALITY)
    religion=models.CharField(max_length=50,choices=RELIGION)
    biodata=models.TextField(max_length=200)
    image=models.ImageField(upload_to='session/profile_image')


    def __str__(self):
        return f'(self.user.username) Profile'
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)