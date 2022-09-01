from django.db import models
import datetime as dt


class Notes(models.Model):
    task_name = models.CharField(max_length=255, db_index=True, verbose_name='Задача')
    performed = models.BooleanField(default=False, verbose_name='Выполнение')
    task_date = models.DateField(default=f'{dt.date.today()}', verbose_name='Дата')

    def __str__(self):
        return f"{self.task_name}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
