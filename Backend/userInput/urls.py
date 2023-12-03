from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('process/', views.process, name="process"),
    path('integrate_spotify/<str:username>/<str:mood>/',
         views.integrate_spotify, name='integrate_spotify'),
    path('mood/',
         views.mood_caluclate, name='integrate_spotify'),
]
