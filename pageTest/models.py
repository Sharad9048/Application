from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Inventory(models.Model):
    itemName = models.CharField(max_length = 255)
    quantitySize = models.IntegerField()
    stock = models.IntegerField()
    userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)