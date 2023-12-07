from django.urls import path

from .views import LastNewsView

app_name = "lastnews"

urlpatterns = {
    path("", LastNewsView.as_view(), name="lastnews_view")
}
