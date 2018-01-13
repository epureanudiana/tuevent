from django.contrib import admin
from .models import User, Event, ContactMessage
# Register your models here.
admin.site.register(Event)
admin.site.register(ContactMessage)
