import csv
from collections import defaultdict
from datetime import date
from typing import Dict, List

from games.models import Corporation, Game, Player, PlayerGameStats

CSV_PATH = "./games/initial_import/terra-mars-initial-data.csv"
CSV_ROW_INDICES = {
    "game_index": 0,
    "date": 1,
    "played_map": 2,
    "prelude": 3,
    "colonies": 4,
    "generations_count": 5,
    "players_count": 6,
    "player_name": 7,
    "player_corporation": 8,
    "winner": 9,
    "terraforming_rating": 10,
    "milestones": 11,
    "awards": 12,
    "greeneries": 13,
    "cities": 14,
    "red_cards": 15,
    "green_cards": 16,
    "blue_cards": 17,
    "resources": 18,
    "total_score": 19,
}


def import_games_to_database() -> None:
    with open(CSV_PATH, "r") as file:
        reader = csv.reader(file, delimiter=",")

        next(reader)

        indexed_games = defaultdict(list)
        for raw_row in reader:
            row = _process_raw_row(raw_row)
            indexed_games[row["game_index"]].append(row)

    for game_rows in indexed_games.values():
        _add_game_to_database(game_rows)


def _process_raw_row(raw_row: List[str]) -> Dict[str, str]:
    row = {}
    for name, index in CSV_ROW_INDICES.items():
        row[name] = raw_row[index]

    return row


def _add_game_to_database(game_rows: List[Dict[str, str]]) -> None:
    year, month, day = [int(number) for number in game_rows[0]["date"].split("-")]
    game = Game(
        date=date(year, month, day),
        played_map=game_rows[0]["played_map"],
        generations_count=int(game_rows[0]["generations_count"]),
        players_count=int(game_rows[0]["players_count"]),
        venus_next=False,
        prelude=game_rows[0]["prelude"] == "1",
        colonies=game_rows[0]["colonies"] == "1",
    )

    incomplete_stats_models = []
    for row in game_rows:
        player, created = Player.objects.get_or_create(
            name=row["player_name"], defaults={"name": row["player_name"]}
        )
        if created:
            player.save()

        if row["winner"] == "1":
            game.winner = player
            game.save()

        corporation_name = row["player_corporation"]
        corporation, created = Corporation.objects.get_or_create(
            display_name=corporation_name, defaults={"display_name": corporation_name}
        )
        if created:
            corporation.save()

        stats = PlayerGameStats(
            player=player,
            corporation=corporation,
            terraforming_rating=int(row["terraforming_rating"]),
            milestones=int(row["milestones"]),
            awards=int(row["awards"]),
            greeneries=int(row["greeneries"]),
            cities=int(row["cities"]),
            red_cards=int(row["red_cards"]),
            green_cards=int(row["green_cards"]),
            blue_cards=int(row["blue_cards"]),
            resources=int(row["resources"]),
            total_score=int(row["total_score"]),
        )
        incomplete_stats_models.append(stats)

    for stats in incomplete_stats_models:
        stats.game = game
        stats.save()
