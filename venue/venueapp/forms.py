from django.forms import ModelForm
from .models import *


class AddEventForm(ModelForm):
    
    class Meta:
        model = Event
        fields = '__all__'
