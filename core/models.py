from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

class Platform(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.FloatField()