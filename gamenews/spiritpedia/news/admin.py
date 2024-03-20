from django.contrib import admin
from .models import News, Tournament, Team






class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'image', 'important')
    list_filter = ('important',)
    search_fields = ('title', 'summary')

admin.site.register(News, NewsAdmin)

class TournamentAdmin(admin.ModelAdmin):
  list_display = ('image', 'name', 'organizer', 'start_time', 'end_time')
admin.site.register(Tournament, TournamentAdmin)

class TeamAdmin(admin.ModelAdmin):
  list_display = ('logo', 'name', 'players')
admin.site.register(Team, TeamAdmin)

