"""
URL-конфигурация приложения responseApp.

Демонстрирует все встроенные конвертеры типов Django:
  <str:...>   — строка без '/' (по умолчанию)
  <int:...>   — неотрицательное целое число
  <slug:...>  — ASCII-буквы, цифры, дефисы и подчёркивания
  <path:...>  — строка, включая символ '/'

Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path

from . import views

# Пространство имён приложения для обратного связывания URL
app_name = "responseApp"

urlpatterns = [
    # Главная страница приложения
    # URL: /responseApp/
    path("", views.index, name="index"),

    # HTML-ответ с текущим временем
    # URL: /responseApp/html/
    path("html/", views.html, name="html"),

    # Калькулятор через GET-параметры (?x=...&y=...)
    # URL: /responseApp/calculate/?x=10&y=5
    path("calculate/", views.calculate_get, name="calculate"),

    # Захват строкового параметра (без '/')
    # URL: /responseApp/f_str/hello
    path("f_str/<str:str_value>", views.f_str, name="f_str"),

    # Захват целочисленного параметра
    # URL: /responseApp/f_int/42
    path("f_int/<int:int_value>", views.f_int, name="f_int"),

    # Захват slug-параметра
    # URL: /responseApp/f_slug/my-first-slug
    path("f_slug/<slug:slug_value>", views.f_slug, name="f_slug"),

    # Захват нескольких параметров разных типов
    # URL: /responseApp/f_str_int_slug/hello/123/my-slug
    path(
        "f_str_int_slug/<str:str_value>/<int:int_value>/<slug:slug_value>",
        views.f_str_int_slug,
        name="f_str_int_slug",
    ),

    # Захват пути с произвольной вложенностью (включая '/')
    # URL: /responseApp/f_path/building/your-1st/x=42
    path("f_path/<path:path_value>", views.f_path, name="f_path"),
]
