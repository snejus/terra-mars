from django.core.management.base import BaseCommand

from games.initial_import.import_games import import_games_to_database


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        import_games_to_database()
