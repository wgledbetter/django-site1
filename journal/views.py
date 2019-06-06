from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# import bytes

from .models import Journal, Entry

import uuid

# Create your views here.

# The difference between each journal page is really just the json it pulls the data from.
# I should be able to use the same html template for everything

def all(request):
    
    # file = open('./static/journal/WebTest.json')
    # entries = json.loads(file.read())

    entries = Entry.objects.all().order_by('date')
    pag = Paginator(entries, 25)
    
    context = {
        'page': 'journal',
        'jname': 'All',
        'entry_enum': enumerate(entries),
    }
    
    return render(request, 'journal/journal.html', context)

#-------------------------------------------------------------------------------
def index(request):
    # What would be useful to go in here?
        # Journal posts closest to your current location?

    journals = Journal.objects.all()
    nentries = [Entry.objects.all().count()]
    for j in journals:
        nentries += [Entry.objects.filter(journal__name__iexact=j.name).count()]
    
    context = {
        'page': 'journal',
        'journal_enum': enumerate(journals),
        'num_entries': nentries,
    }
    
    return render(request, 'journal/index.html', context)

#------------------------------------------------------------------------
def journal(request, jname):

    # Pull all entries for this journal
    # Probably just access a journal model object
    # If DNE, have default
    entries = Entry.objects.filter(journal__name__iexact=jname).order_by('date')
    nPerPage = 15
    pag = Paginator(entries, nPerPage)
    try:
        pageNum = int(request.GET.get('page'))
    except:
        pageNum = 1
        
    pageEntries = pag.get_page(pageNum)

    context = {
        'page': 'journal',
        'jname': jname.capitalize(),
        'entries': pageEntries,
        'firstEntryID': (pageNum-1)*nPerPage + 1
    }

    return render(request, 'journal/journal.html', context)
    
#-------------------------------------------------------------------------------
def year(request, year):

    # Pull entries for this year
    entries = Entry.objects.filter(date__year__exact=year).order_by('date')
    
    context = {
        'page': 'journal',
        'year': year,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)

#-------------------------------------------------------------------------------
def year_month(request, year, month):
    
    # Pull entries for this month and year
    entries = Entry.objects.filter(date__year__exact=year).filter(date__month__exact=month).order_by('date')

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
    entries = Entry.objects.filter(date__year__exact=year).filter(date__month__exact=month).filter(date__day__exact=day).order_by('date')

    context = {
        'page': 'journal',
        'year': year,
        'month': month,
        'day': day,
        'entries': entries,
    }

    return render(request, 'journal/journal.html', context)
    
#-------------------------------------------------------------------------------
def entry(request, euuid):
    
    e = Entry.objects.filter(entry_uuid__exact=euuid)
    
    # Need to do text parsing to identify photos and insert them
    # Also line breaks, probably
    
    context = {
        'page': 'journal',
        'entry': e[0],
        'text': e[0].text
    }
    
    return render(request, 'journal/entry.html', context)