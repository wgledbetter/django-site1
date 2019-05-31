from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'page': 'base',
    }
    return render(request, 'base/index.html', context)