# django — учебный проект на Django 5.2

Учебный Django-проект, демонстрирующий ключевые концепции фреймворка:
HTTP-ответы, рендеринг шаблонов, работу с формами (GET и POST).

---

## Структура проекта

```
django/
├── config/       # Конфигурация проекта
│   ├── settings.py         # Настройки Django
│   ├── urls.py             # Корневые URL-маршруты
│   ├── views.py            # Главная страница
│   ├── asgi.py             # ASGI-точка входа
│   └── wsgi.py             # WSGI-точка входа
│
├── responseApp/            # Приложение: HTTP-ответы и типы параметров URL
│   ├── views.py            # Представления
│   └── urls.py             # URL-маршруты
│
├── renderApp/              # Приложение: рендеринг шаблонов
│   ├── views.py            # Представления
│   ├── urls.py             # URL-маршруты
│   ├── templates/          # HTML-шаблоны
│   └── static/renderApp/   # CSS, JS, изображения
│
├── websiteApp/             # Приложение: формы GET и POST
│   ├── views.py            # Представления
│   ├── urls.py             # URL-маршруты
│   ├── forms.py            # Django-формы
│   ├── templates/          # HTML-шаблоны
│   └── static/websiteApp/  # CSS, JS, изображения
│
├── static/                 # Общие статические файлы проекта
├── templates/              # Общие шаблоны проекта
├── manage.py               # Утилита управления Django
└── requirements.txt        # Зависимости проекта
```

---

## Приложения и URL-адреса

### responseApp — HTTP-ответы

| URL                                        | Описание                |
| ------------------------------------------ | ----------------------- |
| `/responseApp/`                            | Главная страница        |
| `/responseApp/html/`                       | HTML с текущим временем |
| `/responseApp/calculate/?x=3&y=7`          | Сумма x + y через GET   |
| `/responseApp/f_str/hello`                 | Захват `<str:...>`      |
| `/responseApp/f_int/42`                    | Захват `<int:...>`      |
| `/responseApp/f_slug/my-slug`              | Захват `<slug:...>`     |
| `/responseApp/f_str_int_slug/hi/5/my-slug` | Три параметра сразу     |
| `/responseApp/f_path/a/b/x=10`             | Захват `<path:...>`     |

### renderApp — Шаблоны

| URL                              | Описание                    |
| -------------------------------- | --------------------------- |
| `/renderApp/`                    | Главная с приветствием      |
| `/renderApp/greet/Иванов`        | Приветствие по имени        |
| `/renderApp/page_01/id/page/010` | Первая страница             |
| `/renderApp/page_02/id/page/020` | Вторая страница (с якорями) |
| `/renderApp/pages/first`         | Маршрутизатор страниц       |
| `/renderApp/task/a=2`            | Решение задачи 2001         |
| `/renderApp/objects_arrays/`     | Список товаров и боксов     |

### websiteApp — Формы

| URL                          | Описание                      |
| ---------------------------- | ----------------------------- |
| `/websiteApp/home/`          | Домашняя страница             |
| `/websiteApp/form_abc/`      | JS-форма (проверка диапазона) |
| `/websiteApp/abc_form_get/`  | Django-форма через GET        |
| `/websiteApp/abc_form_post/` | Django-форма через POST       |
| `/websiteApp/form_get_all/`  | Вывод всех GET-параметров     |
| `/websiteApp/store/`         | Магазин (форма заказа)        |
| `/websiteApp/store_result/`  | Результат заказа              |

---

## Инструкция по разворачиванию проекта

### 1. Требования к системе

- Python 3.11 или выше
- pip 23+
- Git (опционально)

Проверить версию Python:

```bash
python --version
# или
python3 --version
```

---

### 2. Получение кода

**Вариант A — распаковать из архива:**

```bash
unzip django.zip
cd django
```

**Вариант B — клонировать из Git:**

```bash
git clone <url-репозитория> django
cd django
```

---

### 3. Создание виртуального окружения

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (cmd):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

После активации в приглашении командной строки появится `(venv)`.

---

### 4. Установка зависимостей

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Проверить установленные пакеты:

```bash
pip list
```

---

### 6. Применение миграций

```bash
python manage.py migrate
```

Ожидаемый вывод — список применённых миграций Django (auth, admin, sessions и т.д.).

---

### 7. Создание суперпользователя (опционально)

Для доступа к административному интерфейсу:

```bash
python manage.py createsuperuser
```

---

### 8. Запуск сервера разработки

```bash
python manage.py runserver
```

По умолчанию сервер запускается на `http://127.0.0.1:8000/`.

Для использования другого порта:

```bash
python manage.py runserver 8080
```

---

### 9. Проверка работоспособности

Откройте в браузере:

- `http://127.0.0.1:8000/` — главная страница проекта
- `http://127.0.0.1:8000/responseApp/` — приложение HTTP-ответов
- `http://127.0.0.1:8000/renderApp/` — приложение шаблонов
- `http://127.0.0.1:8000/websiteApp/` — приложение форм

---

### 12. Остановка сервера

Нажмите `Ctrl + C` в терминале, где запущен сервер.

Деактивировать виртуальное окружение:

```bash
deactivate
```

---
