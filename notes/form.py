from django import forms
from .models import *


class AddTask(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['task_name', 'task_date']


