from rest_framework import serializers
#from rest_framework import Event
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_location', 'event_category', 'event_description')
