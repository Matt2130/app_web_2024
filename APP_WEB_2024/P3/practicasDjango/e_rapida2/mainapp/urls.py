from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='index'),
    path('', views.index, name='inicio'),
    path('acercade/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
]