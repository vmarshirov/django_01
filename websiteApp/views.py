"""
Представления приложения websiteApp.

Демонстрирует работу с HTML-формами в Django:
  - GET-форма: данные передаются через строку запроса URL
  - POST-форма: данные передаются в теле запроса (с CSRF-защитой)
  - Вывод всех GET-параметров запроса на страницу
  - Простой «магазин» с отправкой заказа через GET

Документация:
    https://docs.djangoproject.com/en/5.2/topics/forms/
    https://docs.djangoproject.com/en/5.2/ref/request-response/
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static

from .forms import AbcForm
from .objects_arrays import box_array, goods_array

# ---------------------------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------------------------


def get_last_url_element(request):
    """
    Извлекает последний значимый сегмент из URL текущего запроса.

    Используется в шаблонах для подсветки активного пункта навигации.
    Например: '/websiteApp/home/' → 'home'

    Args:
        request (HttpRequest): Объект HTTP-запроса Django.

    Returns:
        str: Последний непустой сегмент URL.
    """
    # Разбиваем путь по '/' и берём предпоследний элемент
    # (последний будет пустым из-за завершающего '/')
    url_elements_list = request.path.split("/")
    return url_elements_list[-2]


def solution(a, b, c):
    """
    Проверяет, равно ли значение C сумме A и B.

    Args:
        a (int): Значение переменной A.
        b (int): Значение переменной B.
        c (int): Значение переменной C.

    Returns:
        str: Текстовый результат проверки.
    """
    if a + b == c:
        return "С равна сумме A и B"
    return "С не равна сумме A и B"


# ---------------------------------------------------------------------------
# Представления
# ---------------------------------------------------------------------------


def home(request):
    """
    Домашняя страница приложения websiteApp.

    URL: http://127.0.0.1:8000/websiteApp/home/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон home.html.
    """
    last_url_element = get_last_url_element(request)
    return render(request, "home.html", {"last_url_element": last_url_element})


def form_get_all(request):
    """
    Выводит все ключи и значения текущего GET-запроса на страницу.

    Демонстрирует методы работы с объектом request.GET (QueryDict):
      .keys(), .values(), .items()

    URL: http://127.0.0.1:8000/websiteApp/form_get_all/?a=1&b=2

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон context.html со словарём параметров.
    """
    last_url_element = get_last_url_element(request)

    # Преобразуем QueryDict в обычный dict для передачи в шаблон
    items_dict = dict(request.GET.items())

    context = {
        "items_dict": items_dict,
        "last_url_element": last_url_element,
    }
    return render(request, "context.html", context)


def form_abc(request):
    """
    Страница с JavaScript-формой для проверки вхождения числа в диапазон.

    Логика проверки выполняется на стороне клиента (JS),
    результат отправляется на сервер через GET-запрос.

    URL: http://127.0.0.1:8000/websiteApp/form_abc/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон form_abc.html.
    """
    last_url_element = get_last_url_element(request)
    context = {"last_url_element": last_url_element}
    return render(request, "form_abc.html", context)


def abc_form_get(request):
    """
    Форма Django с отправкой данных через GET-запрос.

    При валидном GET-запросе — вычисляет результат и отображает его.
    При пустом запросе — показывает пустую форму.

    URL: http://127.0.0.1:8000/websiteApp/abc_form_get/
    URL с данными: /websiteApp/abc_form_get/?a=1&b=2&c=3&content=...

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон abc_form_get.html.
    """
    last_url_element = get_last_url_element(request)

    # Инициализируем форму данными из GET-запроса
    form = AbcForm(request.GET)

    if form.is_valid():
        # Извлекаем очищенные и валидированные данные из формы
        form_dict = form.cleaned_data
        a = form_dict["a"]
        b = form_dict["b"]
        c = form_dict["c"]
        result = solution(a, b, c)
        context = {
            "form_get": form,
            "result": result,
            "last_url_element": last_url_element,
        }
    else:
        # Форма не заполнена или содержит ошибки — показываем пустую форму
        form = AbcForm()
        context = {
            "form_get": form,
            "last_url_element": last_url_element,
        }

    return render(request, "abc_form_get.html", context)


def abc_form_post(request):
    """
    Форма Django с отправкой данных через POST-запрос.

    POST-запрос требует CSRF-токен в шаблоне ({% csrf_token %}).
    При валидном POST — вычисляет и показывает результат.
    При GET — отображает пустую форму.
    При невалидном POST — возвращает форму с ошибками.

    URL: http://127.0.0.1:8000/websiteApp/abc_form_post/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон abc_form_post.html.
    """
    last_url_element = get_last_url_element(request)

    if request.method == "POST":
        # Инициализируем форму данными из POST-запроса
        form = AbcForm(request.POST)

        if form.is_valid():
            # Извлекаем очищенные данные
            form_dict = form.cleaned_data
            a = form_dict["a"]
            b = form_dict["b"]
            c = form_dict["c"]
            result = solution(a, b, c)
            context = {
                "form_post": form,
                "result": result,
                "last_url_element": last_url_element,
            }
            return render(request, "abc_form_post.html", context)

        # Форма заполнена, но содержит ошибки — возвращаем с ошибками
        context = {
            "form_post": form,
            "last_url_element": last_url_element,
        }
        return render(request, "abc_form_post.html", context)

    else:
        # GET-запрос — показываем пустую форму
        form = AbcForm()
        context = {
            "form_post": form,
            "last_url_element": last_url_element,
        }
        return render(request, "abc_form_post.html", context)


def store(request):
    """
    Страница магазина со списком товаров и формой заказа.

    Товары отображаются в виде карточек; пользователь вводит количество
    и отправляет заказ через GET-форму на страницу store_result.

    URL: http://127.0.0.1:8000/websiteApp/store/

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон store.html со списком товаров.
    """
    last_url_element = get_last_url_element(request)
    print("last_url_element: ", last_url_element)
    context = {
        "last_url_element": last_url_element,
        "dict_of_array": {"box_array": box_array, "goods_array": goods_array},
    }
    return render(request, "store.html", context)


def store_result(request):
    """
    Страница результата заказа из магазина.

    Получает список артикулов и количеств через GET-параметры
    (несколько значений с одним именем — QueryDict.getlist()).

    URL: /websiteApp/store_result/?vendor_code=VC111&amount=2&vendor_code=VC222&amount=0

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отрендеренный шаблон store_result.html с итогами заказа.
    """
    # getlist() возвращает список всех значений с данным именем параметра
    vendor_codes = request.GET.getlist("vendor_code")
    amounts = request.GET.getlist("amount")

    # Формируем словарь: артикул → количество
    order_dict = dict(zip(vendor_codes, amounts))

    return render(request, "store_result.html", {"d": order_dict})
