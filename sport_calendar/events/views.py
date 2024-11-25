from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def events(request):
    events = Event.objects.order_by('date')
    return render(request, 'events.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Save the object to the database
            return redirect('events')  # Redirect to another view
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()  # Save the updated object to the database
            return redirect('events')  # Redirect to another view
    else:
        form = EventForm(instance=event)

    return render(request, 'add_event.html', {'form': form, 'event': event})