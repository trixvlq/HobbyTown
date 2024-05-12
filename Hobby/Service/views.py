from django.shortcuts import render

from Events.models import *
from Games.models import *


def index(request):
    news = Article.objects.all()
    games = Game.objects.all()
    events = Event.objects.all()
    context = {
        'games': games,
        'events': events,
        'news': news,
        'filters':True
    }
    return render(request, 'Service/index.html', context)
