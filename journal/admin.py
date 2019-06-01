from django.contrib import admin

# Register your models here.
from .models import Journal, Entry, Location, Weather, Photo

admin.site.register(Journal)
admin.site.register(Entry)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(Weather)