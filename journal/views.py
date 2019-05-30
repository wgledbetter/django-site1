from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# The difference between each journal page is really just the json it pulls the data from.
# I should be able to use the same html template for everything

def test(request):
    return render(request, 'journal/index.html')

#-------------------------------------------------------------------------------
def index(request):
    # What would be useful to go in here?
        # Journal posts closest to your current location?
    #return HttpResponse('Journal Index')
    return render(request, 'journal/index.html')

#-------------------------------------------------------------------------------
def food(request):
    return HttpResponse('Food Journal Index')