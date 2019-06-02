from django.shortcuts import render

import astro

# Create your views here

def index(request):
    
    context = {
        'page': 'astro',
        'cpp_string': astro.bindfunction(4),
    }
    
    return render(request, 'astro/index.html', context)