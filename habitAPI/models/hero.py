#TODO: Add theme fkey after creating theme model


from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .title import Title

class Hero(models.Model):
  #Link to a user created by registering on website
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  #Level values for each stat, defaulting to start at level 1
  strength_level = models.IntegerField(default=1)
  dexterity_level = models.IntegerField(default=1)
  spirit_level = models.IntegerField(default=1)
  intellect_level = models.IntegerField(default=1)
  charm_level = models.IntegerField(default=1)

  #Experience values for each stat, default exp starts at 0
  strength_exp = models.IntegerField(default=0)
  dexterity_exp = models.IntegerField(default=0)
  spirit_exp = models.IntegerField(default=0)
  intellect_exp = models.IntegerField(default=0)
  charm_exp = models.IntegerField(default=0)

  #Bool for whether or not tutorial has been completed, defaulting to false
  tutorial_completed = models.BooleanField(default=False)

  #Title selector, by default accounts have unlocked no titles.
  title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True, default=None)

  #Profile Picture url, by default no picture is chosen
  profile_picture_url = models.CharField(default=None, max_length=100)

  #Credits value, by default a user does not have any credits
  credits_owned = models.IntegerField(default=0)

  #Boss damage for raidboss fight, users will gain boss damage during a raidboss fight. Resets after boss fight ends.
  boss_damage = models.IntegerField(default=0)

  #Prestige values for users who max out a stat(level 10) and continue to do tasks under that stat.
  prestige_exp = models.IntegerField(default=0)
  prestige_level = models.IntegerField(default=0)


  class Meta:
    verbose_name = ("User")
    verbose_name_plural = ("Users")

  def __str__(self):
    return self.name