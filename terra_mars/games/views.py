from rest_framework import viewsets

from games.models import Corporation, Game, Player, PlayerGameStats
from games.serializers import (
    CorporationSerializer,
    GameSerializer,
    PlayerGameStatsSerializer,
    PlayerSerializer,
)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CorporationViewSet(viewsets.ModelViewSet):
    queryset = Corporation.objects.all()
    serializer_class = CorporationSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerGameStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerGameStats.objects.all()
    serializer_class = PlayerGameStatsSerializer
