from django.shortcuts import render
from .models import Zoon_Profile
from members.models import ZoonList,Members,Office
from .models import Members,ZoonList,Office


def Dhaka(request):
    diction={
        'title':'dhaka',
        'zoon_text':'This is Dhaka Zoon page',
    }
    return render(request, 'zoon/Dhaka.html', context=diction)

def DhakaMember(request):
    member_ctg = Members.objects.filter(city__icontains='dhaka')
    diction={
        'title':'Dhaka',
        'zoon_text':'This is Dhaka Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/dhaka/dhaka_mem.html', context=diction)




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

def ComillaMember(request):
    member_ctg = Members.objects.filter(city__icontains='comilla')
    diction={
        'title':'Comilla',
        'zoon_text':'This is Comilla Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/comila/com_mem.html', context=diction)


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

def SylletMember(request):
    member_ctg = Members.objects.filter(city__icontains='Syllet')
    diction={
        'title':'Syllet',
        'zoon_text':'This is Syllet Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/syllet/syllet_mem.html', context=diction)


def Moymonshing(request):
    diction={
        'title':'Moymonshing',
        'zoon_text':'This is Moymonshing Zoon page',
    }
    return render(request, 'zoon/moymonshin.html', context=diction)


def MoymonshinMember(request):
    member_ctg = Members.objects.filter(city__icontains='moymonshing')
    diction={
        'title':'Moymonshing',
        'zoon_text':'This is Moymonshing Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/mymoshing/moym_mem.html', context=diction)





def Power_Plant(request):
    diction={
        'title':'power-Plant',
        'zoon_text':'This is Power Plant Zoon page',
    }
    return render(request, 'zoon/Power_plant.html', context=diction)


def Power_plantMember(request):
    member_ctg = Members.objects.filter(city__icontains='Power plant')
    diction={
        'title':'Power-plant',
        'zoon_text':'This is Power Zo Plant zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/power_plnt/pow_plnt_mem.html', context=diction)