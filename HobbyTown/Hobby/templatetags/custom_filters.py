from django import template
from ..models import *
register = template.Library()

@register.filter
def custom_range(value):
    return range(value)
@register.filter
def dif(first,second):
    return range(first-second)
@register.filter
def empty_check(games):
    values = [i for i in games]
    ids = []
    for i in values:
        id = ''
        for j in str(i)[15:]:
            if j not in '1234567890':
               break
            else:
                id += j
        ids.append(id)
    objects = EventGame.objects.filter(id__in=ids)
    if objects.filter(players__gt=0):
        return True
    else:
        return False