"""
URL-конфигурация приложения websiteApp.

Демонстрирует маршрутизацию для приложения с HTML-формами.

Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path

from . import views

# Пространство имён приложения для обратного связывания URL
# Использование: {% url 'websiteApp:home' %}
app_name = "websiteApp"

urlpatterns = [
    # Корневой URL приложения — перенаправляет на home
    # URL: /websiteApp/
    path("", views.home, name="root"),

    # Домашняя страница
    # URL: /websiteApp/home/
    path("home/", views.home, name="home"),

    # JS-форма с проверкой вхождения числа в диапазон (клиентская логика)
    # URL: /websiteApp/form_abc/
    path("form_abc/", views.form_abc, name="form_abc"),

    # Django-форма с отправкой через GET
    # URL: /websiteApp/abc_form_get/
    path("abc_form_get/", views.abc_form_get, name="abc_form_get"),

    # Django-форма с отправкой через POST (требует CSRF-токен)
    # URL: /websiteApp/abc_form_post/
    path("abc_form_post/", views.abc_form_post, name="abc_form_post"),

    # Страница вывода всех параметров GET-запроса
    # URL: /websiteApp/form_get_all/?key=value
    path("form_get_all/", views.form_get_all, name="form_get_all"),

    # Страница магазина с каталогом товаров
    # URL: /websiteApp/store/
    path("store/", views.store, name="store"),

    # Страница результата заказа из магазина
    # URL: /websiteApp/store_result/
    path("store_result/", views.store_result, name="store_result"),
]
