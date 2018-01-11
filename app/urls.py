from django.urls import path

from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('leisure', views.leisure, name='leisure'),
    path('educational', views.educational, name='educational'),
    path('professional', views.professional, name='professional'),
    path('personal', views.personal, name='personal'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('create', views.EventCreate.as_view(), name='event-add')
]
