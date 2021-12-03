from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('',views.index , name="index"),
    path('login',views.loginForm , name="login"),
    path('Register',views.Register , name="Register"),
    path('logout',views.LogoutUser , name="logout"),
    

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pages/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html'), name='password_reset_complete'),      


]