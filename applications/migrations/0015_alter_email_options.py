# Generated by Django 4.1.4 on 2023-08-22 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0014_orderauthor_alter_chat_options_alter_thema_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'managed': True, 'ordering': ['-datetime_send'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
