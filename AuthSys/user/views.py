from . forms import SingUpForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def user_home(request):
    if request.user.is_authenticated:
        return render(request, 'user/home.html', {'Username' : request.user})    
    return HttpResponseRedirect('/user/login/')

def sign_up(request):
    if request.method == "POST":
        try:
            fm = SingUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "SignUp Successfuly!")
                return HttpResponseRedirect('/user/')
        except Exception as e:
            print(e.__str__())
            return render(request, 'user/signUp.html', {'form':fm})
    else:
        fm = SingUpForm()
    return render(request, 'user/signUp.html', {'form':fm})

def log_in(request):
    fm = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                fm = AuthenticationForm(request=request, data=request.POST)
                if fm.is_valid():
                    username = fm.cleaned_data['username']
                    password = fm.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user:
                        login(request=request, user=user)
                        messages.success(request, "LogIn Successfuly!")
                        return HttpResponseRedirect('/user/')
                    messages.error(request, "Please Enter Correct Credentials")
            except Exception as e:
                print(e.__str__())
                return render(request, 'user/logIn.html', {'form':fm})
        else:
            return render(request, 'user/logIn.html', {'form':fm})
    else:
        return HttpResponseRedirect('/user/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')