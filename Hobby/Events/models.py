from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Service.models import *
from Games.models import *


class Event(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_finish = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField()
    address = models.CharField(max_length=100)
    description = models.TextField()
    limit = models.IntegerField()
    limited_games = models.ManyToManyField(Game, through='EventsGames')

    def __str__(self):
        return self.name


class EventsGames(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.event.name + '<-' + self.game.name


class Sign(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(region="KZ")
    date = models.DateField()

    def __str__(self):
        return self.event.name + ' ' + self.name


class SpecialSign(Sign):
    game = models.ForeignKey(EventsGames, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name
