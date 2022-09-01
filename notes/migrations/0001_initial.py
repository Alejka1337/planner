# Generated by Django 4.0.1 on 2022-08-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(db_index=True, max_length=255, verbose_name='Задача')),
                ('performed', models.BooleanField(default=False, verbose_name='Выполнение')),
                ('task_date', models.DateField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]