from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pages.forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from django.contrib.auth.models import User
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
                                request.session['username'] = username
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
                        UserInfo.objects.create(user = user)
                        messages.success(request, 'Merci pour votre inscription!')
                        return redirect('login')
                else:
                        print(form.errors)
        else:
                form = UserForm()

       
        return render(request,"pages/Register.html" , { 'form' : form })

def LogoutUser(request):
        logout(request)
        return redirect('index')


@login_required
def profil(request, user_id):
	#if request.method == 'POST':
		#user_obj = User.objects.get(id=user_id)
		#user_profile_obj = UserInfo.objects.get(id=user_id)
		#user_profile_obj.save()
		#user_profile_obj.refresh_from_db()
		#return render(request, 'user_profil/profil.html', {'my_profile': user_profile_obj})
	if (request.user.is_authenticated and request.user.id == user_id):
		user_obj = User.objects.get(id=user_id)
		#user_profile = UserInfo.objects.get(id=user_id)
		return render(request, "user_profil/profil.html",{'my_profile': user_obj})


@login_required
def editprofil(request, id):
    	#if request.method == 'POST':
		#user_obj = User.objects.get(id=user_id)
		#user_profile_obj = UserInfo.objects.get(id=user_id)
		#user_profile_obj.save()
		#user_profile_obj.refresh_from_db()
		#return render(request, 'user_profil/profil.html', {'my_profile': user_profile_obj})
	if (request.user.is_authenticated and request.user.id == id):
		user_obj = User.objects.get(id=id)
		#user_profile = UserInfo.objects.get(id=user_id)
		return render(request, "user_profil/editprofil.html",{'my_edit_profile': user_obj})