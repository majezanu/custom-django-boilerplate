# VARIABLES 
TEST = ./test/
SOURCE = ./source/
VAR:=$(shell python3 app/tools/key_generator.py) 
# COMMANDS
initEnvironment:
	cp docker-compose.override.example.yml ./docker-compose.override.yml
	cp app/app/settings/local.sample.env app/app/settings/local.env
	cp app/app/settings/local.sample.env app/app/settings/local.docker.env
	echo "SECRET_KEY=$(VAR)" >> app/app/settings/local.env \
	&& echo "DB_HOST='localhost'" >> app/app/settings/local.env \
	&& echo "SECRET_KEY=$(VAR)" >> app/app/settings/local.docker.env \
	&& echo "DB_HOST='db'" >> app/app/settings/local.docker.env 
	
dockerBuild:
	docker-compose build

dockerUp:
	docker-compose up

dockerAll: dockerBuild dockerUp
	
dockerSuperUser:
	docker-compose exec django python3 app/manage.py createsuperuser --settings=app.settings.dev_docker

dockerUnitTest:
	docker-compose build \
	&& docker-compose run --service-ports testing python3 app/manage.py test --settings=app.settings.dev_docker

requirements: # Install requirements
	pip install -r requirements.txt

runDb:
	docker-compose up -d db

run: # Run project
	python3 app/manage.py runserver

unitTest:
	python3 app/manage.py test