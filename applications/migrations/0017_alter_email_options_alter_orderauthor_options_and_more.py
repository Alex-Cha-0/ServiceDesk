# Generated by Django 4.1.4 on 2023-08-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0016_email_author_email_specialist_email_uid_division_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'managed': False, 'ordering': ['-datetime_send'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='orderauthor',
            options={'managed': True, 'ordering': ['author']},
        ),
        migrations.AddField(
            model_name='orderauthor',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='applications.email'),
        ),
    ]
