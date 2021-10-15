from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join , name="join"), #name join 은 그냥 안해도 됨
    path('login/', views.login , name="login"), #name join 은 그냥 안해도 됨
    path('logout/', views.logout , name="logout"), #name join 은 그냥 안해도 됨
    path('', views.home, name="home")
]
