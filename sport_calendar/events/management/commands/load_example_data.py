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
            venue, created = Venue.objects.get_or_create(_fkey_country=country, **venue_data)
            venues[venue.name] = venue

        sports = {}
        for sport_data in data['sports']:
            sport, created = Sport.objects.get_or_create(**sport_data)
            sports[sport.name] = sport

        teams = {}
        for team_data in data['teams']:
            sport_name = team_data.pop('sport')
            sport = sports[sport_name]
            team, created = Team.objects.get_or_create(_fkey_sport=sport, **team_data)
            teams[team.name] = team

        for event_data in data['events']:
            sport_name = event_data.pop('sport')
            venue_name = event_data.pop('venue')
            team_names = event_data.pop('teams')

            sport = sports[sport_name]
            venue = venues[venue_name]
            
            teams = [teams.get(team_name) for team_name in team_names ]
            event, created = Event.objects.get_or_create(
                                        _fkey_sport=sport, 
                                        _fkey_venue=venue,
                                         **event_data)
            if created:
                event._fkey_teams.add(*teams)
                print(event) 
        self.stdout.write(self.style.SUCCESS('Example data loaded successfully.'))