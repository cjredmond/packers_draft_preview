from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from draftpick.models import Player

class IndexView(TemplateView):
    template_name = 'index_view.html'

class DraftpickDetailView(DetailView):
    model = Player
