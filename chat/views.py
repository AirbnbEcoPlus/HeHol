from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ChatView(TemplateView):
    template_name: str = "chat/chat.html"
