from .dev_base import *

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()
# Create a local.env file in the settings directory
# But ideally this env file should be outside the git repo
env_file = Path(__file__).resolve().parent / 'local.docker.env'
if env_file.exists():
    environ.Env.read_env(str(env_file))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_USE_TLS=False