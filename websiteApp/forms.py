"""
Формы приложения websiteApp.

Определяет форму AbcForm для демонстрации двух подходов к отправке данных:
  - GET-запрос  (abc_form_get): данные видны в URL
  - POST-запрос (abc_form_post): данные скрыты, требует CSRF-токен

Документация по формам:
    https://docs.djangoproject.com/en/5.2/topics/forms/
    https://docs.djangoproject.com/en/5.2/ref/forms/fields/
    https://docs.djangoproject.com/en/5.2/ref/forms/api/
"""

from django import forms


class AbcForm(forms.Form):
    """
    Форма для задачи «Равна ли C сумме A и B?».

    Поля:
        content (CharField): Текстовое описание задачи (textarea).
        a (IntegerField): Значение переменной A (необязательное).
        b (IntegerField): Значение переменной B (обязательное).
        c (IntegerField): Значение переменной C (обязательное).
    """

    # Текстовое поле для формулировки задачи.
    # required=True — поле обязательно для заполнения.
    # widget=forms.Textarea() — многострочное поле ввода.
    content = forms.CharField(
        label="Формулировка задачи",
        initial="Равна ли C сумме A и B?",
        required=True,
        widget=forms.Textarea,
    )

    # Числовое поле для переменной A.
    # required=False — поле необязательно; если не заполнено, вернёт None.
    a = forms.IntegerField(
        label="Значение A",
        required=False,
        initial=1,
        widget=forms.NumberInput(),
    )

    # Числовое поле для переменной B (обязательное).
    b = forms.IntegerField(
        label="Значение B",
        initial=2,
        widget=forms.NumberInput(),
    )

    # Числовое поле для переменной C (обязательное).
    # Используется виджет по умолчанию (NumberInput).
    c = forms.IntegerField(
        label="Значение C",
        initial=3,
    )
