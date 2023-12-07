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

        # Propriétés du flux
        print(news_feed.feed.keys())

        # Titre du flux
        print("Feed Title:", news_feed.feed.title)

        # Sous-titre du flux
        print("Feed Subtitle:", news_feed.feed.subtitle)

        # Propriétés de chaque item du flux
        print(news_feed.entries[0].keys())

        # Récupération du deernier feed (dernier bulletin CERT-FR)
        for i in range(0, len(news_feed.entries)):
            print(news_feed.entries[i]['title'])
            print(news_feed.entries[i]['link'])
