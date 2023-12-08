"""
URL configuration for HeHol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import IndexView
urlpatterns = [
    path('api/', include("api.urls")),
    path('search/', include("search.urls")),
    path('lastnews/', include("lastnews.urls")),
    path('chatbot/', include("chat.urls", namespace="chat")),
    path('vote/', include("vote.urls", namespace="vote")),
    path('adminpanel/', include("adminpanel.urls")),
    path('', IndexView.as_view(), name="index"),
]
