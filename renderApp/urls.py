"""
URL-конфигурация приложения renderApp.

Демонстрирует различные способы захвата параметров из URL
и передачи их в шаблоны через контекст.

Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path

from . import views

# Пространство имён приложения для обратного связывания URL
# Использование: {% url 'renderApp:greet' path_value='Иванов' %}
app_name = "renderApp"

urlpatterns = [
    # Главная страница renderApp
    # URL: /renderApp/
    path("", views.index, name="index"),

    # Приветствие с именем из URL (<str:...> не допускает '/')
    # URL: /renderApp/greet/Иванов
    path("greet/<str:path_value>", views.greet, name="greet"),

    # Первая страница (<path:...> допускает '/' в значении)
    # URL: /renderApp/page_01/id/page/010
    path("page_01/<path:path_value>", views.page_01, name="page_01"),

    # Вторая страница с якорными ссылками
    # URL: /renderApp/page_02/id/page/020
    path("page_02/<path:path_value>", views.page_02, name="page_02"),

    # Маршрутизатор: 'first' → page_01, 'second' → page_02
    # URL: /renderApp/pages/first
    path("pages/<path:path_value>", views.pages, name="pages"),

    # Решение задачи 2001 (знак числа)
    # URL: /renderApp/task/a=2
    path("task/<path:path_value>", views.task, name="task"),

    # Страница с массивами объектов (список товаров и боксов)
    # URL: /renderApp/objects_arrays/
    path("objects_arrays/", views.objects_arrays, name="objects_arrays"),
]
