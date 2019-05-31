from django.shortcuts import render

# Create your views here

def index(request):
    
    context = {
        'page': 'effection',
    }
    
    return render(request, 'effection/index.html', context)