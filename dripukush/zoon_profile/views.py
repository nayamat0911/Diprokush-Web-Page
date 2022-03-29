from django.shortcuts import render
from .models import Zoon_Profile
from members.models import ZoonList,Members,Office
from .models import Members,ZoonList,Office

def Chittagong(request):
    diction={
        'title':'chittagong',
        'zoon_text':'This is Chitagong Zoon page',
    }
    return render(request, 'zoon/chittagong.html', context=diction)

def ChittagongMember(request):
    member_ctg = Members.objects.filter(city__icontains='chittagong')
    diction={
        'title':'chittagong',
        'zoon_text':'This is Chitagong Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/ctg/ctg_mem.html', context=diction)


def Cumilla(request):
    member_com = Members.objects.filter(city__contains='comilla')
    diction={
        'title':'cumilla',
        'zoon_text':'This is Cumilla Zoon page',
         'show_list':member_com,
    }
    return render(request, 'zoon/cumilla.html', context=diction)

def Syllet(request):
    # zone = Members.objects.order_by('')
    member = Members.objects.filter(city__contains='syllet')
    diction={
        'title':'syllet',
        'zoon_text':'This is syllet Zoon page',
        # 'show_list':zone,
        'show_list':member,
    }
    return render(request, 'zoon/syllet.html', context=diction)
    