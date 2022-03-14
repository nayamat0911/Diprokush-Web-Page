from session.models import UserProfile
from django.contrib.messages.api import warning
from session import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserModel
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages

#email sending import--------------
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
#for confirm account--------------
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.contrib.auth import get_user_model
UserModel = get_user_model()


#impot for user profile form
from .forms import UserProfileForm



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:home")
                messages.success(request, 'Your have successfully login!', extra_tags='alert')
            else:
                messages.error(request, "invalaid user or password")
        else:
            messages.error(request, "invalaid user or password")
    else:
        form=AuthenticationForm()

    diction={
        'title':'Login',
        'user_login':'User Login',
        'user_form':form
    }
    return render(request, 'session/user_login.html', context=diction)


def user_logout(request):
    logout(request)
    return redirect('user_login')
    messages.success(request, 'Your have successfully logout!', extra_tags='alert')

from .forms import SignUpForm
def user_signup(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            mail_subject="Activate your account "
            messages=render_to_string('session/confirm_account.html',{
                'user':user,
                'domain':current_site.domain, 
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject, messages,to=[send_mail])
            email.send()
            # messages.info(request,'Successfully created an account you can login Now!')
            # messages.info(request,'Activated your account')
            return redirect('user_login')
            
 
    else:
        form=SignUpForm()


    diction={
        'title':'sign-up',
        'user_signup':"Sign Up form",
        'signup_form':form
    }
    return render(request, 'session/user_signup.html', context=diction)

def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Your account is activated, now you can login")
        return redirect('user_login')
    else:
        messages.warning(request,"activation link is Invalid")
        return redirect('user_signup')

def changed_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request,"Password Changed Successfully changed")
            return redirect("user_login")
    else:
        form=PasswordChangeForm(user=request.user)
    diction={
        "title":'Changed Password',
        "Changed_password":" Changed Your Password",
        "changed_pass":form
    }
    return render(request,'session/changed_password.html', context=diction)



#user profile funcion
def userProfile(request):
    try:
        instance=UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance=None
    if request.method == "POST":
        if instance:
            form=UserProfileForm(request.POST, request.FILES,instance=instance)
        else:
            form=UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'Successfully saved your profile')
            return redirect('home:home')
    else:
        form=UserProfileForm()
    diction={
        'title':'User Profile ',
        'user_profile_title':'Create Your Prfile',
        'user_profile_form':form
    }
    return render(request,'session/user_profile_create.html', context=diction)

    