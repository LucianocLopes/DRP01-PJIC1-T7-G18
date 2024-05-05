# import all base.py for use in dev.py and prod.py
from pi1tg18.settings.base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env.bool("DEBUG", default=False)


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


INSTALLED_APPS += [
    "debug_toolbar",
    'django_extensions',
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# DATABASES = {
#     # read os.environ['DATABASE_URL'] and raises
#     # ImproperlyConfigured exception if not found
#     #
#     # The db() method is an alias for db_url().
#     'default': env.db(),

#     # read os.environ['SQLITE_URL']
#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////tmp/my-tmp-sqlite.db'
#     )
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "pi1t7g18",
        "USER": "lucianoclopes",
        "PASSWORD": "WiLu010381@",
        "OPTIONS": {
            "charset": "utf8mb4",
            "collation": "utf8mb4_unicode_ci",
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
