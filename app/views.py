from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
from .models import Event

def index(request):
    return render(request, 'app/index.html')

def leisure(request):
    latest_event_list = Event.objects.order_by('-event_date')[:50]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'app/leisure.html', context)

def educational(request):
    return render(request, 'app/educational.html')

def professional(request):
    return render(request, 'app/professional.html')

def personal(request):
    return render(request, 'app/personal.html')

def myprofile(request):
    return render(request, 'app/myprofile.html')

class EventCreate(CreateView):
    model = Event
    fields = ['published_by', 'event_name', 'event_location', 'event_date', 'event_description']
