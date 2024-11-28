from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Event
from .forms import *
from django.apps import apps

MODELS_HTML = 'models'

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
    return render(request, 'add_event.html', {'form': form, 'operation': 'Add'})


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm(instance=event)
    return render(request, 'add_event.html',
                {'form': form,
                 'event': event,
                'operation': 'Edit'
    })


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('events')


def list_models(request, model_name):
    model_class = get_model_by_name('events', model_name)
    
    query = request.GET.get('query')
    if query:
        results = model_class.objects.filter(name__icontains=query).order_by('name')
    else:
        results = model_class.objects.order_by('name')
    return render(request,
                f'{MODELS_HTML}/list_models.html', 
                {
                    'models': results,
                    'model_name': model_name
                }
    )


form_classes = {
        'sport': SportForm,
        'team': TeamForm,
        'venue': VenueForm,
        'country': CountryForm
    }

def add_model(request, model_name):
    form_classes = {
        'sport': SportForm,
        'team': TeamForm,
        'venue': VenueForm,
        'country': CountryForm
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
    return render(request, f'{MODELS_HTML}/add_model.html',
                {
                    'form': form,
                    'model_name': model_name,
                    'operation': 'Add'
    })


def edit_model(request, model_name, model_id):
    model_class = get_model_by_name('events', model_name)
    model = get_object_or_404(model_class, id=model_id)

    form_class = form_classes.get(model_name.lower())
    if not form_class:
        raise ValueError('Invalid model')

    if request.method == 'POST':
        form = form_class(request.POST, instance=model)
        if form.is_valid():
            form.save()
    else:
        form = form_class(instance=model)
    return render(request, f'{MODELS_HTML}/add_model.html',
                {
                    'form': form,
                    'model_name': model_name,
                    'model': model,
                    'operation': 'Edit'
    })


def delete_model(request, model_name, model_id):
    model_class = get_model_by_name('events', model_name)
    event = get_object_or_404(model_class, id=model_id)
    event.delete()
    return redirect(f'{MODELS_HTML}/list_models', model_name=model_name)


def get_model_by_name(app_label, model_name):
    try:
        model = apps.get_model(app_label, model_name)
        return model
    except LookupError:
        raise ValueError(f"Model '{model_name}' in app '{app_label}' not found.")