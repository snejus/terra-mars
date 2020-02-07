from django.urls import path

from .views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
    path("games", IndexView.as_view()),
    path("players", IndexView.as_view()),
]
