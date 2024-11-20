from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"events/?$", views.events, name="event_list"),
    #re_path(r"event/<int:id>/?$", views, name="event_detail"),
]
