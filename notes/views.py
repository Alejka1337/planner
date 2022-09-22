from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Notes
from .form import AddTask
import calendar
import datetime as dt
from django.core.exceptions import ValidationError

menu = {'title': 'Добавить задачу', 'url': 'add'}

c = calendar.HTMLCalendar(firstweekday=1)
month_cal = c.formatmonth(dt.date.today().year, dt.date.today().month, withyear=False)
titles = ['Список задач', 'Добавить задачу']


def main_page(request):
    '''Главная страница планировщика'''

    task_list = Notes.objects.all().values()
    return render(request, 'notes/main.html', {'task_list': task_list,
                                               'menu': menu,
                                               'title': titles[0]})


def add_page(request):
    '''Страница добавления новой задачи'''

    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.add_error('task_date', ValidationError('Дата не может быть в прошлом'))
    else:
        form = AddTask()

    return render(request, 'notes/add.html', {'menu': menu,
                                              'form': form,
                                              'calendar': month_cal,
                                              'title': titles[1]})


def update_task(request, task_id):
    '''Функция для обновления статуса задачи'''

    task = Notes.objects.get(id=task_id)
    task.performed = not task.performed
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    '''Функция для удаления задачи из БД'''

    task = Notes.objects.get(id=task_id)
    task.delete()
    return redirect('home')


