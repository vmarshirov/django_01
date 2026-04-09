"""
Конфигурация приложения renderApp.

Документация:
    https://docs.djangoproject.com/en/5.2/ref/applications/
"""

from django.apps import AppConfig


class RenderAppConfig(AppConfig):
    """
    Класс конфигурации для приложения renderApp.

    Attributes:
        default_auto_field (str): Тип поля первичного ключа по умолчанию.
        name (str): Полное Python-имя приложения.
    """

    # Тип первичного ключа по умолчанию для всех моделей приложения
    default_auto_field = "django.db.models.BigAutoField"

    # Имя приложения должно совпадать с именем пакета Python
    name = "renderApp"
