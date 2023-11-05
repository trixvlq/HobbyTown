from django.contrib import admin
from .models import *


class EventGameInline(admin.TabularInline):
    model = EventGame


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    inlines = [EventGameInline]


class GameAdmin(admin.ModelAdmin):
    inlines = [EventGameInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(EventGame)
admin.site.register(SpecialSign)
admin.site.register(RegularSign)