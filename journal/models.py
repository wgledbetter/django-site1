from django.db import models
# from django_mysql import models

from datetime import datetime
import uuid

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        
class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    
class Photo(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    order = models.IntegerField()
    iden = models.CharField(max_length=200)
    def __str__(self):
        return self.iden
    
class Weather(models.Model):
    tempc = models.FloatField()
    condition = models.CharField(max_length=200)
    def __str__(self):
        return self.condition

class Entry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    # audios = models.JSONField()
    date = models.DateTimeField(default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Photo)
    starred = models.BooleanField()
    # tags = models.JSONField()
    text = models.TextField()
    timezone = models.CharField(max_length=200)
    entry_uuid = models.UUIDField(default=uuid.uuid4)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.entry_uuid)