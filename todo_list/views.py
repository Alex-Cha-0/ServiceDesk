from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import ToDo
from django.contrib import messages


class ListOfDo(ListView):
    model = ToDo
    template_name = "todo.html"
    context_object_name = 'content'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListOfDo, self).get_context_data(**kwargs)
        context['title'] = 'Список дел'
        # message_id = self.kwargs.get('message_id', None)
        # context['data_message'] = Attachments.objects.all()

        return context

    def get_queryset(self):
        return ToDo.objects.all()


def add_todo(request):
    # получаем из данных запроса POST отправленные через форму данные
    content = request.POST.get("content", "Undefined")
    date_due = request.POST.get("date")
    todo_model = ToDo(todo_content=content, todo_due_time=date_due)
    todo_model.save()

    # return HttpResponse(f"<h2>Задача '{content}', добавлена")
    return redirect(f'/todo/')


def mark_as_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = True
    model.save()
    return redirect(f'/todo/')


def mark_as_complete(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = False
    model.todo_completed = True
    model.save()
    return redirect(f'/todo/')


def edit_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.todo_in_work = False
    model.todo_completed = False
    model.save()
    return redirect(f'/todo/')


def delete_todo(requests, id):
    model = ToDo.objects.get(todo_id=id)
    model.delete()
    return redirect(f'/todo/')


def update_todo(request, id):
    # получаем из данных запроса POST отправленные через форму данные
    content = request.POST.get("edit_content", "Undefined")
    model = ToDo.objects.get(todo_id=id)
    model.todo_content = content
    model.save()
    # return HttpResponse(f"<h2>Задача '{content}', добавлена")
    return redirect(f'/todo/')
