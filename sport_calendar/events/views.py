from django.shortcuts import render
from .models import Event

# Create your views here.

def home(request):
    return render(request, 'home.html')

def events(request):
    events = Event.objects.order_by('date')
    return render(request, 'events.html', {'events': events})