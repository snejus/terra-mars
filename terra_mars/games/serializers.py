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
