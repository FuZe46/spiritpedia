from django.contrib import admin
from .models import *
from django.forms import widgets

class GameWidget(widgets.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = [(game.pk, game.name) for game in Game.objects.all()]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'image', 'important')
    list_filter = ('important',)
    search_fields = ('title', 'summary')

from .forms import TournamentForm
class TournamentAdmin(admin.ModelAdmin):
    form = TournamentForm
    list_display = ('name', 'game', 'start_date', 'end_date', 'prize_pool')
    list_filter = ('game', 'start_date')
    search_fields = ('name',)
    filter_horizontal = ('teams',)  # Опционально, если вы хотите использовать виджет FilteredSelectMultiple для teams

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "game":
            kwargs["queryset"] = Game.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Tournament, TournamentAdmin)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    search_fields = ('name', 'game')

    formfield_overrides = {
        'game': {
            'widget': GameWidget,
        },
    }

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

@admin.register(TeamPlayer)
class TeamPlayerAdmin(admin.ModelAdmin):
    list_display = ('team', 'player')
    search_fields = ('team__name', 'player__name')  # Search by team and player name

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game',)
    search_fields = ('game',)

