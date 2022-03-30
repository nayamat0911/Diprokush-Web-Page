from django.shortcuts import render
# models
from .models import PaymentInfo
from members.models import Members

# forms
from payment import forms


# Create your views here.
def PaymentSetp_1(request):
    form = forms.PaymentForm_1()
    dict_pay={
        'title':"payment",
        'text':"Payment Your Dues",
        'step1':'Setp 1',
        'step2':'Setp 2',
        'step3':'Setp 3',
        'step4':'Setp 4',
        'form_pay':form

    }
    return render (request, 'pay/pay_step_1.html', context=dict_pay)


def PaymentSetp_2(request):
    form = forms.PaymentForm_2()
    dict_pay={
        'title':"payment",
        'text':"Payment Your Dues",
        'step1':'Setp 1',
        'step2':'Setp 2',
        'step3':'Setp 3',
        'step4':'Setp 4',
        'form_pay':form

    }
    return render (request, 'pay/pay_step_2.html', context=dict_pay)


def PaymentSetp_3(request):
    form = forms.PaymentForm_3()
    dict_pay={
        'title':"payment",
        'text':"Payment Your Dues",
        'step1':'Setp 1',
        'step2':'Setp 2',
        'step3':'Setp 3',
        'step4':'Setp 4',
        'form_pay':form

    }
    return render (request, 'pay/pay_step_3.html', context=dict_pay)

def PaymentSetp_4(request):
    # form = forms.PaymentForm_3()
    dict_pay={
        'title':"payment",
        'text':"Payment Your Dues",
        'step1':'Setp 1',
        'step2':'Setp 2',
        'step3':'Setp 3',
        'step4':'Setp 4',
        'form_pay':'Wating For next Part'

    }
    return render (request, 'pay/pay_step_4.html', context=dict_pay)