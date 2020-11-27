from django.db import models
from django.db.models import F
from .hero import Hero
from .task import Task

class User_Task(models.Model):

    user = models.ForeignKey(Hero, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("User Task")
        verbose_name_plural = ("User Tasks")

    def __str__(self):
        return self.name
