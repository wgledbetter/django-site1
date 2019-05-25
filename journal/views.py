from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Journal Index')

#-------------------------------------------------------------------------------
def food(request):
    return HttpResponse('Food Journal Index')