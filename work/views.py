from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'page': 'work',
    }

    return render(request, 'work/index.html', context)