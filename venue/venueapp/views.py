from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Seat
from .forms import AddEventForm


events = Event.objects.all()


    
            


# Create your views here.
def index(request):
    return render(request, "venueapp/index.html", {
        "events": Event.objects.all(),
    })

def eventPage(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, "venueapp/event.html", {
        "event": event,
    })

def addEvent(request):
    form = AddEventForm()
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
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

