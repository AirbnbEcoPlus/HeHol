from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import feedparser
# Create your views here.



class LastNewsView(TemplateView):
    template_name: str = "lastnews/lastnews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);


        # Création d'une instance
        news_feed = feedparser.parse('https://www.greenpeace.fr/post_news/feed')
        rss_list = []
        for entry in news_feed.entries:
            rss_list.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', '')
            })

        context['rss_list'] = rss_list

        return context

