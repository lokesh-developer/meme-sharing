from django.contrib import admin
from django.urls import path
from share import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/about', views.about, name='about'),
    path('/explore', views.explore, name='explore'),
    path('/categories', views.categories, name='categories'),
]
