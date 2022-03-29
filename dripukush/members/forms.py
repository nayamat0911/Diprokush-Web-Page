from dataclasses import field
from django import forms
from django.forms import fields 
from members import models
from members.models import ZoonList,Office


class MembersForm(forms.ModelForm):
    class Meta:
        model=models.Members
        # fields = ['first_name','last_name','post','office_address',]
        exclude=["payment",]

# class officeForm(forms.ModelForm):
#     class Meta:
#         model=models.Office
#         exclude=['zoon_list',]

class ZoneForm(forms.ModelForm):
    class Meta:
        model=models.ZoonList
        fields="__all__"