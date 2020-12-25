from django.db import models
from .product import Product
from .product_group import ProductGroup
from .stash_location import StashLocation


class StashSetting(models.Model):
    name = models.CharField(max_length=200)
    stash_location = models.ForeignKey(StashLocation, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT, null=True, blank=True)
