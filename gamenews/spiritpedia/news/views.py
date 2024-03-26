from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django import template
from .models import *
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournament_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournaments'] = self.get_queryset()  # Передача турниров в контекст
        return context

class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    paginate_by = 10

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'

class AddTournamentView(CreateView):
    model = Tournament
    template_name = 'add_tournament.html'
    fields = ['name', 'logo', 'game', 'start_date', 'end_date', 'prize_pool', 'teams']
    success_url = reverse_lazy('tournament_list')

class AddTeamView(CreateView):
    model = Team
    template_name = 'add_team.html'
    fields = ['name', 'logo', 'game', 'players']
    success_url = reverse_lazy('team_list')

    
def news(request):
    # Получаем все объекты модели News из базы данных
    news_list = News.objects.all()
    # Передаем список новостей в шаблон
    return render(request, "news.html", {'news_list': news_list})
def guids(request):
    return render(request, "guids.html")
def matches(request):
    return render(request, "matches.html")
def tournaments(request):
    # Создаем объект представления TournamentListView
    tournament_list_view = ListView.as_view(
        queryset=Tournament.objects.all(),  # Здесь выбираем все турниры из базы данных
        template_name='tournament_list.html',  # Указываем имя шаблона для отображения
        paginate_by=10,  # Опционально, если вы хотите разбить список турниров на страницы
        context_object_name='tournaments'  # Указываем имя переменной контекста, в которой будут переданы турниры в шаблон
    )
    # Вызываем метод as_view() представления, передавая ему текущий запрос request
    return tournament_list_view(request)


def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsForm()
    return render(request, 'upload_news.html', {'form': form})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, "news_detail.html", {'news_item': news_item})

def index(request):
    news_list = News.objects.filter(important=True)  # Фильтрация только главных новостей
    return render(request, 'index.html', {'news_list': news_list})

