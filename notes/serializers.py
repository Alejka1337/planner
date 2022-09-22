from rest_framework import serializers
from .models import Notes


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("task_name", "performed", "task_date")





