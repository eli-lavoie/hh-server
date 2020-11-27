from django.db import models
from django.db.models import F

class Stat(models.Model):

  #The name of the stat
  stat_name = models.CharField(max_length=9)

  #The required experience to achieve next level in the stat.
  level_1_exp = models.IntegerField(default=0)
  level_2_exp = models.IntegerField(default=0)
  level_3_exp = models.IntegerField(default=0)
  level_4_exp = models.IntegerField(default=0)
  level_5_exp = models.IntegerField(default=0)
  level_6_exp = models.IntegerField(default=0)
  level_7_exp = models.IntegerField(default=0)
  level_8_exp = models.IntegerField(default=0)
  level_9_exp = models.IntegerField(default=0)
  level_10_exp = models.IntegerField(default=0)

  class Meta:
    verbose_name = ("stat")
    verbose_name_plural = ("stats")

  def __str__(self):
    return self.name
