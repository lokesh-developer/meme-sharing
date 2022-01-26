from django.shortcuts import render, HttpResponse
# from urls import  path
def index(request):
    return HttpResponse(request, 'index.html')

def about(request):
    return HttpResponse(request, 'about.html')

def explore(request):
    return render(request, 'explore.html')

def categories(request):
    return render(request, 'categories.html')
