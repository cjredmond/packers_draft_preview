from django.shortcuts import render
from news.models import News
from django.views.generic import TemplateView, ListView, DetailView

class NewsFeedView(TemplateView):
    def get_context_data(self):
        context = super().get_context_data()
        context['articles'] = News.objects.all().order_by('-time')
        return context
    template_name = 'news_feed_view.html'

class NewsDetailView(DetailView):
    model = News
