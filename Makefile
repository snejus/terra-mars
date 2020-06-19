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

list:
	docker-compose run --rm web python manage.py

# shell with models and common django things already imported
shell:
	docker-compose run --rm web python manage.py shell_plus --print-sql

# shows SQL difference between models and database state
sqldiff:
	docker-compose run --rm web python manage.py sqldiff decisionbatch

# prints urls for all apps
showurls:
	docker-compose run --rm web python manage.py show_urls


