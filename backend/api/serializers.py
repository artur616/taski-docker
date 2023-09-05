from rest_framework import serializers

from .models import Task

"""
    Сериализатор для работы с пользователями.
"""

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')
