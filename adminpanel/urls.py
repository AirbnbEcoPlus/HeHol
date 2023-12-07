from django.urls import path, include
from .views import AddWebSite

urlpatterns = [
    path('addwebsite/', AddWebSite.as_view(), name="addwebsite")
]
