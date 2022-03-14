from django.shortcuts import render
from .models import Home
# Create your views here.
def basic(request):
    diction={
        'title':'home',
        
    }
    return render(request, 'basic.html', context=diction)
def home(request):
    home_profile = Home.objects.get()
    diction={
        'title':'home',
        'text':'This is home page',
        'profile_data': home_profile
    }
    return render(request, 'Home/home_page.html', context=diction)