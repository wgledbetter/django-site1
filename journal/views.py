from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.

# The difference between each journal page is really just the json it pulls the data from.
# I should be able to use the same html template for everything

def test(request):
    
    file = open('./static/journal/WebTest.json')
    entries = json.loads(file.read())
    
    context = {
        'page': 'journal',
        'entries': entries,
    }
    
    return render(request, 'journal/index.html', context)

#-------------------------------------------------------------------------------
def index(request):
    # What would be useful to go in here?
        # Journal posts closest to your current location?
    
    context = {
        'page': 'journal',
    }
    
    return render(request, 'journal/index.html', context)

#-------------------------------------------------------------------------------
def food(request):
    
    context = {
        'page': 'journal',
    }
    
    return HttpResponse('Food Journal Index', context)