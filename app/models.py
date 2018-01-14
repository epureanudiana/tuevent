from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField

# Create your models here.
class Event(models.Model):
    CATEGORIES = (
        ('le', 'Leisure'),
        ('pe', 'Personal'),
        ('ed', 'Educational'),
        ('pr', 'Professional'),
    )
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_location = models.CharField(max_length=250)
    #position = GeopositionField()
    event_date = models.DateTimeField('Date_format: YYYY-MM-DD HH:mm:ss')
    event_description = models.CharField(max_length=300)
    event_category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
    )
    def __str__(self):
        return self.event_name
    def get_absolute_url(self):
        return reverse('app:leisure')

class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=200)
    sender_email = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
