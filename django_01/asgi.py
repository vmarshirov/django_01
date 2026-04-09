"""
Точка входа ASGI для проекта django.

Предоставляет ASGI-совместимый callable с именем ``application``,
который используется асинхронными серверами (например, Daphne, Uvicorn).

Документация:
    https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Устанавливаем модуль настроек Django по умолчанию
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_01.settings")

# ASGI-приложение, которое передаётся серверу
application = get_asgi_application()
