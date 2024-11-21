import os
import json
from django.core.management.base import BaseCommand
from events.models import Venue, Team, Sport, Country, Event

class Command(BaseCommand):
    help = 'Load initial data from examples.json if no events are available'

    def handle(self, *args, **kwargs):
        if Event.objects.exists():
            self.stdout.write(self.style.SUCCESS('Events already exist. No data loaded.'))
            return

        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'examples.json')

        with open(file_path) as f:
            data = json.load(f)

        countries = {}
        for country_data in data['countries']:
            country, created = Country.objects.get_or_create(**country_data)
            countries[country.name] = country

        venues = {}
        for venue_data in data['venues']:
            country_name = venue_data.pop('country')
            country = countries[country_name]
            venue, created = Venue.objects.get_or_create(fkey_country=country, **venue_data)
            venues[venue.name] = venue

        sports = {}
        for sport_data in data['sports']:
            sport, created = Sport.objects.get_or_create(**sport_data)
            sports[sport.name] = sport

        teams = {}
        for team_data in data['teams']:
            sport_name = team_data.pop('sport')
            sport = sports[sport_name]
            team, created = Team.objects.get_or_create(fkey_sport=sport, **team_data)
            teams[team.name] = team

        for event_data in data['events']:
            sport_name = event_data.pop('sport')
            venue_name = event_data.pop('venue')
            home_team_name = event_data.pop('home_team')
            away_team_name = event_data.pop('away_team')
            
            home_team = teams[home_team_name]
            away_team = teams[away_team_name]
            sport = sports[sport_name]
            venue = venues[venue_name]
            
            event, created = Event.objects.get_or_create(
                                        fkey_sport=sport, 
                                        fkey_venue=venue,
                                        fkey_home_team=home_team,
                                        fkey_away_team=away_team,
                                         **event_data)
        
        self.stdout.write(self.style.SUCCESS('Example data loaded successfully.'))