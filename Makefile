superuser:
	docker exec -it catocms-backend ./manage.py createsuperuser

shell:
	docker exec -it catocms-backend ./manage.py shell

makemigrations:
	docker exec -it catocms-backend ./manage.py makemigrations

migrate:
	docker exec -it catocms-backend ./manage.py migrate

initialfixture:
	docker exec -it catocms-backend ./manage.py loaddata initial

statics:
	docker exec -it catocms-backend ./manage.py collectstatic --noinput

makemessages:
	docker exec -it catocms-backend django-admin makemessages

compilemessages:
	docker exec -it catocms-backend django-admin compilemessages

templatesfixture:
	docker exec -it catocms-backend ./manage.py loaddata templates
