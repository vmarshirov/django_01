from django.templatetags.static import static

# Список товаров в магазине
# Первые два — локальные изображения, остальные — внешние URL

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
        "id": "5",
        "title": "Название 1",
        "vendor_code": "VC555",
        "description": "Описание 5",
        "price": 500,
        "img": static("renderApp/images/1_1.png"),
    },
    {
        "id": "6",
        "title": "Название 2",
        "vendor_code": "VC666",
        "description": "Описание 6",
        "price": 600,
        "img": static("renderApp/images/1_2.png"),
    },
]
