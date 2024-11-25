from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'events/?$', views.events, name='events'),
    re_path(r'add/?$', views.add_event, name='add_event'),
    #re_path(r'event/<int:id>/?$', views, name='event_detail'),
]
