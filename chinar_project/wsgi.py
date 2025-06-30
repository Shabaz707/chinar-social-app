# F:\chinar\chinar_project\wsgi.py

"""
WSGI config for chinar_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'chinar_project' project.
# This is crucial for Gunicorn to find your settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chinar_project.settings')

application = get_wsgi_application()
