#!/usr/bin/env python
"""
Утилита командной строки Django для административных задач.

Использование:
    python manage.py runserver          # Запуск сервера разработки
    python manage.py makemigrations     # Создание файлов миграций
    python manage.py migrate            # Применение миграций к БД
    python manage.py createsuperuser    # Создание администратора
    python manage.py collectstatic      # Сбор статических файлов
    python manage.py shell              # Интерактивная оболочка Django

Документация: https://docs.djangoproject.com/en/5.2/ref/django-admin/
"""

import os
import sys


def main():
    """
    Точка входа для административных команд Django.

    Устанавливает переменную окружения DJANGO_SETTINGS_MODULE
    и передаёт управление стандартному обработчику команд Django.
    """
    # Указываем Django, где находится модуль настроек проекта
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_01.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что Django установлен "
            "и доступен в переменной PYTHONPATH. "
            "Возможно, вы забыли активировать виртуальное окружение?"
        ) from exc

    # Выполняем команду, переданную через аргументы командной строки
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
