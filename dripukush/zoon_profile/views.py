from django.shortcuts import render
from .models import Zoon_Profile


def Chittagong(request):
    zoon_data = Zoon_Profile.objects.get()
    diction={
        'title':'chittagong',
        'zoon_text':'This is Chitagong Zoon page',
        'pro_data': zoon_data
    }
    return render(request, 'zoon/chittagong.html', context=diction)

def Cumilla(request):
    diction={
        'title':'cumilla',
        'zoon_text':'This is Cumilla Zoon page',
        # 'profile_data': 
    }
    return render(request, 'zoon/cumilla.html', context=diction)

def Syllet(request):
    diction={
        'title':'syllet',
        'zoon_text':'This is syllet Zoon page',
        # 'profile_data': 
    }
    return render(request, 'zoon/syllet.html', context=diction)
    