ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .envs
endif


build:
	docker-compose up -d --build --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

down-v:
	docker-compose down -v

logs:
	docker-compose logs -f

makemigrations:
	docker-compose run --rm monolith_backend python manage.py makemigrations

migrate:
	docker-compose run --rm monolith_backend python manage.py migrate --no-input

superuser:
	docker-compose run --rm monolith_backend python manage.py createsuperuser

shell:
	docker-compose run --rm monolith_backend python manage.py shell_plus
