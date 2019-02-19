"""
WSGI config for Proyecto_AYD2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/Proyecto_AYD2')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/Proyecto_AYD2/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proyecto_AYD2.settings")
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()


