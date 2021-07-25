# VARIABLES 
TEST = ./test/
SOURCE = ./source/

# COMMANDS

docker:
	docker-compose build \
	&& docker-compose up

dockerUnittest:
	docker-compose build \
	&& docker-compose run --service-ports testing python3 app/manage.py test 

requirements: # Install requirements
	pip install -r requirements.txt

run: # Run project
	python3 app/manage.py runserver

unittest:
	python3 app/manage.py test