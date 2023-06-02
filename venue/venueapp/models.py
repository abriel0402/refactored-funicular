from django.db import models




OPTIONS = {
    (25, '25'),
    (60, '60'),
    (100, '100'),
}

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    soldOut = models.BooleanField()
    seats = 100


    def __str__(self):
        return self.name

class Seat(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()
    booked = models.BooleanField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"Seat row {self.row}, col {self.col} for "
    