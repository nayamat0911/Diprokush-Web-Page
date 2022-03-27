
from distutils.command.upload import upload
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class ZoonList(models.Model):
    zoon_name = models.CharField(max_length=50)

    def __str__(self):
        return self.zoon_name
        
class Office(models.Model):
    zoon_list = models.ForeignKey(ZoonList, on_delete=models.CASCADE, default=False)
    office_name = models.CharField(max_length=100)

    def __str__(self):
        return self.office_name

    
class Members(models.Model):
    employee_info = models.ForeignKey(Office, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='member/member_img' ,blank=True)
    office_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.first_name + ' '+ self.last_name)
