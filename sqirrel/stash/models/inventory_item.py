from django.db import models
from .product import Product
from .stash_location import StashLocation


class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False)
    stash_location = models.ForeignKey(StashLocation, on_delete=models.CASCADE, null=False, blank=False)
