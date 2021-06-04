from django.views.generic import ListView, DetailView

from .models import Category, Post



class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category__slug=category_id)


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'
    # context_object_name = 'post'







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