from django.contrib import admin
from django.urls import path , include
from . import views
from .views import register

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
]
