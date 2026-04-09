"""
Тесты приложения renderApp.

Документация:
    https://docs.djangoproject.com/en/5.2/topics/testing/

Запуск тестов:
    python manage.py test renderApp
"""

from django.test import TestCase


class RenderAppURLTests(TestCase):
    """Тесты доступности URL-адресов приложения renderApp."""

    def test_index_status_code(self):
        """Главная страница renderApp должна возвращать код 200."""
        response = self.client.get("/renderApp/")
        self.assertEqual(response.status_code, 200)

    def test_greet_status_code(self):
        """Страница приветствия должна возвращать код 200."""
        response = self.client.get("/renderApp/greet/Иванов")
        self.assertEqual(response.status_code, 200)

    def test_objects_arrays_status_code(self):
        """Страница с массивами объектов должна возвращать код 200."""
        response = self.client.get("/renderApp/objects_arrays/")
        self.assertEqual(response.status_code, 200)
