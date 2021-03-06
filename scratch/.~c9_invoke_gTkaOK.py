from django.db import migrations

import sqlite3
import uuid

def filljournal(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    
    Journal = apps.get_model("journal", "Journal")
    Location = apps.get_model("journal", "Location")
    Photo = apps.get_model("journal", "Photo")
    Weather = apps.get_modal("journal", "Weather")
    Entry = apps.get_modal("journal", "Entry")
    
    # Open DayOne db
    conn = sqlite3.connect('../../private/DayOne.sqlite')
    c = conn.cursor()
    
    # Create Journals
    j_pk = []
    for j in c.execute('SELECT * FROM journal'):
        jrnl = Journal()
        jrnl.name = j[7]
        jrnl.save()
        j_pk += j[0]


    # Create Locations
    l_pk = []
    for l in c.execute('SELECT * FROM location'):
        loc = Location()
        loc.lat = l[6]
        loc.lon = l[7]
        l_pk += [l[0]]


    # Create Weather
    w_pk = []
    for w in c.execute('SELECT * FROM weather'):
        weather = Weather()
        weather.tempc = w[9]
        weather.condition = w[14]
        w_pk += [w[0]]


    # Create Entries
    e_pk = []
    for e in c.execute('SELECT * FROM entry'):
        entry = Entry()
        entry.journal = j_pk.index(e[4])+1
        entry.date = e[12]
        entry.location = l_pk.index(e[5])+1
        entry.starred = (e[3]==1)
        entry.text = e[16]
        entry.timezone = e[20]
        entry.entry_uuid = uuid.UUID(e[17])
        entry.weather = w_pk.index(e[11])+1
        e_pk += [e[0]]


    # Create Photos
    for p in c.execute('SELECT * FROM photo'):
        photo = Photo()
        photo.height = p[4]
        photo.width = p[7]
        photo.order = p[6]
        photo.iden = p[19]
        photo.entry = e_pk.index(p[8])+1


    return


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(filljournal)
    ]
