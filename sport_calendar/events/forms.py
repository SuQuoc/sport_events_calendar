from django import forms
from .models import Event

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
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%d/%m/%Y']

    def clean(self):
        cleaned_data = super().clean()
        sport = cleaned_data.get('fkey_sport')
        home_team = cleaned_data.get('fkey_home_team')
        away_team = cleaned_data.get('fkey_away_team')

        if sport != home_team.fkey_sport:
            self.add_error('fkey_sport', 'Selected sport does not match with the sport of the Home Team.')

        if sport != away_team.fkey_sport:
            self.add_error('fkey_sport', 'Selected sport does not match with the sport of the Away Team.')

        if home_team == away_team:
            self.add_error('fkey_home_team', 'Home Team and Away Team can not be the same.')

        return cleaned_data