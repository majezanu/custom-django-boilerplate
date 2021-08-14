**A Fantastic Django Custom project starter.**

This project it's based on the Django Edge template (https://django-edge.readthedocs.io/en/latest/)

## Requirements
* Python 3
* Django
* Virtualenv
* Docker

## Quick start:
This section describes the steps to follow to lift the project from this repository. You have two options to do this, one is using docker and docker-compose and the other is using the traditional way with a virtual environment.
### Common steps
This section describes common steps that are recommended to be done regardless of the option chosen to build the project.

I recommend run the following commands to generate the correct files to run this project.

1. To create some `.env` files and `docker-compose` file you need to run:
```bash
$ make initEnvironment
```
This command will create two `.env` files in `app/app/settings` folder:
- `local.env`
- `local.docker.env` 

These two files are the same except for the variable DB_HOST. 

`local.env` has `DB_HOST=localhost` and `local.docker.env` has `DB_HOST=db` Therefore, the latter is necessary so that the containers can be interconnected in docker.

That command also will create a `docker-compose.override.yml` file in root folder.

2. You need to make sure that these variables in the `docker-compose.override.yml` are correctly mapped in the .env as follows
- POSTGRES_DB => DB_NAME
- POSTGRES_USER => DB_USER
- POSTGRES_PASSWORD => DB_PASSWORD

### Using docker (recomended)
This section describes the steps to build the project using docker and docker-compose. Some commands are used that can be seen in the `makefile` file

1. You can build the containers using the following command:
```bash
$ make dockerBuild
```
Or can start the container using:
```bash
$ make dockerUp
```
You can also do the above two things using the following command
```bash
$ make dockerAll
```
The `docker-compose` file is made for the database to get up, run migrations and static files and then I got the django server up

2. Finally, you can create a super user with:
```bash
$ make dockerSuperUser
```

### Normal way
In case you don't want to use docker, then you would have to use the "normal" way of setting up a project in django.

1. You need to create and activate a new virtual environment so that you can install all the necessary packages for your project there.
```bash
$ virtualenv -p python3 <envname>
$ source ./<envname>/bin/activate
```
2. You can run the following command to install requirements:
```bash
$ make requirements
``` 
Note: You can also use the normal command `pip install -r requirements.txt`
3. (Optional) You can use the following command to use the docker-compose to up a Postgres database:
```bash
$ make runDb
```
Note: This command use the `docker-compose.yml` file and it will run the container in detached mode.
4. Finally, you can run the following command to run the django proyect 
```bash
$ make run
```
Note: You can also use the normal command `python3 app/manage.py runserver`

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
