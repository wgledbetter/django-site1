from django.db import migrations

import sqlite3
import uuid

def filljournal(apps, schema_editor):
    print()
    
    db_alias = schema_editor.connection.alias
    
    Journal = apps.get_model("journal", "Journal")
    Location = apps.get_model("journal", "Location")
    Photo = apps.get_model("journal", "Photo")
    Weather = apps.get_model("journal", "Weather")
    Entry = apps.get_model("journal", "Entry")
    
    # Open DayOne db
    conn = sqlite3.connect('invisible/DayOne.sqlite')
    c = conn.cursor()
    
    # Create Journals
    j_pk = []
    for j in c.execute('SELECT * FROM journal'):
        jrnl = Journal()
        jrnl.name = j[7].replace(' ', '_')
        jrnl.save()
        j_pk += [j[0]]


    print(Journal.objects.all().count())
    # Create Locations
    l_pk = []
    for l in c.execute('SELECT * FROM location'):
        loc = Location()
        loc.lat = l[6]
        loc.lon = l[7]
        loc.save()
        l_pk += [l[0]]


    print(Location.objects.all().count())
    nullLoc = Location()
    nullLoc.lat = 696.9
    nullLoc.lon = 696.9
    nullLoc.save()
    l_pk += [-1]
    # Create Weather
    w_pk = []
    for w in c.execute('SELECT * FROM weather'):
        weather = Weather()
        weather.tempc = w[9]
        weather.condition = w[14]
        weather.save()
        w_pk += [w[0]]


    print(Weather.objects.all().count())
    nullWeather = Weather()
    nullWeather.tempc = -280
    nullWeather.condition = 'NULL'
    nullWeather.save()
    w_pk += [-1]
    # Create Entries
    e_pk = []
    for e in c.execute('SELECT * FROM entry'):
        entry = Entry()
        entry.journal = Journal.objects.get(id=j_pk.index(e[4])+1)
        entry.date = e[12]
        try:
            entry.location = Location.objects.get(id=l_pk.index(e[5])+1)
        except:
            entry.location = Location.objects.get(id=l_pk.index(-1)+1)
        entry.starred = (e[3]==1)
        entry.text = e[16]
        entry.timezone = e[20]
        entry.entry_uuid = uuid.UUID(e[17])
        try:
            entry.weather = Weather.objects.get(id=w_pk.index(e[11])+1)
        except:
            entry.weather = Weather.objects.get(id=w_pk.index(-1)+1)
        entry.save()
        e_pk += [e[0]]


    print(Entry.objects.all().count())
    # Create Photos
    for p in c.execute('SELECT * FROM photo'):
        photo = Photo()
        photo.height = p[4]
        photo.width = p[7]
        photo.order = p[6]
        photo.iden = p[19]
        photo.entry = Entry.objects.get(id=e_pk.index(p[8])+1)
        photo.save()


    return


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(filljournal)
    ]
