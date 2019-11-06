from enum import Enum

from django.db import models


class MapName(Enum):
    DEFAULT = "Default"
    HELLAS = "Hellas"
    ELYSIUM = "Elysium"


class Corporation(models.Model):
    display_name = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.name = self.display_name.replace(" ", "-").lower()
        super(Corporation, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    date = models.DateField()
    played_map = models.CharField(
        max_length=16, choices=[(tag.value, tag.name) for tag in MapName]
    )
    generations_count = models.PositiveSmallIntegerField()
    players_count = models.PositiveSmallIntegerField()

    winner = models.ForeignKey(
        "Player", on_delete=models.PROTECT, related_name="games_won"
    )

    venus_next = models.BooleanField()
    prelude = models.BooleanField()
    colonies = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.date} - {self.played_map} - {self.winner.name}"


class PlayerGameStats(models.Model):
    game = models.ForeignKey(
        "Game", on_delete=models.CASCADE, related_name="players_game_stats"
    )

    player = models.ForeignKey(
        "Player", on_delete=models.PROTECT, related_name="games_stats"
    )
    corporation = models.ForeignKey(
        "Corporation", on_delete=models.PROTECT, related_name="games_stats"
    )

    terraforming_rating = models.PositiveSmallIntegerField()
    milestones = models.PositiveSmallIntegerField()
    awards = models.PositiveSmallIntegerField()
    greeneries = models.PositiveSmallIntegerField()
    cities = models.PositiveSmallIntegerField()
    red_cards = models.SmallIntegerField()
    green_cards = models.SmallIntegerField()
    blue_cards = models.SmallIntegerField()
    resources = models.PositiveSmallIntegerField()
    total_score = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{str(self.game)}: {self.player.name}"
