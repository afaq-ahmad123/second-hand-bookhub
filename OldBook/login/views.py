from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.core.mail import send_mail
from .forms import UserForm, LoginForm
#from .models import user as userInfo
from OldBook.settings import *
from django.conf import global_settings

from django.apps import apps
userInfo = apps.get_model('login','user')
from_email =  'kashifsss915@gmail.com'
# Create your views here.
def log(request):
    return render(request,'login/login.html')


def register(request):
    print("in register")
    form = UserForm(request.POST or None)
    login_form = LoginForm()
    if form.is_valid():
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        request.session["email"] = email
        user = userInfo.objects.filter(email=email)
        if user:
            messages.add_message(request, messages.ERROR, 'Already registered')
            return render(request, 'login/login.html', {'form': form ,'loginForm': login_form, 'message':messages})
        # now send and email to user informing about signup
        if password != confirm:
            #raise form.ValidationError("Password not same")
            messages.add_message(request, messages.ERROR, 'Password not same')
            return render(request, 'login/login.html', {'form': form, 'loginForm': login_form, 'message': messages})
        subject = "Welcome to NUCES Cricle"
        form.save()
        return redirect("home-url")
    else:
        messages.add_message(request, messages.ERROR, 'Invalid Data')
        return render(request, 'login/login.html', {'form': form ,'loginForm': login_form, 'message':messages})

def add_user(request):
    user = userInfo(name='Afaq',email='afaqahmadmalik970@gmail.com',password='123456',contact='+923114187882',
                   address='house#8, street#10, Lahore.')
    u=userInfo.objects.filter(email='afaqahmadmalik970@gmail.com')
    if not u:
        request.session["email"] = 'afaqahmadmalik970@gmail.com'
        Success=user.save()
    else:
        Success=0
        print(u)

    if Success:
        print('User Ok', user)
        return redirect("home-url")
    else:
        form = UserForm(request.POST or None)
        login_form = LoginForm()
        return render(request, 'login/login.html', {'form': form ,'loginForm': login_form})

def del_user(request):
    print(userInfo.objects.filter(email='afaqahmadmalik970@gmail.com'))
    Sucess=userInfo.objects.filter(email='afaqahmadmalik970@gmail.com').delete()
    if Sucess:

        return redirect("home-url")
    #userInfo.objects.get(email='afaqahmadmalik970@gmail.com').delete()
    else :
        form = UserForm(request.POST or None)
        login_form = LoginForm()
        return render(request, 'login/login.html', {'form': form, 'loginForm': login_form})
def login_user(request):
    print("in login user")
    form = UserForm()
    login_form = LoginForm(request.POST or None)
    if not request.POST.get('email') or not request.POST.get('password'):
        print("not Valid")
        return render(request, 'login/login.html', {'form': form, 'loginForm': login_form})
    if login_form.authenticate_data(request.POST.get('email'), request.POST.get('password')):
        print("valid")
        email = request.POST.get("email")
        request.session["email"] = email
        return redirect("home-url")
    else:

        print("not Valid")
        return render(request, 'login/login.html', {'form': form, 'loginForm': login_form})


def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('login_user')


#
# @login_required
# def password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was updated successfully!')  # <-
#             return redirect('settings:password')
#         else:
#             messages.warning(request, 'Please correct the error below.')  # <-
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'profiles/change_password.html', {'form': form})