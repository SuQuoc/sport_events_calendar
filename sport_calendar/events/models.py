from django.db import models

class Event(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = 'scheduled'
        ONGOING = 'ongoing'
        FINISHED = 'completed'
        CANCELLED = 'cancelled'

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fkey_sport = models.ForeignKey('Sport', on_delete=models.CASCADE, related_name='events')
    fkey_venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='events')
    fkey_home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_events')
    fkey_away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='away_events')

    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        choices=Status.choices,
        default=Status.SCHEDULED,
    )

    # def __str__(self):
    #     team_names = [team.name for team in self.fkey_teams.all()]
    #     if len(team_names) < 2:
    #         raise ValueError('An event must have at least two teams')
    #     return f'{self.name}: {team_names[0]} vs {team_names[1]}'


class Venue(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fkey_country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='countries')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fkey_sport = models.ForeignKey('Sport', on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.name} - {self.code}'
