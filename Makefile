MANAGE := poetry run python manage.py

install:
	poetry install

test:
	@$(MANAGE) test

start:
	poetry install
	@$(MANAGE) migrate
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

migrate:
	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage run ./manage.py test
	poetry run coverage xml
