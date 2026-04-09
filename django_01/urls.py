"""
Корневая URL-конфигурация проекта django.

Здесь определяются главные маршруты, которые Django проверяет
в первую очередь при получении каждого HTTP-запроса.

Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Примеры:
    Функциональные представления:
        path('', views.home, name='home')

    Классовые представления:
        path('', Home.as_view(), name='home')

    Подключение URLconf другого приложения:
        path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # Административный интерфейс Django
    # URL: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),

    # Главная страница проекта
    # URL: http://127.0.0.1:8000/
    path("", views.index, name="index"),

    # Приложение для демонстрации HTTP-ответов и типов URL-параметров
    # URL: http://127.0.0.1:8000/responseApp/
    path("responseApp/", include("responseApp.urls")),

    # Приложение для демонстрации рендеринга шаблонов
    # URL: http://127.0.0.1:8000/renderApp/
    path("renderApp/", include("renderApp.urls")),

    # Приложение для демонстрации форм и работы с данными
    # URL: http://127.0.0.1:8000/websiteApp/
    path("websiteApp/", include("websiteApp.urls")),
]
