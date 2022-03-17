from django.shortcuts import render

# Create your views here.

def commitee(request):
    dection_com={
        'title':'Commitee',
        'text': 'This is commitee page' 
    }
    return render(request, 'commitee/commitee_main.html', context=dection_com)