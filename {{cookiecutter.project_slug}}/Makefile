all: up

build:
	docker build -t plusfun/push_notification:0.1 .

docker-push:
	docker push onfta/onfta_api:0.1

docker-pull:
	docker pull onfta/onfta_api:0.1

up:
	docker-compose up -d

celery:
	cd push_api && celery -A common.celery.celery worker -l info

restart:
	docker-compose restart push_notification

run:
	cd push_api && python app.py

init-db:
	cd push_api && python manage.py create_schema

d-init-db:
	docker exec -it pushnotification_push_notification_1 python3 manage.py create_schema
