from django.db import models

from datetime import datetime

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Entry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())