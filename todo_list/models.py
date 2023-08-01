from django.db import models
from datetime import datetime

from django.utils import timezone


class ToDo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo_content = models.TextField(blank=True, null=True)
    todo_datetime_add = models.DateTimeField(default=timezone.now, blank=True, null=True)
    todo_due_time = models.DateTimeField(blank=True, null=True)
    todo_in_work = models.BooleanField(default=False, blank=True, null=True)
    todo_completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'todo'
        ordering = ['-todo_datetime_add']

    def __str__(self):
        return str(self.todo_id)


