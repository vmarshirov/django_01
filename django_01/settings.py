"""
Настройки Django для проекта django.

Документация по настройкам:
    https://docs.djangoproject.com/en/5.2/topics/settings/

Полный список параметров:
    https://docs.djangoproject.com/en/5.2/ref/settings/

Чек-лист перед деплоем в production:
    https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Базовые пути
# ---------------------------------------------------------------------------

# Корневая директория проекта (две уровня выше текущего файла)
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Безопасность
# ---------------------------------------------------------------------------

# ВНИМАНИЕ: В production SECRET_KEY необходимо вынести в переменную окружения!
# Пример: SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "fallback-dev-key")
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-zu(fyfxcz#6w3&5t0*kj$g0yc0fpo^jtw8loqwn)3236!g6wn-",
)

# ВНИМАНИЕ: DEBUG=True допустим только при разработке!
# В production обязательно установить DEBUG=False.
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# Список хостов/доменов, которым разрешено обслуживаться этим сайтом.
# В production заменить "*" на конкретный домен, например: ["example.com"]
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",")


# ---------------------------------------------------------------------------
# Приложения
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    # Встроенные приложения Django
    "django.contrib.admin",  # Административный интерфейс
    "django.contrib.auth",  # Система аутентификации
    "django.contrib.contenttypes",  # Типы контента (используется auth и admin)
    "django.contrib.sessions",  # Сессии пользователей
    "django.contrib.messages",  # Система сообщений (flash messages)
    "django.contrib.staticfiles",  # Управление статическими файлами
    # Приложения проекта
    "responseApp",  # Примеры HTTP-ответов и типов URL-параметров
    "renderApp",  # Примеры рендеринга шаблонов и работы с контекстом
    "websiteApp",  # Примеры форм (GET и POST) и работы с магазином
]


# ---------------------------------------------------------------------------
# Промежуточное программное обеспечение (Middleware)
# ---------------------------------------------------------------------------

MIDDLEWARE = [
    # Добавляет заголовки безопасности (HSTS, XSS-защита и т.д.)
    "django.middleware.security.SecurityMiddleware",
    # Управляет сессиями между запросами
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Включает стандартные HTTP-заголовки и завершающий слэш
    "django.middleware.common.CommonMiddleware",
    # Защита от CSRF-атак
    "django.middleware.csrf.CsrfViewMiddleware",
    # Связывает пользователя из сессии с запросом
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Передаёт сообщения между представлениями
    "django.contrib.messages.middleware.MessageMiddleware",
    # Защита от кликджекинга через заголовок X-Frame-Options
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ---------------------------------------------------------------------------
# URL-маршрутизация
# ---------------------------------------------------------------------------

# Корневой модуль URL-конфигурации проекта
ROOT_URLCONF = "django_01.urls"


# ---------------------------------------------------------------------------
# Шаблоны
# ---------------------------------------------------------------------------

TEMPLATES = [
    {
        # Используем стандартный бэкенд шаблонов Django
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Дополнительные директории для поиска шаблонов (общие для всего проекта)
        "DIRS": [BASE_DIR / "templates"],
        # Автоматически искать шаблоны в поддиректории templates/ каждого приложения
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Добавляет переменную debug в контекст шаблона
                "django.template.context_processors.debug",
                # Добавляет объект request в контекст шаблона
                "django.template.context_processors.request",
                # Добавляет объект user и perms в контекст шаблона
                "django.contrib.auth.context_processors.auth",
                # Добавляет объект messages в контекст шаблона
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ---------------------------------------------------------------------------
# WSGI / ASGI
# ---------------------------------------------------------------------------

# Точка входа для WSGI-совместимых серверов (Gunicorn, uWSGI и т.д.)
WSGI_APPLICATION = "django_01.wsgi.application"


# ---------------------------------------------------------------------------
# База данных
# ---------------------------------------------------------------------------

# Используем SQLite для разработки.
# В production рекомендуется PostgreSQL или MySQL.
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------------------------
# Валидация паролей
# ---------------------------------------------------------------------------

# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        # Запрещает пароли, слишком похожие на имя пользователя или email
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        # Требует минимальную длину пароля (по умолчанию 8 символов)
        "NAME": ("django.contrib.auth.password_validation" ".MinimumLengthValidator"),
    },
    {
        # Запрещает распространённые пароли из встроенного списка
        "NAME": ("django.contrib.auth.password_validation" ".CommonPasswordValidator"),
    },
    {
        # Запрещает пароли, состоящие только из цифр
        "NAME": ("django.contrib.auth.password_validation" ".NumericPasswordValidator"),
    },
]


# ---------------------------------------------------------------------------
# Интернационализация
# ---------------------------------------------------------------------------

# Документация: https://docs.djangoproject.com/en/5.2/topics/i18n/

# Язык интерфейса (ru-ru — русский)
LANGUAGE_CODE = "ru-ru"

# Временная зона сервера
TIME_ZONE = "Europe/Moscow"

# Включить перевод строк (gettext)
USE_I18N = True

# Хранить даты/время в БД с учётом часового пояса (UTC)
USE_TZ = True


# ---------------------------------------------------------------------------
# Статические файлы (CSS, JavaScript, изображения)
# ---------------------------------------------------------------------------

# Документация: https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL-префикс для статических файлов
STATIC_URL = "static/"

# Дополнительные директории для поиска статических файлов
# (помимо директорий static/ внутри каждого приложения)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Директория, куда collectstatic собирает все статические файлы
# для production. В разработке не используется.
# STATIC_ROOT = BASE_DIR / "staticfiles"


# ---------------------------------------------------------------------------
# Тип первичного ключа по умолчанию
# ---------------------------------------------------------------------------

# Используем 64-битный целочисленный автоинкрементный ключ
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
