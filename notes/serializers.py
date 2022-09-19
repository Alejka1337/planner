from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.Serializer):
    task_name = serializers.CharField(max_length=255)
    performed = serializers.BooleanField(default=False)
    task_date = serializers.DateTimeField(read_only=True)


# class NotesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



# def encode():
#     model = NotesModel('Учить DRF')
#     model_sr = TaskSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')