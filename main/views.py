from django.http import HttpResponse
from django.shortcuts import render

from .models import Category


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})
# TODO: Переписать при помощи классов






# TODO: Список постов
# TODO: Переход по страницам
# TODO: Регистрауия, активация, логин, логаут
# TODO: Фильтрация, поиск сортировка
# TODO: Пагинация
# TODO: Переиспользование шаблонов
# TODO: Проверка прав
# TODO: Избранное
# TODO: Дизайн
# TODO: Описание (README)