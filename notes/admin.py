from django.contrib import admin
from .models import *

admin.site.register(Notes)

# class NotesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'task_name', 'performed', 'task_date')
#     list_display_links = ('id', 'task_name')
#     search_fields = ('task_name',)
#     list_editable = ('performed',)
#     list_filter = ('task_name', 'performed', 'task_date')


