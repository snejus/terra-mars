from django.urls import include, path
from rest_framework import routers

from games import views

router = routers.DefaultRouter()
router.register("corporation", views.CorporationViewSet)
router.register("game", views.GameViewSet)
router.register("player", views.PlayerViewSet, basename="player")
router.register("playersummary", views.PlayerSummaryViewSet, basename="playersummary")
router.register("playergamestats", views.PlayerGameStatsViewSet)

urlpatterns = [path("", include(router.urls))]
