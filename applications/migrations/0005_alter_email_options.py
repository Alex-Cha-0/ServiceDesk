# Generated by Django 4.1.4 on 2023-08-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_alter_category_options_alter_categorychoice_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'managed': True, 'ordering': ['-datetime_send'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
