"""
Тесты приложения websiteApp.

Запуск тестов:
    python manage.py test websiteApp
"""

from django.test import TestCase


class WebsiteAppURLTests(TestCase):
    """Тесты доступности URL-адресов приложения websiteApp."""

    def test_home_status_code(self):
        """Домашняя страница должна возвращать код 200."""
        response = self.client.get("/websiteApp/home/")
        self.assertEqual(response.status_code, 200)

    def test_abc_form_get_status_code(self):
        """GET-форма должна возвращать код 200."""
        response = self.client.get("/websiteApp/abc_form_get/")
        self.assertEqual(response.status_code, 200)

    def test_abc_form_get_with_data(self):
        """GET-форма с корректными данными должна вернуть результат."""
        response = self.client.get(
            "/websiteApp/abc_form_get/",
            {"content": "Тест", "a": "1", "b": "2", "c": "3"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("равна".encode(), response.content)

    def test_abc_form_post_get_request(self):
        """POST-форма при GET-запросе должна возвращать пустую форму."""
        response = self.client.get("/websiteApp/abc_form_post/")
        self.assertEqual(response.status_code, 200)

    def test_abc_form_post_with_data(self):
        """POST-форма с корректными данными должна вернуть результат."""
        response = self.client.post(
            "/websiteApp/abc_form_post/",
            {"content": "Тест", "a": "1", "b": "2", "c": "3"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("равна".encode(), response.content)

    def test_store_status_code(self):
        """Страница магазина должна возвращать код 200."""
        response = self.client.get("/websiteApp/store/")
        self.assertEqual(response.status_code, 200)
