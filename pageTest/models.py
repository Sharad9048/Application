from django.db import models

# Create your models here.

class Inventory(models.Model):
    itemName = models.CharField(max_length = 255)
    quantitySize = models.IntegerField()
    stock = models.IntegerField()


