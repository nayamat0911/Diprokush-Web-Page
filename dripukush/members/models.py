
from distutils.command.upload import upload
from django.db import models
from django.db.models.deletion import CASCADE
from session.models import UserProfile
# Create your models here.


class ZoonList(models.Model):
    ZONE_NAME=(
        ('--Select--', '--select--'),
        ('Dhaka', 'Dhaka'),
        ('Chittangog', 'Chittangog'),
        ('Cumilla', 'Cumilla'),
        ('Maymoshing', 'Maymoshing'),
        ('Syllet', 'Syllet'),
        ('Power plant', 'Power plant'),
    )
    zoon_name = models.CharField(max_length=200, choices=ZONE_NAME)

    def __str__(self):
        return self.zoon_name
        
class Office(models.Model):
    zoon_list = models.ForeignKey(ZoonList, on_delete=models.CASCADE, default=False)
    office_name = models.CharField(max_length=100)

    def __str__(self):
        return self.office_name

    
class Members(models.Model):
    # employee_info = models.ForeignKey(Office, on_delete=models.CASCADE ,related_name='member_pro')
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    POST_CATAGORY=(
        ('------Select------', '------select------'),
        ('Excutive Engineer','Excutive Engineer'),
        ('Sub-Divisional Engineer','Sub-Divisional Engineer'),
        ('Assistant Engineer','Assistant Engineer'),
        ('Sub-Assistant Engineer','Sub-Assistant Engineer'),
    )
    post = models.CharField(max_length=200, choices=POST_CATAGORY, default='')
    office_address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    dipu_id = models.CharField(max_length=30 , blank=True)
    ideb_id = models.CharField(max_length=30 , blank=True)
    payment = models.IntegerField(default='500', blank=True)
    Bio = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to='member_pic' ,blank=True)

    def __str__(self):
        return str(self.first_name + ' '+ self.last_name)
