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
    
    return render(request, 'journal/journal.html', context)

#-------------------------------------------------------------------------------
def index(request):
    # What would be useful to go in here?
        # Journal posts closest to your current location?
    
    context = {
        'page': 'journal',
        'journals': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    }
    
    return render(request, 'journal/index.html', context)

#-------------------------------------------------------------------------------
def year(request, year):

    # Pull entries for this year
    entries = 0
    
    context = {
        'page': 'journal',
        'year': year,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)

#-------------------------------------------------------------------------------
def year_month(request, year, month):
    
    # Pull entries for this month and year
    entries = 0

    context = {
        'page': 'journal',
        'year': year,
        'month': month,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)

#-------------------------------------------------------------------------------
def year_month_day(request, year, month, day):

    # Pull entries for this day
    entries = 0

    context = {
        'page': 'journal',
        'year': year,
        'month': month,
        'day': day,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)

#------------------------------------------------------------------------
def journal(request, jname):

    # Pull all entries for this journal
    # Probably just access a journal model object?
    entries = 0

    context = {
        'page': 'journal',
        'jname': jname,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)