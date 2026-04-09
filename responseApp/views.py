"""
Представления приложения responseApp.

Демонстрирует различные способы формирования HTTP-ответов в Django:
  - Простой текстовый ответ
  - Ответ с HTML-содержимым
  - Обработка GET-параметров из строки запроса
  - Различные типы URL-параметров: str, int, slug, path

Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
    https://docs.djangoproject.com/en/5.2/topics/http/views/
"""

import datetime

from django.http import HttpResponse


def index(request):
    """
    Главная страница приложения responseApp.

    URL: http://127.0.0.1:8000/responseApp/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Простой текстовый ответ.
    """
    return HttpResponse("responseApp — приложение для демонстрации HTTP-ответов")


def html(request):
    """
    Возвращает HTML-страницу с текущим временем сервера.

    URL: http://127.0.0.1:8000/responseApp/html/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: HTML-ответ с текущей датой и временем.
    """
    # Получаем текущее время на сервере
    now = datetime.datetime.now()
    return HttpResponse(f"<html><body>Сейчас {now}.</body></html>")


def calculate_get(request):
    """
    Простой калькулятор суммы двух чисел через GET-параметры.

    URL: http://127.0.0.1:8000/responseApp/calculate/?x=1&y=2

    Параметры GET-запроса:
        x (str): Первое слагаемое (по умолчанию "0").
        y (str): Второе слагаемое (по умолчанию "0").

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: HTML-ответ с результатом или сообщением об ошибке.
    """
    # Извлекаем параметры x и y из строки запроса, по умолчанию "0"
    x_str = request.GET.get("x", "0")
    y_str = request.GET.get("y", "0")

    try:
        # Пробуем привести строки к числам с плавающей точкой
        x = float(x_str)
        y = float(y_str)
        z = x + y
        result = (
            f"<h1>Калькулятор GET</h1>"
            f"<p>x = {x}</p>"
            f"<p>y = {y}</p>"
            f"<h2>z = x + y = {z}</h2>"
        )
    except ValueError:
        # Если параметры не являются числами — возвращаем понятную ошибку
        result = (
            "<h1>Ошибка</h1>"
            "<p>Передайте числовые значения для x и y. "
            "Пример: <code>?x=10&amp;y=5</code></p>"
        )

    return HttpResponse(result)


def f_str(request, str_value):
    """
    Демонстрирует захват строкового параметра из URL (<str:...>).

    URL: http://127.0.0.1:8000/responseApp/f_str/abc

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        str_value (str): Строковый параметр из URL (не содержит '/').

    Returns:
        HttpResponse: HTML-ответ с полученным значением.
    """
    return HttpResponse(f"<p>f_str — str_value: {str_value}</p>")


def f_int(request, int_value):
    """
    Демонстрирует захват целочисленного параметра из URL (<int:...>).

    URL: http://127.0.0.1:8000/responseApp/f_int/12345

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        int_value (int): Целочисленный параметр из URL. Django
                         автоматически преобразует строку в int.

    Returns:
        HttpResponse: Текстовый ответ с типом и значением параметра.
    """
    return HttpResponse(
        f"f_int — тип: {type(int_value).__name__}, int_value: {int_value}"
    )


def f_slug(request, slug_value):
    """
    Демонстрирует захват slug-параметра из URL (<slug:...>).

    Slug — строка из ASCII-букв, цифр, дефисов и нижних подчёркиваний.

    URL: http://127.0.0.1:8000/responseApp/f_slug/building-your-1st-django-site

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        slug_value (str): Slug-параметр из URL.

    Returns:
        HttpResponse: Текстовый ответ с полученным slug.
    """
    return HttpResponse(f"f_slug — slug_value: {slug_value}")


def f_str_int_slug(request, str_value, int_value, slug_value):
    """
    Демонстрирует одновременный захват нескольких параметров разных типов.

    URL: http://127.0.0.1:8000/responseApp/f_str_int_slug/hello/123/my-slug

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        str_value (str): Строковый параметр.
        int_value (int): Целочисленный параметр.
        slug_value (str): Slug-параметр.

    Returns:
        HttpResponse: HTML-ответ со всеми параметрами.
    """
    return HttpResponse(
        f"str_value: {str_value}<br>"
        f"int_value: {int_value}<br>"
        f"slug_value: {slug_value}"
    )


def f_path(request, path_value):
    """
    Демонстрирует захват пути произвольной вложенности (<path:...>).

    В отличие от <str:...>, path-конвертер захватывает '/' в URL.
    Пример URL: http://127.0.0.1:8000/responseApp/f_path/building/your-1st/x=42

    Ожидаемая структура пути: segment1/segment2/x=<число>

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Полный путь из URL, включая все '/'.

    Returns:
        HttpResponse: Текстовый ответ со значением x из последнего сегмента.
    """
    # Разбиваем путь на сегменты по символу '/'
    path_elements = path_value.split("/")

    # Извлекаем значение x из последнего сегмента формата "x=<число>"
    last_segment = path_elements[-1]
    x = last_segment.split("=")[1] if "=" in last_segment else "не найдено"

    return HttpResponse(f"f_path — x: {x}")
