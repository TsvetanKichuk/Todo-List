from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("tasks:tags-list")

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField(max_length=5000)
    datetime = models.DateTimeField(auto_now_add=True)
    boolean = models.BooleanField(default=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["datetime", "boolean"]

    def get_absolute_url(self):
        return reverse("tasks:tasks-list")

    def __str__(self):
        return f"{self.content} ({self.boolean} {self.datetime} {self.tags.name})"
