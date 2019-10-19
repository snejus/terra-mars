#!/usr/bin/env python
import os
import sys
import time

from django.db import connections
from django.db.utils import OperationalError


def main() -> None:
    if should_ensure_database_connection():
        ensure_database_connection()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def should_ensure_database_connection() -> bool:
    return os.getenv("DJANGO_SETTINGS_MODULE") != "terra_mars.settings.static"


def ensure_database_connection() -> None:
    db_conn = connections["default"]
    is_connected = False
    attempts = 0
    while not is_connected and attempts < 10:
        try:
            db_conn.ensure_connection()
            is_connected = True
            print("Connected to database")
        except OperationalError:
            print("Can't connect to database, retrying...")
            attempts += 1
            time.sleep(6)
    else:
        if not is_connected:
            raise Exception("Could not connect to database after 10 attempts.")


if __name__ == "__main__":
    main()
