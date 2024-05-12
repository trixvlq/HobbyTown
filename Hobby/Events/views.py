from django.shortcuts import render
from .models import *


def index(request):
    events = Event.objects.all().order_by('date_start')
    dates = events.values_list('date_start', flat=True).distinct()
    for i in dates:
        print(i)
    context = {
        'events': events,
        'dates': dates
    }
    return render(request, 'Events/index.html', context)
