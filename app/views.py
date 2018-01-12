#views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from django.template import RequestContext
from django.shortcuts import render, get_object_or_404

from django.db.models import F
from django.conf import settings
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




# Create your views here.




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

@login_required
def welcome(request):
    #user = request.user
    return render(request, 'app/welcome.html')
    #return render(request,
    #'home.html',
    #{ 'user': request.user }
    #)
