"""
Главное представление проекта django.

Обрабатывает запрос на корневой URL ('/') и возвращает
простой текстовый HTTP-ответ — отправная точка проекта.
"""

from django.http import HttpResponse


def index(request):
    """
    Обработчик главной страницы проекта.

    URL: http://127.0.0.1:8000/

    Args:
        request (HttpRequest): Объект HTTP-запроса Django.

    Returns:
        HttpResponse: Простой текстовый ответ с приветствием.
    """
    return HttpResponse(
        "django — учебный проект на Django 5.2  <br>http://127.0.0.1:8000/responseApp/ — приложение HTTP-ответов    <br>http://127.0.0.1:8000/renderApp/ — приложение шаблонов    <br>http://127.0.0.1:8000/websiteApp/` — приложение форм"
    )
