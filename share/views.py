from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def explore(request):
    return render(request, 'explore.html')

def categories(request):
    return render(request, 'categories.html')
