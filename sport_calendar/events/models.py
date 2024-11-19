from django.db import models

# Create your models here.


class Event(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = 'scheduled'
        ONGOING = 'ongoing'
        FINISHED = 'completed'
        CANCELLED = 'cancelled'

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE, related_name="events")
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE, related_name="events")
    teams = models.ManyToManyField("Team", related_name="teams")
    
    date = models.DateTimeField()
    time = models.TimeField()
    status = models.CharField(
        choices=Status.choices,
        default=Status.SCHEDULED,
    )


class Venue(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, related_name="countries")
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE, related_name="teams")

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
        return f"{self.name} - {self.code}"
