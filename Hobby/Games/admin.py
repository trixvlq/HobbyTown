from django.contrib import admin
from .models import *


class GameAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Game, GameAdmin)
admin.site.register(GameMaker)
admin.site.register(Category)
admin.site.register(UserReview)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Downvote)
