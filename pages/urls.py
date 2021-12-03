from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('login',views.loginForm , name="login"),
    path('Register',views.Register , name="Register"),
    path('logout',views.LogoutUser , name="logout"),
    path('profil/<int:user_id>',views.profil , name="profil"),
    path('editprofil',views.editprofil , name="editprofil"),
]