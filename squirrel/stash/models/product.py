from django.db import models
from .product_group import ProductGroup


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    product_group = models.ManyToManyField(ProductGroup, blank=False)
