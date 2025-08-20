from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для таски"""
    class Meta:
        model = Task
        fields = "__all__"
