from django.urls import include, path
from rest_framework import routers

from games import views

router = routers.DefaultRouter()
router.register("player", views.PlayerViewSet)

urlpatterns = [path("", include(router.urls))]
