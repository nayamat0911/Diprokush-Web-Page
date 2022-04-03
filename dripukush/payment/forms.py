from dataclasses import fields
from pyexpat import model
from django import forms
from .models import PaymentInfo, PaymentInfo_2,PaymentInfo_3

class PaymentForm_1(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ['name','post']

class PaymentForm_2(forms.ModelForm):
    class Meta:
        model = PaymentInfo_2
        fields = ['dipu_id','ideb_id',]

class PaymentForm_3(forms.ModelForm):
    class Meta:
        model = PaymentInfo_3
        fields = ['office_address','email', 'mobile']