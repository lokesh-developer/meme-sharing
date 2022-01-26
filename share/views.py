from django.shortcuts import render, HttpResponse
# from urls import  path
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def share(request):
    return render(request, 'share.html')

def categories(request):
    return render(request, 'categories.html')
