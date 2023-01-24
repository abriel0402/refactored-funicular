from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Seat
from .forms import AddEventForm
import math


events = Event.objects.all()







# Create your views here.
def index(request):
    return render(request, "venueapp/index.html", {
        "events": Event.objects.all(),
    })

def eventPage(request, event_id):

    seatsRow1 = []
    seatsRow2 = []
    seatsRow3 = []
    seatsRow4 = []
    seatsRow5 = []

    rowedSeats = [seatsRow1, seatsRow2, seatsRow3, seatsRow4, seatsRow5]

    event = Event.objects.get(pk=event_id)
    eventSeats = []
    for seat in Seat.objects.all():
        if seat.event.id == event_id:
            eventSeats.append(seat)
    soldOutCheck = True
    for seat in eventSeats:
        if seat.booked == False:
            soldOutCheck = False
    if soldOutCheck == True:
        event.soldOut = True

    for seat in eventSeats:
        if seat.row == 1:
            seatsRow1.append(seat)
        elif seat.row == 2:
            seatsRow2.append(seat)
        elif seat.row == 3:
            seatsRow3.append(seat)
        elif seat.row == 4:
            seatsRow4.append(seat)
        elif seat.row == 5:
            seatsRow5.append(seat)
    
    return render(request, "venueapp/event.html", {
        "event": event,
        "eventSeats": eventSeats,
        "rowedSeats": rowedSeats,

    })

def addEvent(request):
    form = AddEventForm()
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            eventsLen = events.count()
            newEvent = events[eventsLen-1]
            for i in range(5):
                for j in range(5):
                    Seat.objects.create(row=i+1, col=j+1, booked=False, event=newEvent)

    return render(request, 'venueapp/addEvent.html', {
        "form": form,
    })

def delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect("index")

def removeEvent(request):
    return render(request, "venueapp/removeEvent.html", {
        "events": Event.objects.all(),
    })

def seatPage(request, seat_id):
    seat = Seat.objects.get(pk=seat_id)
    return render(request, "venueapp/seat.html", {
        "seat": seat,
        "seat_id": seat.id,
    })

def seatPurchased(request, seat_id, event_id):
    seat = Seat.objects.get(pk=seat_id)
    seat.booked = True
    seat.save()
    return redirect("event", event_id=event_id)