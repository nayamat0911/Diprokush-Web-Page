from cProfile import label
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from session.models import New_User
from django.forms import fields, widgets

class SignUpForm(forms.ModelForm):
    class Meta:
        model=New_User
        fields=('name','email','password1','password2'  )
        labels = {'name':'Your Name:', 'email':'Enter Email:', 'password1':'Password', 'password2':'Confirm Password'}
        widgets = {'password1':forms.PasswordInput, 'password2':forms.PasswordInput}

#user profile form
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=UserProfile
        exclude=('user',)