from django.db import models

import uuid
from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = "created", "Создано"
        IN_PROGRESS = "in_progress", "В работе"
        DONE = "done", "Завершено"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )

    def __str__(self):
        return self.title
