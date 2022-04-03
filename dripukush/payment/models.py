
from django.db import models
from members.models import Members
# Create your models here.
class PaymentInfo(models.Model):
    payIntro_1=models.ForeignKey(Members, on_delete=models.CASCADE, related_name='payintro_1' ,default='')
    name = models.CharField(max_length=50, blank=False)
    POST_CATAGORY=(
        ('------Select------', '------select------'),
        ('Excutive Engineer','Excutive Engineer'),
        ('Sub-Divisional Engineer','Sub-Divisional Engineer'),
        ('Assistant Engineer','Assistant Engineer'),
        ('Sub-Assistant Engineer','Sub-Assistant Engineer'),
    )
    post = models.CharField(max_length=200, choices=POST_CATAGORY, default='')

    def __str__(self):
        return self.name
    
class PaymentInfo_2(models.Model):
    payIntro_2=models.ForeignKey(PaymentInfo, on_delete=models.CASCADE, related_name='payintro_2', )
    dipu_id = models.CharField(max_length=30 , blank=True)
    ideb_id = models.CharField(max_length=30 , blank=True)
    

    def __str__(self):
        return self.dipu_id

class PaymentInfo_3(models.Model):
    payIntro_3=models.ForeignKey(PaymentInfo_2, on_delete=models.CASCADE, related_name='payintro_3')
    office_address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=17)

    def __str__(self):
        return self.email