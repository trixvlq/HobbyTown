from django.contrib import admin
from .models import *


class EventGameInline(admin.TabularInline):
    model = EventsGames


class EventAdmin(admin.ModelAdmin):
    inlines = [EventGameInline]


admin.site.register(Event, EventAdmin)
admin.site.register(EventsGames)
admin.site.register(Sign)
admin.site.register(SpecialSign)
