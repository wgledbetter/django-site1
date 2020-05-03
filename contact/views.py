from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'page': 'contact',
    }

    return render(request, 'contact/index.html', context)