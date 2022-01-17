from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'shareMemes': "Share your memes here!",
    }
    return render(request, 'index.html', context)
