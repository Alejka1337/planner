from django import forms
from .models import *
import datetime as dt


class AddTask(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['task_name', 'task_date']

    def is_valid(self):
        date_now = str(dt.date.today())
        if self.data['task_date'] < date_now:
            return False

        return self.is_bound and not self.errors