from collections import Counter
from typing import Any, Tuple

from rest_framework import serializers

from games.models import Corporation, Game, Player, PlayerGameStats


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("id", "name")


class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = ("id", "name")


class GameSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer(read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "date",
            "played_map",
            "generations_count",
            "players_count",
            "winner",
            "venus_next",
            "prelude",
            "colonies",
        )


class PlayerGameStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    corporation = CorporationSerializer(read_only=True)

    class Meta:
        model = PlayerGameStats
        fields = (
            "id",
            "game",
            "player",
            "corporation",
            "terraforming_rating",
            "milestones",
            "greeneries",
            "cities",
            "red_cards",
            "green_cards",
            "blue_cards",
            "resources",
        )


class PlayerSummarySerializer(serializers.ModelSerializer):
    games_played = serializers.SerializerMethodField("get_games_played")
    games_won = serializers.SerializerMethodField("get_games_won")
    favourite_corporation = serializers.SerializerMethodField(
        "get_favourite_corporation"
    )

    class Meta:
        model = Player
        fields = ("id", "name", "games_played", "games_won", "favourite_corporation")

    def get_games_played(self, player: Player) -> int:
        return PlayerGameStats.objects.filter(player=player).count()

    def get_games_won(self, player: Player) -> int:
        return Game.objects.filter(winner=player).count()

    def get_favourite_corporation(self, player: Player) -> Tuple[Any, int]:
        corporations = PlayerGameStats.objects.filter(player=player).values(
            "corporation__display_name"
        )

        return Counter(
            [c["corporation__display_name"] for c in corporations]
        ).most_common(1)[0]
