from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django import template
from .models import News
from .forms import NewsForm

def index(request):
    return render(request, "index.html")
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
    return render(request, "tournaments.html")


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

