from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('news', views.news, name='news_list'),
    path('guids', views.guids, name='guids'),
    path('matches', views.matches, name='matches'),
    #path('tournaments', views.tournaments, name='tournaments'),
    path('upload_news', views.upload_news, name='upload_news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
    path('tournaments/', views.TournamentListView.as_view(), name='tournament_list'),
    path('tournaments/<int:pk>/', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('teams/', views.TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('tournaments/add/', views.AddTournamentView.as_view(), name='add_tournament'),
    path('teams/add/', views.AddTeamView.as_view(), name='add_team'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
