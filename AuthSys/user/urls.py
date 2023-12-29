from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='UserHome'),
    path('login/', views.log_in, name='LogIn'),
    path('signup/', views.sign_up, name='SignUp'),
    path('logout/', views.log_out, name='LogOut'),
    path('changePass/', views.change_pass, name='ChangePassword'),
]
