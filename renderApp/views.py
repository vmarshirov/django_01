"""
Представления приложения renderApp.

Демонстрирует работу с шаблонами Django:
  - Передача контекста в шаблон
  - Захват параметров из URL (str, path)
  - Условное ветвление и перенаправление
  - Передача массивов объектов в шаблон

Документация:
    https://docs.djangoproject.com/en/5.2/topics/templates/
    https://docs.djangoproject.com/en/5.2/ref/templates/builtins/
    https://docs.djangoproject.com/en/5.2/ref/templates/language/
"""

from django.shortcuts import redirect, render
from django.templatetags.static import static


def index(request):
    return render(request, "layout.html")


def greet(request, path_value):
    """
    Страница приветствия с именем из URL.

    URL: http://127.0.0.1:8000/renderApp/greet/Иванов

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Строка из URL (имя пользователя для приветствия).

    Returns:
        HttpResponse: Отрендеренный шаблон greet.html с именем.
    """
    # Передаём захваченное имя в шаблон через словарь контекста
    context = {"key": path_value}
    return render(request, "greet.html", context)


def page_01(request, path_value):
    """
    Первая страница с произвольным URL-путём.

    URL: http://127.0.0.1:8000/renderApp/page_01/id/page/010

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Произвольный путь из URL (включая '/').

    Returns:
        HttpResponse: Отрендеренный шаблон page_01.html.
    """
    context = {"path_value": path_value}
    return render(request, "page_01.html", context)


def page_02(request, path_value):
    """
    Вторая страница с якорными ссылками для навигации внутри страницы.

    URL: http://127.0.0.1:8000/renderApp/page_02/id/page/020

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Произвольный путь из URL (включая '/').

    Returns:
        HttpResponse: Отрендеренный шаблон page_02.html.
    """
    context = {"path_value": path_value}
    return render(request, "page_02.html", context)


def pages(request, path_value):
    """
    Маршрутизатор страниц: направляет на page_01 или page_02.

    Демонстрирует условное ветвление и редиректы.

    URL: http://127.0.0.1:8000/renderApp/pages/first
    URL: http://127.0.0.1:8000/renderApp/pages/second

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Значение 'first', 'second' или произвольное.

    Returns:
        HttpResponse: Отрендеренный шаблон или redirect.
    """
    context = {"path_value": path_value}

    if path_value == "first":
        # Отображаем первую страницу
        return render(request, "page_01.html", context)
    elif path_value == "second":
        # Отображаем вторую страницу
        return render(request, "page_02.html", context)
    else:
        # При неизвестном значении перенаправляем на page_01
        return redirect("renderApp:page_01", path_value=path_value)


def task_solution(a_value):
    """
    Вспомогательная функция: проверяет знак числа.

    Демонстрирует вынесение бизнес-логики из представления.

    Args:
        a_value (int): Проверяемое целое число.

    Returns:
        str: Строка с результатом проверки ("a > 0" или "a <= 0").
    """
    if a_value > 0:
        result_value = "a > 0"
    else:
        result_value = "a <= 0"
    return result_value


def task(request, path_value):
    """
    Представление решения задачи: определяет знак числа из URL.

    Задача 2001: «Значение переменной a больше нуля?»

    URL: http://127.0.0.1:8000/renderApp/task/a=2
    URL: http://127.0.0.1:8000/renderApp/task/a=-5

    Ожидаемый формат path_value: "a=<целое_число>"

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        path_value (str): Путь вида "a=<число>" или "a=<число>/...".

    Returns:
        HttpResponse: Отрендеренный шаблон task.html с результатом.
    """
    # Разбиваем путь на сегменты (на случай вложенных путей)
    path_elements = path_value.split("/")

    # Извлекаем значение переменной a из первого сегмента ("a=<число>")
    list_a = path_elements[0].split("=")
    int_a = int(list_a[1])

    # Получаем результат через вспомогательную функцию
    result_value = task_solution(int_a)

    # Формулировка задачи
    formulation_value = "2001. Значение переменной a больше нуля?"

    context = {
        "formulation_value": formulation_value,
        "a_value": int_a,
        "result_value": result_value,
    }
    return render(request, "task.html", context)


def objects_arrays(request):
    """
    Страница демонстрации передачи массивов объектов в шаблон.

    Показывает два независимых массива: товары и боксы.
    Шаблон перебирает их с помощью тега {% for %}.

    URL: http://127.0.0.1:8000/renderApp/objects_arrays/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон objects_arrays.html.
    """
    # Массив товаров: первые два используют локальные изображения,
    # остальные — внешние URL (GitHub raw).
    # Для локальных изображений вызываем static() на стороне Python,
    # чтобы шаблон получал готовый URL без использования {% static variable %}.
    goods_array = [
        {
            "id": "1",
            "title": "Товар 1",
            "vendor_code": "VC111",
            "description": "Описание 1",
            "price": 100,
            # static() возвращает URL вида '/static/renderApp/images/uso_001.jpg'
            "img": static("renderApp/images/uso_001.jpg"),
        },
        {
            "id": "2",
            "title": "Товар 2",
            "vendor_code": "VC222",
            "description": "Описание 2",
            "price": 200,
            "img": static("renderApp/images/uso_002.jpg"),
        },
        {
            "id": "3",
            "title": "Товар 3",
            "vendor_code": "VC333",
            "description": "Описание 3",
            "price": 300,
            # Внешний URL передаётся как есть — изображение загружается с GitHub
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg",
        },
        {
            "id": "4",
            "title": "Товар 4",
            "vendor_code": "VC444",
            "description": "Описание 4",
            "price": 400,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_004.jpg",
        },
    ]

    # Массив боксов: используют локальные изображения (URL разрешается здесь)
    box_array = [
        {
            "title": "Название 1",
            "description": "Описание 1",
            "img": static("renderApp/images/1_1.png"),
        },
        {
            "title": "Название 2",
            "description": "Описание 2",
            "img": static("renderApp/images/1_2.png"),
        },
    ]

    # Вкладываем оба массива в один словарь контекста
    context = {
        "dict_of_array": {
            "goods_array": goods_array,
            "box_array": box_array,
        }
    }
    return render(request, "objects_arrays.html", context)
