import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi1t7g18.settings.dev')

application = get_wsgi_application()
