from django.urls import include, path
from rest_framework import routers

from games import views

router = routers.DefaultRouter()
router.register("player", views.PlayerViewSet)
router.register("corporation", views.CorporationViewSet)
router.register("game", views.GameViewSet)
router.register("player_game_stats", views.PlayerGameStatsViewSet)

urlpatterns = [path("", include(router.urls))]
