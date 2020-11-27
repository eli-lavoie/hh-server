from django.db import models
from django.db.models import F
from .stat import Stat
from .hero import Hero

class Habit(models.Model):
  #The stat that the habit falls under
  stat = models.ForeignKey(Stat, on_delete=models.CASCADE)

  #The name of the stat
  name = models.CharField(max_length=25)

  #The creator of the habit
  created_by = models.ForeignKey(Hero, on_delete=models.CASCADE)
  

  class Meta:
    verbose_name = ("Habit")
    verbose_name_plural = ("Habits")

  def __str__(self):
    return self.name

