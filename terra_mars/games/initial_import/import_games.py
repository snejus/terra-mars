import csv

CSV_PATH = "./games/initial_import/terra-mars-initial-data.csv"


def import_games_to_database() -> None:
    with open(CSV_PATH, "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            print(row)
