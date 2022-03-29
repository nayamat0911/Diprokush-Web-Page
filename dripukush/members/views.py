from django import forms
from django.shortcuts import redirect, render



# Create your views here.
def member_page(request):
    diction={
        'title':'members',
        'text':'This is member page'
    }
    return render(request, 'member_sec/member_page.html', context=diction)

# members form
from members import forms

def member_form(request):
    form =forms.MembersForm()
    zone_form =forms.ZoneForm()
    # office_form =forms.officeForm()
    if request.method == 'POST':
        form=forms.MembersForm(request.POST, request.FILES)
        zone_form=forms.ZoneForm(request.POST)
        # office_form=forms.officeForm(request.POST)
        if form.is_valid() and zone_form.is_valid():
            form.save(commit=True)
            zone_form.save(commit=True)
            # office_form.save(commit=True)
            return redirect('members_app:members_list')

    diction={
        'title':'members form',
        'member_title':'Add Member',
        'member_add_form':form,
        'zone_form':zone_form,
        # 'office_form':office_form,
    }
    return render(request, 'member_sec/members_form.html', context=diction)

from .models import Members,ZoonList,Office

def members_list(request):
    office = Office.objects.order_by('zoon_list')
    member = Members.objects.order_by('first_name')

    diction={
        'title':'Member list',
        'member_title':'All Member List',

        'member_office':office,
        'member_show_list':member
    }
    return render(request, 'member_sec/show_member_list.html', context=diction)

def members_info(request,member_id):
    member_info_pky = Members.objects.get(pk=member_id)
    # zoon_info_pky = ZoonList.objects.get(pk=member_id)

    diction={
        'title':'Member info',
        'member_info__':'Member Information',
        'member_show_info':member_info_pky,
        # 'zoon_show_info':zoon_info_pky
    }
    return render(request, 'member_sec/member_info.html', context=diction)



#=================member add process=============
def How_to_add(request):
    diction={
        'title':'How to add',
        'text':'Member Add Process'
    }
    return render(request, 'member_sec/How_to_add.html', context=diction)

