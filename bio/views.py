from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'page': 'bio',
    }

    return render(request, 'bio/index.html', context)