from django.contrib import admin
from django.urls import path
from share import views

urlpatterns = [
    path('', views.index, name='home'),
]
