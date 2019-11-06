build:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml build

up:
	DJANGO_SETTINGS_MODULE=terra_mars.settings.development docker-compose -f docker-compose.yml -f docker-compose.development.yml up

down:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml down

make-migrations:
	DJANGO_SETTINGS_MODULE=terra_mars.settings.development docker-compose -f docker-compose.yml -f docker-compose.development.yml run terra_mars_web python manage.py makemigrations

migrate:
	DJANGO_SETTINGS_MODULE=terra_mars.settings.development docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm terra_mars_web python manage.py migrate

import-initial-data:
	DJANGO_SETTINGS_MODULE=terra_mars.settings.development docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm terra_mars_web python manage.py import_initial_data
