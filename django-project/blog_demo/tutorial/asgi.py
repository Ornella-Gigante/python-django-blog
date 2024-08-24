"""
ASGI config for tutorial project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/

Es una interfaz de puerta del servidor pero con soporte asincrono (que no ocurre al mismo tiempo)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")

application = get_asgi_application()
