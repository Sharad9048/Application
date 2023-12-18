from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserCatogory(models.Model):
    class catogories(models.TextChoices):
        storeBusiness = "SB", _("Store Business")
        distributer = "DB", _("Distributer")
        dispatcher = "DP", _("Dispatcher")
        producer = "PD", _("Producer")
    uid = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    userCatogory = models.IntegerField(choices = catogories)
