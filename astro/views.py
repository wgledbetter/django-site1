from django.shortcuts import render

from astro import astrocpp

# Create your views here

def index(request):
    
    context = {
        'page': 'astro',
        'cpp_out': astrocpp.bindfunction(4),
    }
    
    return render(request, 'astro/index.html', context)