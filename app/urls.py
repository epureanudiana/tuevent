from django.urls import path
from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth.views import login

from . import views
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from app.views import *



from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('leisure', views.leisure, name='leisure'),
    path('educational', views.educational, name='educational'),
    path('professional', views.professional, name='professional'),
    path('personal', views.personal, name='personal'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('create', views.EventCreate.as_view(), name='event-add'),
    path('home', views.index, name='home'),
    path('map', views.map, name='map'),
    #path('register', views.register, name='register'),
    #path('register/success/', views.register_success, name='register_success'),
    #path('login', views.login, name='login'), #!!!neeeds to be defined in the views - missing so far

    ##path('logout', views.logout_page, name='logout_page'),
    ##url(r'^login/',login, name='login'),

    #url(r'^login/$',views.login , name='login'),
    ##url(r'^register/$', register, name='register'),
    ##url(r'^register/success/$', register_success, name='register_success'),
    ##url(r'^accounts/login/$',login, name='login'),
    url(r'^logout$', logout_page, name='logout_page'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    path('contact', views.contact, name='contact'),
    path('share', views.share, name='share'),
]
