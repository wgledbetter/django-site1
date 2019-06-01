from django.shortcuts import render
from django.http import HttpResponse

from .models import Journal, Entry

# Create your views here.

# The difference between each journal page is really just the json it pulls the data from.
# I should be able to use the same html template for everything

def all(request):
    
    # file = open('./static/journal/WebTest.json')
    # entries = json.loads(file.read())

    entries = Entry.objects.all().order_by('date')
    
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

    context = {
        'page': 'journal',
        'jname': jname.capitalize(),
        'entry_enum': enumerate(entries),
    }

    return render(request, 'journal/journal.html', context)
    
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