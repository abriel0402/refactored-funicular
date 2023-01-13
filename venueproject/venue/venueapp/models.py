from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    soldOut = models.BooleanField()
    seating = models.CharField(max_length=60)

    def __str__(self):
        return self.name