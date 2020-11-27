from django.db import models
from django.db.models import F
from .title import Title
from .hero import Hero

class Titles_Available(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)


    

    class Meta:
        verbose_name = ("Titles_Available")
        verbose_name_plural = ("Titles_Availables")

    def __str__(self):
        return self.name
