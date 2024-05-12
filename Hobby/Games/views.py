from django.shortcuts import render, get_object_or_404

from Games.models import Game


def index(request):
    games = Game.objects.all()
    return render(request, 'Games.html', {'Games': games})


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'Games/game.html', {'game': game})
