from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class SearchView(TemplateView):
    template_name: str = "search/search.html"
