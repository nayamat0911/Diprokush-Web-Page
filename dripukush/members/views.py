from django import forms
from django.shortcuts import redirect, render

import members

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
    if request.method == 'POST':
        form=forms.MembersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return redirect('members_app:members_list')

    diction={
        'title':'members form',
        'member_title':'Add Member',
        'member_add_form':form
    }
    return render(request, 'member_sec/members_form.html', context=diction)

from .models import Members,ZoonList

def members_list(request):
    member = Members.objects.order_by('first_name')

    diction={
        'title':'Member list',
        'member_title':'All Member List',
        'member_show_list':member
    }
    return render(request, 'member_sec/show_member_list.html', context=diction)

def members_info(request,member_id):
    member_info_pky = Members.objects.get(pk=member_id)
    zoon_info_pky = ZoonList.objects.get(pk=member_id)

    diction={
        'title':'Member info',
        'member_info__':'Member Information',
        'member_show_info':member_info_pky,
        'zoon_show_info':zoon_info_pky
    }
    return render(request, 'member_sec/member_info.html', context=diction)

