# Generated by Django 4.0.1 on 2022-08-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='task_date',
            field=models.DateField(default='2022-08-30 21:04:16.978810', verbose_name='Дата'),
        ),
    ]
