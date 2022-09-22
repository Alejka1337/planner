from rest_framework import generics
from .serializers import TaskSerializer
from .models import Notes


class TaskListApiView(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateApiView(generics.UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyApiView(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = TaskSerializer


class TaskCreateApiView(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = TaskSerializer


