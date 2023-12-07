from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import WebSiteForm
# Create your views here.

class AddWebSite(FormView):
    template_name: str = "admin/addwebsite.html"
    form_class = WebSiteForm
    success_url = "/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
