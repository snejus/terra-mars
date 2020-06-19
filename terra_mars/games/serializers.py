from typing import Dict, Union

from rest_framework import serializers

from games.models import Corporation, Game, Player, PlayerGameStats


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class CorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer(read_only=True)

    class Meta:
        model = Game
        fields = "__all__"


class PlayerGameStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    corporation = CorporationSerializer(read_only=True)

    class Meta:
        model = PlayerGameStats
        fields = "__all__"


class PlayerSummarySerializer(serializers.ModelSerializer):
    """Read-only serializer for player's summary."""

    games_played = serializers.SerializerMethodField()
    games_won = serializers.SerializerMethodField()
    favourite_corporation = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = "__all__"
        read_only_fields = (
            "id",
            "name",
            "games_played",
            "games_won",
            "favourite_corporation",
        )

    def get_games_played(self, player: Player) -> int:
        return player.games_stats.count()

    def get_games_won(self, player: Player) -> int:
        return player.games_won.count()

    def get_favourite_corporation(self, player: Player) -> Dict[str, Union[str, int]]:
        return player.favourite_corp()
