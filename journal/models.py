from django.db import models

# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=200)

class Entry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    text = models.TextField()