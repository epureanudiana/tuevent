#views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from app.forms import *
from .forms import PostEvent
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render, get_object_or_404

from django.db.models import F
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth.models import User, Group
# Imports for the Contact page
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

# Create your views here.
from .models import Event, ContactMessage


class EventList(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def index(request):
    return render(request, 'app/index.html')

def leisure(request):
    latest_event_list = Event.objects.filter(event_category='le')
    latest_event_list = latest_event_list.order_by('-event_date')[:50]
    context = {'latest_event_list': latest_event_list,
        'category': 'Leisure',
        'css': 'app/leisure.css',
        'js': 'app/javascript/leisure.js'}
    return render(request, 'app/events-base.html', context)

def personal(request):
    latest_event_list = Event.objects.filter(event_category='pe')
    latest_event_list = latest_event_list.order_by('-event_date')[:50]
    context = {'latest_event_list': latest_event_list,
        'category': 'Personal',
        'css': 'app/personal.css',
        'js': 'app/javascript/personal.js'}
    return render(request, 'app/events-base.html', context)

def educational(request):
    latest_event_list = Event.objects.filter(event_category='ed')
    latest_event_list = latest_event_list.order_by('-event_date')[:50]
    context = {'latest_event_list': latest_event_list,
        'category': 'Educational',
        'css': 'app/educational.css',
        'js': 'app/javascript/educational.js'}
    return render(request, 'app/events-base.html', context)

def professional(request):
    latest_event_list = Event.objects.filter(event_category='pr')
    latest_event_list = latest_event_list.order_by('-event_date')[:50]
    context = {'latest_event_list': latest_event_list,
        'category': 'Professional',
        'css': 'app/professional.css',
        'js': 'app/javascript/professional.js'}
    return render(request, 'app/events-base.html', context)

def myprofile(request):
    user =   request.user
    #user = get_object_or_404(User, pk=request.user.id)
    my_event_list = Event.objects.filter(published_by = user).order_by('-event_date')[:30]
    #above_5 = Count('event', filter=Q(book__rating__gt=5))
    #my_event_list =  Event.objects.filter(event_category='pr')
    #context = {'my_event_list': my_event_list}


    #my_event_list = Event.objects.filter(event_category='le')

    context = {'my_event_list': my_event_list}
    return render(request, 'app/myprofile.html', context, { 'user': request.user })






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
    return render(request,
    'app/index.html',
    { 'user': request.user }
    )
