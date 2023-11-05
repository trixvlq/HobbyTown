from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib.humanize.templatetags import humanize

class Game(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField()
    def __str__(self):
        return self.title
class EventGame(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    players = models.IntegerField()
    current = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game.title) + "(" + str(self.players) + ')'


class Event(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    games = models.ManyToManyField(Game, through='EventGame')
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    places = models.IntegerField()
    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return self.title

    def get_reverse_url(self):
        return reverse('event', kwargs={'slug': self.slug})


class Sign(models.Model):
    name = models.CharField(max_length=200)
    number = PhoneNumberField(region="KZ")
    time = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey("Event",on_delete=models.CASCADE)

    class Meta:
        abstract = True
    def __str__(self):
        return str(self.name) + str(self.number) + str(self.event) + str(humanize.naturaltime(self.time))
class SpecialSign(Sign):
    games = models.ManyToManyField('EventGame')
    game = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name) + str(self.number) + str(self.game) + str(humanize.naturaltime(self.time))
class RegularSign(Sign):
    pass
