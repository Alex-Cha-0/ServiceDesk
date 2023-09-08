from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import ToDo
from django.contrib import messages


class ListOfDo(LoginRequiredMixin, ListView):
    template_name = "todo.html"
    model = ToDo
    context_object_name = 'content'
    raise_exception = True

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return ToDo.objects.filter(todo_spec=user_id, todo_completed=False)


class TodoByActive(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = "todo.html"
    context_object_name = 'content'
    raise_exception = True

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return ToDo.objects.filter(todo_spec=user_id, todo_completed=False)


class TodoByClose(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = "todo.html"
    context_object_name = 'content'
    raise_exception = True

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return ToDo.objects.filter(todo_spec=user_id, todo_completed=True)


def add_todo(request):
    # получаем из данных запроса POST отправленные через форму данные
    content = request.POST.get("content", "Undefined")
    date_due = request.POST.get("date")
    user = User.objects.get(id=request.user.id)
    todo_model = ToDo(todo_content=content, todo_due_time=date_due, todo_spec=user)
    todo_model.save()

    # return HttpResponse(f"<h2>Задача '{content}', добавлена")
    return redirect(f'/todo/{user.id}')


def mark_as_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = True
    model.save()
    return redirect(f'/todo/{requests.user.id}')


def mark_as_complete(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = False
    model.todo_completed = True
    model.save()
    return redirect(f'/todo/{requests.user.id}')


def edit_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = False
    model.todo_completed = False
    model.save()
    return redirect(f'/todo/{requests.user.id}')


def delete_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.delete()
    return redirect(f'/todo/{requests.user.id}')


def update_todo(request, id):
    # получаем из данных запроса POST отправленные через форму данные
    content = request.POST.get("edit_content", "Undefined")
    model = ToDo.objects.get(todo_id=id)
    model.todo_content = content
    model.save()
    # return HttpResponse(f"<h2>Задача '{content}', добавлена")
    return redirect(f'/todo/{request.user.id}')
