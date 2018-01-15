from django.contrib import admin
from .models import User, Event, ContactMessage, XattendsY
# Register your models here.
admin.site.register(Event)
admin.site.register(ContactMessage)
admin.site.register(XattendsY)
