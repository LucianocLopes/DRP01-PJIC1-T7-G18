"""
WSGI config for pi1tg18 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi1tg18.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi1tg18.settings.prod')
>>>>>>> 01b6098 (new corrections and mysql configurations)

application = get_wsgi_application()
