from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pages.forms import UserForm
from django.contrib.auth.models import User
from .helpers import send_forget_password_mail
from .models import UserInfo

# Create your views here.

def index(request):
        return render(request,"pages/index.html" )

def loginForm(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username and password:
                        user = authenticate(username=username , password=password)

                        if user is not None:
                                login(request, user)
                                return redirect('index')
                        else:
                                messages.error(request, "L'identifiant ou le mot de passe est incorrect") 
                else:
                        messages.error(request, 'Remplissez tous les champs')


        return render(request,"pages/login.html" )

def Register(request):
        
        if request.method == 'POST':
                form = UserForm(data=request.POST)
                if form.is_valid():
                        user = form.save()
                        user.set_password(user.password)
                        user.save()
                        messages.success(request, 'Merci pour ton inscription!')
                        return redirect('login')
                else:
                        print(form.errors)
        else:
                form = UserForm()

       
        return render(request,"pages/Register.html" , { 'form' : form })

def LogoutUser(request):
        logout(request)
        return redirect('login')



