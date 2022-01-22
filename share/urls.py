from django.contrib import admin
from django.urls import path
from share import views

urlpatterns = [
    path('', views.index, name='home'),
    path('share', views.share, name='share'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('categories', views.categories, name='categories'),
]
