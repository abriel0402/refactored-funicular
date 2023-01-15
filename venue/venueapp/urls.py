from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/", views.eventPage, name="event"),
    path("add-event/", views.addEvent, name="addEvent"),
    path("remove-event/", views.removeEvent, name="removeEvent"),
    path("del/<int:event_id>", views.delete, name="delete"),
]