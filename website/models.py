from django.db import models

class Item(models.Model):
    itemId = models.CharField(max_length=50)
    available = models.BooleanField()
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    price = models.BigIntegerField()
    priceType = models.CharField(max_length=50)
    defaultTaxRates = models.BooleanField()
    stockCount = models.IntegerField()
    modifiedTime = models.BigIntegerField()
    colorCode = models.CharField(max_length=50)

    def __str__(self):
      return f"{self.name}"