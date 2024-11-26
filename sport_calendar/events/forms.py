from django import forms
from .models import Event, EventStatus, Sport
import re


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
                'name',
                'description',
                'fkey_sport',
                'fkey_venue',
                'fkey_home_team',
                'fkey_away_team',
                'date',
                'time',
                'status',
        ]

        labels = {
            'name': 'Event Name',
            'description': 'Description',
            'fkey_sport': 'Sport',
            'fkey_venue': 'Venue',
            'fkey_home_team': 'Home Team',
            'fkey_away_team': 'Away Team',
            'date': 'Date',
            'time': 'Time',
            'status': 'Status',
        }

        widgets = {
            'date': forms.DateInput(attrs={
                                            'type': 'text',
                                            'placeholder': 'dd/mm/yyyy'
                                        }, 
                                    format='%d/%m/%Y'
                                    ),
            'time': forms.TimeInput(attrs={'type': 'time', 'step': 60})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%d/%m/%Y']

    def clean(self):
        cleaned_data = super().clean()
        sport = cleaned_data.get('fkey_sport')
        home_team = cleaned_data.get('fkey_home_team')
        away_team = cleaned_data.get('fkey_away_team')
        venue = cleaned_data.get('fkey_venue')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        self.validate_sport(sport, home_team, away_team)
        
        if not self.venue_available(venue, date, time):
            self.add_error('fkey_venue', 'Venue is not available at the selected date and time.')

        if not self.team_available(home_team, date, time):
            self.add_error('fkey_home_team', 'Home Team is not available at the selected date and time.')

        if not self.team_available(away_team, date, time):
            self.add_error('fkey_away_team', 'Home Team is not available at the selected date and time.')
        
        return cleaned_data
    

    def validate_sport(self, sport, home_team, away_team):
        if sport != home_team.fkey_sport:
            self.add_error('fkey_sport', 'Selected sport does not match with the sport of the Home Team.')

        if sport != away_team.fkey_sport:
            self.add_error('fkey_sport', 'Selected sport does not match with the sport of the Away Team.')

        if home_team == away_team:
            self.add_error('fkey_home_team', 'Home Team and Away Team can not be the same.')


    def venue_available(self, venue, date, time):    
        events = venue.events.filter(status=EventStatus.SCHEDULED, date=date, time=time)
        if events.exists():
            return False
        
            
    def team_available(self, team, date, time):
        # NOTE: should only return 1 event, except of event creation outside of this form
        # e.g. admin interface
        events = team.home_events.filter(status=EventStatus.SCHEDULED, date=date, time=time)
        if events.exists():
            return False

        events = team.away_events.filter(status=EventStatus.SCHEDULED, date=date, time=time)
        if events.exists():
            return False
        
        return True
    

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = [
                'name',
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z ]*$', name):
            raise forms.ValidationError('Name can only contain alphabetical characters and spaces.')

        name = ' '.join(word.capitalize() for word in name.split())
        return name
