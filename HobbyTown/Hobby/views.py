import re
from .bot import *
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import redirect
from django.utils import timezone
from .serializers import *
from rest_framework import generics


class ShowAPIView(generics.ListAPIView):
    queryset = EventSign.objects.all().order_by('time')
    serializer_class = FormSerializer


def send_mail(request, event_slug):
    if request.method == "POST":
        event = Event.objects.get(slug=event_slug)
        name = request.POST.get('name')
        number = request.POST.get('number')
        game_ids = request.POST.getlist('choices')
        games = EventGame.objects.filter(id__in=game_ids)
        with transaction.atomic():
            for game in games:
                game.current += 1
                game.players -= 1
                if game.players == 0:
                    send_message(f"На игру {game} игротеки {game.event.title} места закончились!")
                game.save()
        event_sign = EventSign.objects.create(event=event, name=name, number=number)
        event_sign.games.set(games)
        games_selected = EventGame.objects.filter(id__in = game_ids)
        game_strings = [str(game) for game in games_selected]
        print(game_strings)
        result = ', '.join(game_strings)
        if len(games_selected) > 1:
            message = f"На игротеку {event.title} записался {name} под номером {number} на игры {result}."
        else:
            message = f"На игротеку {event.title} записался {name} под номером {number} на игру {result}."
        print(message)
        send_message(message)


        return redirect('home')


def index(request):
    current_time = timezone.now()
    events = Event.objects.filter(date_start__gt=current_time)
    games = EventGame.objects.all()
    days = sorted(set(event.date_start.date() for event in events))
    forms = [EventSignForm(instance=event, games=games.filter(event=event)) for event in events]
    data = zip(events, forms)
    print(days)
    context = {
        'events': events,
        "forms": forms,
        'data': zip(events, forms),
        'days': days,
        'games': games,
    }
    return render(request, 'index.html', context)
