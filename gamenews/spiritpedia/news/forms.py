from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'summary', 'image', 'important']

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Tournament, Team

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
        widgets = {
            'teams': FilteredSelectMultiple("Teams", is_stacked=False)
        }
