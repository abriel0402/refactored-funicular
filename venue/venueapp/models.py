from django.db import models





# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    soldOut = models.BooleanField()


    def __str__(self):
        return self.name

class Seat(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()
    booked = models.BooleanField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"Seat row {self.row}, col {self.col} for "
    