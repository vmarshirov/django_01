"""
Тесты приложения responseApp.

Запуск тестов:
    python manage.py test responseApp
"""

from django.test import TestCase


class ResponseAppURLTests(TestCase):
    """Тесты доступности URL-адресов приложения responseApp."""

    def test_index_status_code(self):
        """Главная страница responseApp должна возвращать код 200."""
        response = self.client.get("/responseApp/")
        self.assertEqual(response.status_code, 200)

    def test_html_status_code(self):
        """Страница /html/ должна возвращать код 200."""
        response = self.client.get("/responseApp/html/")
        self.assertEqual(response.status_code, 200)

    def test_calculate_get(self):
        """Калькулятор должен корректно считать сумму x+y."""
        response = self.client.get("/responseApp/calculate/", {"x": "3", "y": "7"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"10", response.content)

    def test_calculate_invalid(self):
        """Калькулятор должен вернуть сообщение об ошибке при нечисловых данных."""
        response = self.client.get("/responseApp/calculate/", {"x": "abc", "y": "7"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ошибка".encode(), response.content)

    def test_f_int(self):
        """Захват int-параметра должен работать корректно."""
        response = self.client.get("/responseApp/f_int/42")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"42", response.content)
