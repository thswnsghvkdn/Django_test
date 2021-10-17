from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join , name="join"), #name join 은 그냥 안해도 됨
    path('login/', views.login , name="login"), #name join 은 그냥 안해도 됨
    path('logout/', views.logout , name="logout"), #name join 은 그냥 안해도 됨
    path('write/', views.write , name="write"), #name join 은 그냥 안해도 됨
    path('update/<int:pk>', views.update , name="update"), #name join 은 그냥 안해도 됨
    path('detail/<int:pk>', views.update_image , name="detailImage"), #name join 은 그냥 안해도 됨
    path('delete/<int:pk>', views.delete , name="delete"), #name join 은 그냥 안해도 됨
    path('homeImage/', views.home_image, name="homeImage"),
    path('writeImage/', views.write_image, name="writeImage"),
    path('deleteImage/<int:pk>', views.delete_image , name="deleteImage"), #name join 은 그냥 안해도 됨
    path('', views.home, name="home")
]
