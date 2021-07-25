{% comment "This comment section will be deleted in the generated project" %}

**A Fantastic Django Custom project starter.**

This project it's based on the Django Edge template (https://django-edge.readthedocs.io/en/latest/)

## Requirements
* Python 3
* Django
* Virtualenv
* Docker

## Quick start:

Before creating a new project from this template, you need to create a fresh virtual environment, I recomend use Virtualenv:

1. `$ virtualenv -p python3 <envname>`
2. `$ source <envname>/bin/activate` (use the appropriate activate script based on your shell)

Create your new _edgy_ django project:

1. `$ django-admin.py startproject --template=https://github.com/majezanu/custom-django-boilerplate --extension=py,md,html,env <projname>`
2. `$ cd projname`
3. `$ pip install -r requirements.txt `
4. `$ cd app`
5. `$ cp projname/settings/local.sample.env projname/settings/local.env`
6. `$ python manage.py migrate`
7. `$ python manage.py createsuperuser`
8. `$ python manage.py runserver`

If you need to keep `requirements.txt` updated then run

    pipenv lock --requirements > requirements/base.txt
    echo "-r base.txt" > requirements/development.txt
    pipenv lock --requirements --dev >> requirements/development.txt

Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# app

app is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (short desc)
* App2 (short desc)
* App3 (short desc)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv app`
    2. `$ . app/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
