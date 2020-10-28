from django.db import models
from django.db.models import F
from .habit import Habit
from .hero import Hero

class Task(models.Model):
  #The habit that the task falls under
  habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

  #Name of the task
  name = models.CharField()

  #Difficulty of the task determines the experience awarded
  difficulty = models.CharField()
  exp_awarded = models.IntegerField(default=0)

  #Repeatable tasks will give a slight boost to experience if completed on a streak
  repeatable = models.BooleanField(default=False)
  streak = models.IntegerField()
  completed_yesterday = models.BooleanField(default=False)

  #The user that created the task.
  created_by = models.ForeignKey(Hero)

  class Meta:
    verbose_name = ("Task")
    verbose_name_plural = ("Tasks")

  def __str__(self):
    return self.name

