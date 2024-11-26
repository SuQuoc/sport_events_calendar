from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Event
from .forms import EventForm, SportForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def events(request):
    query = request.GET.get('query')
    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) |
            Q(fkey_home_team__name__icontains=query) |
            Q(fkey_away_team__name__icontains=query)
        ).order_by('date', 'time')
    else:
        events = Event.objects.order_by('date', 'time')
    return render(request, 'events.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('events')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm(instance=event)

    return render(request, 'add_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('events')


def add_model(request, model_name):

    form_classes = {
        'sport': SportForm,
    }

    form_class = form_classes.get(model_name.lower())
    if not form_class:
        raise ValueError('Invalid model')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = form_class()

    return render(request, 'add_model.html', {'form': form, 'model_name': model_name})
