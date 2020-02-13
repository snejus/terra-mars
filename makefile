build:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml build

up:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml up

down:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml down

makemigrations:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm web python manage.py makemigrations

migrate:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm web python manage.py migrate

importdata:
	docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm web python manage.py import_initial_data
