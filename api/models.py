from django.db import models


class Collection(models.Model):
    collection = models.CharField(max_length=10, primary_key=True)


class Product(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.CharField(max_length=100, blank=True, default='')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField()


