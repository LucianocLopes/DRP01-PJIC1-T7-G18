import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi1t7g18.settings.dev')

application = get_asgi_application()
