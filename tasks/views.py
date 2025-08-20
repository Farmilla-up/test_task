from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    "CRUD над всеми операциями"

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
