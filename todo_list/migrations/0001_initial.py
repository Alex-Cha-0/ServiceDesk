# Generated by Django 4.1.4 on 2023-07-31 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('todo_content', models.TextField(blank=True, null=True)),
                ('todo_datetime_add', models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 31, 16, 1, 23, 232471), null=True)),
                ('todo_due_time', models.DateTimeField(blank=True, null=True)),
                ('todo_in_work', models.BooleanField(blank=True, default=False, null=True)),
                ('todo_completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'db_table': 'todo',
                'ordering': ['todo_datetime_add'],
                'managed': True,
            },
        ),
    ]