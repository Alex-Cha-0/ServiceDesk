from django.shortcuts import render
from django.views.generic import ListView
from models import ToDo


class ListOfDo(ListView):
    model = ToDo
    template_name = "todo.html"
    context_object_name = 'data'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListOfDo, self).get_context_data(**kwargs)
        context['title'] = 'Список дел'
        # message_id = self.kwargs.get('message_id', None)
        # context['data_message'] = Attachments.objects.all()

        return context


