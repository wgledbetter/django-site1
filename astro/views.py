from django.shortcuts import render

# Create your views here

def index(request):
    
    context = {
        'page': 'astro',
    }
    
    return render(request, 'astro/index.html', context)