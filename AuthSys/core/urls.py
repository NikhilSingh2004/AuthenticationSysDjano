from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.core_home, name='MainHome'),
]
