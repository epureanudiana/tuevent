#views.py
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.csrf import csrf_protect

from app.forms import *
from .forms import PostEvent
from .forms import ContactForm, FilterByForm, OrderByForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.db.models import F
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.models import User, Group
# Imports for the Contact page
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponseRedirect
from django.http import HttpResponse


from .models import Event, ContactMessage


class EventList(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def index(request):

    events=Event.objects.all()
    return render_to_response('app/index.html', {"events": events})

def leisure(request):
    form_class = OrderByForm
    latest_event_list = Event.objects.filter(event_category='le')
    latest_event_list = latest_event_list.order_by('-event_date')

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            order = request.POST.get('orderby', '')
            latest_event_list = order_events(order, latest_event_list)
            form.fields['orderby'].value = order
            form_class = form

    context = {'latest_event_list': latest_event_list[:50],
        'category': 'Leisure',
        'css': 'app/leisure.css',
        'js': 'app/javascript/leisure.js',
        'orderbyform': form_class}
    return render(request, 'app/events-base.html', context)

def personal(request):
    form_class = OrderByForm
    latest_event_list = Event.objects.filter(event_category='pe')
    latest_event_list = latest_event_list.order_by('-event_date')

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            order = request.POST.get('orderby', '')
            latest_event_list = order_events(order, latest_event_list)
            form.fields['orderby'].value = order
            form_class = form

    context = {'latest_event_list': latest_event_list[:50],
        'category': 'Personal',
        'css': 'app/personal.css',
        'js': 'app/javascript/personal.js',
        'orderbyform': form_class}
    return render(request, 'app/events-base.html', context)

def educational(request):
    form_class = OrderByForm
    latest_event_list = Event.objects.filter(event_category='ed')
    latest_event_list = latest_event_list.order_by('-event_date')

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            order = request.POST.get('orderby', '')
            latest_event_list = order_events(order, latest_event_list)
            form.fields['orderby'].value = order
            form_class = form

    context = {'latest_event_list': latest_event_list[:50],
        'category': 'Educational',
        'css': 'app/educational.css',
        'js': 'app/javascript/educational.js',
        'orderbyform': form_class}
    return render(request, 'app/events-base.html', context)

def professional(request):
    form_class = OrderByForm
    latest_event_list = Event.objects.filter(event_category='pr')
    latest_event_list = latest_event_list.order_by('-event_date')

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            order = request.POST.get('orderby', '')
            latest_event_list = order_events(order, latest_event_list)
            form.fields['orderby'].value = order
            form_class = form

    context = {'latest_event_list': latest_event_list[:50],
        'category': 'Professional',
        'css': 'app/professional.css',
        'js': 'app/javascript/professional.js',
        'orderbyform': form_class}
    return render(request, 'app/events-base.html', context)

def myprofile(request):
    user =   request.user
    #user = get_object_or_404(User, pk=request.user.id)
    my_event_list = Event.objects.filter(published_by = user).order_by('-event_date')
    #my_event_list = Event.objects.filter(event_category='le')
    form_class = FilterByForm
    form_class1 = OrderByForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        form1 = form_class1(data=request.POST)

        if form.is_valid():
            filterr = request.POST.get('filterby', '')
            my_event_list = filter_events(filterr, my_event_list)
            form.fields['filterby'].value = filterr
            form_class = form

        if form1.is_valid():
            order = request.POST.get('orderby', '')
            my_event_list = order_events(order, my_event_list)
            form1.fields['orderby'].value = order
            form_class1 = form1

    context = {'my_event_list': my_event_list[:30], 'user': user,
    'filterbyform': form_class, 'orderbyform': form_class1}
    return render(request, 'app/myprofile.html', context)

def order_events(order, events):
    if (order == 'up'):
        events = events.order_by('-event_date')
    elif (order == 'fu'):
        events = events.order_by('event_date')
    elif (order == 'po'):
        events = events.order_by('-event_name') #TODO POPOLARITY
    return events

def filter_events(filterr, events):
    if (filterr == 'le'):
        events = events.filter(event_category='le')
    elif (filterr == 'pe'):
        events = events.filter(event_category='pe')
    elif (filterr == 'ed'):
        events = events.filter(event_category='ed')
    elif (filterr == 'pr'):
        events = events.filter(event_category='pr')
    return events

def map(request):
    events=Event.objects.all()
    return render_to_response('app/map.html', {"events": events})

#def showZoneDetail(request, zone_id):
#    zone=Zone.objects.get(id=zone_id)
#    return render_to_response('zonendetail.html', {"zone": zone})


def contact(request):
    form_class = ContactForm
    success = False

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            success = True
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            m = ContactMessage()
            m.sender_name = contact_name
            m.sender_email = contact_email
            m.content = form_content
            m.save()

    return render(request, 'app/contact.html', {'form': form_class, 'success': success})




class EventCreate(CreateView):
    model = Event
    fields = ['event_name', 'event_location', 'event_date', 'event_description', 'event_category']

    def form_valid(self, form):
         user = self.request.user
         form.instance.published_by = user
         return super(EventCreate, self).form_valid(form)



# Create your views here.
@login_required
def share2(request):
    if request.method == "POST":
        form = PostEvent(request.POST)
        if form.is_valid():
            event = form.save(commit = False)
            event.published_by = request.user
            event.save()
            return redirect('app:share3')
    else:
        form = PostEvent()
    return render(request, 'app/share2.html', {'form': form})

@login_required
def share3(request):
    return render(request, 'app/share3.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
        variables = {
        'form': form
    }

    return render( request,
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render( request,
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

#@login_required
#def welcome(request):
    #user = request.user
#    return render(request, 'app/welcome.html')
    #return render(request,
    #'home.html',
    #{ 'user': request.user }
    #)

@login_required
def index(request):
    #return render(request,
    #'app/index.html',

    #)
    events=Event.objects.all()
    return render_to_response('app/index.html', {"events": events}, { 'user': request.user })
