import csv
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

        previous_row_game_index = 0
        for raw_row in reader:
            row = _process_raw_row(raw_row)

            if row["game_index"] != previous_row_game_index:
                # initialise new game
                month, day, year = [int(number) for number in row["date"].split("/")]
                game = Game(
                    date=date(year, month, day),
                    played_map=row["played_map"],
                    generations_count=row["generations_count"],
                    players_count=row["players_count"],
                    venus_next=False,
                    prelude=True if row["prelude"] == 1 else False,
                    colonies=True if row["colonies"] == 1 else False,
                )

            player, created = Player.objects.get_or_create(
                name=row["player_name"], defaults={"name": row["player_name"]}
            )

            if created:
                player.save()

            if row["winner"] == 1:
                game.winner = player
                game.save()

            corporation, created = Corporation.objects.get_or_create(
                name=row["player_corporation"],
                defaults={"name": row["player_corporation"]},
            )

            if created:
                corporation.save()

            player_game_stats = PlayerGameStats(
                player=player,
                corporation=corporation,
                terraforming_rating=row["terraforming_rating"],
                milestones=row["milestones"],
                awards=row["awards"],
                greeneries=row["greeneries"],
                cities=row["cities"],
                red_cards=row["red_cards"],
                green_cards=row["green_cards"],
                blue_cards=row["blue_cards"],
                resources=row["resources"],
                total_score=row["total_score"],
            )


def _process_raw_row(raw_row: List[str]) -> Dict[str, str]:
    row = {}
    for name, index in CSV_ROW_INDICES.items():
        row[name] = raw_row[index]

    return row
