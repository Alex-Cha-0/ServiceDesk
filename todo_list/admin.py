from django.contrib import admin
from .models import *

class TodoAdmin(admin.ModelAdmin):
    fields = ('todo_content', 'todo_due_time', 'todo_in_work', 'todo_completed', 'todo_spec')
    list_display = ('todo_id', 'todo_content', 'todo_datetime_add', 'todo_due_time', 'todo_in_work', 'todo_completed', 'todo_spec')


admin.site.register(ToDo, TodoAdmin)
