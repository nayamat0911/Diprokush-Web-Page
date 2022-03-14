from django import forms
from django.forms import fields 
from members import models

class MembersForm(forms.ModelForm):
    class Meta:
        model=models.Members
        fields="__all__"