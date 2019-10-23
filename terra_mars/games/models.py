from enum import Enum

from django.db import models


class MapName(Enum):
    DEFAULT = "Default"
    HELLAS = "Hellas"
    ELYSIUM = "Elysium"


class CorporationName(Enum):
    CREDICOR = "Credicor"
    ECOLINE = "Ecoline"
    HELION = "Helion"
    MINING_GUILD = "Mining Guild"
    INVENTRIX = "Inventrix"
    INTERPLANETARY_CINEMATICS = "Interplanetary Cinematics"
    PHOBOLOG = "Phobolog"
    SATURN_SYSTEMS = "Saturn Systems"
    TERACTOR = "Teractor"
    THARSIS_REPUBLIC = "Tharsis Republic"
    THORGATE = "Thorgate"
    UNMI = "UNMI"
    CHEUNG_SHING_MARS = "Cheung Shing Mars"
    ROBINSON_INDUSTRIES = "Robinson Industries"
    POINT_LUNA = "Point Luna"
    VALLEY_TRUST = "Valley Trust"
    VITOR = "Vitor"
    ARKLIGHT = "Arklight"
    ARIDOR = "Aridor"
    POLYPHEMOS = "Polyphemos"
    POSEIDON = "Poseidon"
    STORMCRAFT_INCORPORATED = "Stormcraft Incorporated"


class Corporation(models.Model):
    name = models.CharField(
        max_length=32, choices=[(tag.value, tag.name) for tag in CorporationName]
    )


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
    greeneries = models.PositiveSmallIntegerField()
    cities = models.PositiveSmallIntegerField()
    red_cards = models.PositiveSmallIntegerField()
    green_cards = models.PositiveSmallIntegerField()
    blue_cards = models.PositiveSmallIntegerField()
    resources = models.PositiveSmallIntegerField()
