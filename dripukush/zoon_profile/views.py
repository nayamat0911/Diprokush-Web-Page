from django.shortcuts import render
from .models import Zoon_Profile
from members.models import ZoonList,Members,Office
from .models import Members,ZoonList,Office

#======================dhaka=================
def Dhaka(request):
    diction={
        'title':'dhaka',
        'zoon_text':'Dhaka Zoon page',
    }
    return render(request, 'zoon/Dhaka.html', context=diction)

def DhakaMember(request):
    member_dha = Members.objects.filter(city__icontains='dhaka')
    diction={
        'title':'dhaka-m',
        'zoon_text':'Dhaka Zone Member List',
        'show_list':member_dha,
    }
    return render(request, 'zoon/dhaka/dhaka_mem.html', context=diction)




#======================Chittagong=================
def Chittagong(request):
    diction={
        'title':'ctg',
        'zoon_text':'Chitagong Zoon page',
    }
    return render(request, 'zoon/chittagong.html', context=diction)

def ChittagongMember(request):
    member_ctg = Members.objects.filter(city__icontains='chittagong')
    diction={
        'title':'ctg-m',
        'zoon_text':'Chitagong Zone Member List',
        'show_list':member_ctg,
    }
    return render(request, 'zoon/ctg/ctg_mem.html', context=diction)


#======================Comilla=================
def Cumilla(request):
    member_com = Members.objects.filter(city__contains='comilla')
    diction={
        'title':'cumilla',
        'zoon_text':'Cumilla Zoon page',
         'show_list':member_com,
    }
    return render(request, 'zoon/cumilla.html', context=diction)

def ComillaMember(request):
    member_com = Members.objects.filter(city__icontains='comilla')
    diction={
        'title':'comilla-m',
        'zoon_text':'Comilla Zone Member List',
        'show_list':member_com,
    }
    return render(request, 'zoon/comila/com_mem.html', context=diction)




#======================Syllet=================
def Syllet(request):
    # zone = Members.objects.order_by('')
    member = Members.objects.filter(city__contains='syllet')
    diction={
        'title':'syllet',
        'zoon_text':'syllet Zoon page',
        # 'show_list':zone,
        'show_list':member,
    }
    return render(request, 'zoon/syllet.html', context=diction)

def SylletMember(request):
    member_syl = Members.objects.filter(city__icontains='Syllet')
    diction={
        'title':'syllet-m',
        'zoon_text':'Syllet Zone Member List',
        'show_list':member_syl,
    }
    return render(request, 'zoon/syllet/syllet_mem.html', context=diction)




#======================Moymonshing=================
def Moymonshing(request):
    diction={
        'title':'Moymonshing',
        'zoon_text':'Moymonshing Zoon page',
    }
    return render(request, 'zoon/moymonshin.html', context=diction)


def MoymonshinMember(request):
    member_moy = Members.objects.filter(city__icontains='moymonshing')
    diction={
        'title':'moy-m',
        'zoon_text':'Moymonshing Zone Member List',
        'show_list':member_moy,
    }
    return render(request, 'zoon/mymoshing/moym_mem.html', context=diction)




#======================Power plant=================
def Power_Plant(request):
    diction={
        'title':'power-Plant',
        'zoon_text':'Power Plant Zoon page',
    }
    return render(request, 'zoon/Power_plant.html', context=diction)


def Power_plantMember(request):
    member_powp = Members.objects.filter(city__icontains='Power plant')
    diction={
        'title':'p-p-m',
        'zoon_text':'Power Plant zone Member List',
        'show_list':member_powp,
    }
    return render(request, 'zoon/power_plnt/pow_plnt_mem.html', context=diction)