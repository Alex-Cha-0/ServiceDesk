# Generated by Django 4.1.4 on 2023-08-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_alter_email_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='applications.category'),
        ),

    ]
