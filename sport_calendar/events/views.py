from django.shortcuts import render, redirect
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