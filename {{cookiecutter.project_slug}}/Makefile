all: up

build:
	docker build -t {{cookiecutter.project_slug}}:{{cookiecutter.version}} .

up:
	docker-compose up -d

celery:
	cd {{cookiecutter.project_slug}} && celery -A tasks.celery.celery worker -l info

restart:
	docker-compose restart {{cookiecutter.project_slug}}

run:
	cd {{cookiecutter.project_slug}} && export PYTHONPATH=`pwd` && FLASK_APP=app && flask run

init-db:
	cd {{cookiecutter.project_slug}} && export PYTHONPATH=`pwd` && FLASK_APP=app && flask initdb
