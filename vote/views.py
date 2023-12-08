from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from database.models import website
import random
from django.http import JsonResponse

class VoteView(TemplateView):
    template_name: str = "vote/vote.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_website = website.objects.order_by('?').first()
        context['random_website'] = random_website
        return context
