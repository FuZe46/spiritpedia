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
    path('tournaments', views.tournaments, name='tournaments'),
    path('upload_news', views.upload_news, name='upload_news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
