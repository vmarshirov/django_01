"""
Точка входа WSGI для проекта django.

Предоставляет WSGI-совместимый callable с именем ``application``,
который используется синхронными серверами (Gunicorn, uWSGI и т.д.).

Документация:
    https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем модуль настроек Django по умолчанию
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_01.settings")

# WSGI-приложение, которое передаётся серверу
application = get_wsgi_application()
