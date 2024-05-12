from django.db.models import Avg, Case, When, Exists, OuterRef
from django.shortcuts import render, get_object_or_404

from Games.models import Game, UserReview, Comment


def index(request):
    games = Game.objects.all()
    return render(request, 'Games.html', {'Games': games})


def game(request, slug):
    game = Game.objects.filter(slug=slug).annotate(
        rating=Case(
            When(
                Exists(UserReview.objects.filter(game=OuterRef('id'))) &
                Exists(Comment.objects.filter(game=OuterRef('id'))),
                then=((Avg('userreview__rating') + Avg('comment__rating')) / 2)
            ),
            When(
                Exists(UserReview.objects.filter(game=OuterRef('id'))) &
                ~Exists(Comment.objects.filter(game=OuterRef('id'))),
                then=Avg('userreview__rating')
            ),
            When(
                ~Exists(UserReview.objects.filter(game=OuterRef('id'))) &
                Exists(Comment.objects.filter(game=OuterRef('id'))),
                then=Avg('comment__rating')
            ),
            default=0.0
        )
    ).first()
    context = {
        'game': game,
        'mega_content': True
    }
    return render(request, 'Games/game.html', context)
