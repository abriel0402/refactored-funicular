from django.shortcuts import render
from django.http import HttpResponse
from .models import Event




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