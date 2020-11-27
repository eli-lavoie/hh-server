from django.db import models
from django.db.models import F

class Title(models.Model):

    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Title")
        verbose_name_plural = ("Titles")

    def __str__(self):
        return self.name
