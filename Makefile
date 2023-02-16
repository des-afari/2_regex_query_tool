.PHONY: install
install:
	poetry install 

.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: createsuperuser
createsuperuser:
	poetry run python manage.py createsuperuser