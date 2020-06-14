install: build migrate

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

migrate:
	docker-compose run --rm web python manage.py migrate

importdata:
	docker-compose run --rm web python manage.py import_initial_data
