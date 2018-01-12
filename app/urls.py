from django.urls import path
from django.conf.urls import url, include

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
    path('welcome', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('register/success', views.register_success, name='register_success'),
    #path('accounts/login', views.login, name='login'), #!!!neeeds to be defined in the views - missing so far
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout_page, name='logout_page'),


    #url(r'^register/$', register, name='register'),
    #url(r'^register/success/$', register_success, name='register_success'),
    #url(r'^accounts/login/$',login, name='login'),
    #url(r'^logout/$', logout_page, name='logout_page'),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    path('contact', views.contact, name='contact')
]
