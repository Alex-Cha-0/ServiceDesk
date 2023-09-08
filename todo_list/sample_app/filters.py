import django_filters
from django.forms import forms, DateInput
from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from todo_list.models import ToDo
from django import forms


# создаём фильтр
class PostFilter(django_filters.FilterSet):
    class Meta:
        model = ToDo
        # Поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
            # Мы хотим чтобы нам выводило имя, хотя бы отдалённо похожее на то, что запросил пользователь
            'todo_content': ['icontains'],  # Ищем по ключевым словам в описании
            'author__user__username': ['icontains'],  # Цена должна быть меньше или равна тому, что указал пользователь
        }
