from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/", views.eventPage, name="event"),
    path("add-event/", views.addEvent, name="addEvent"),
]