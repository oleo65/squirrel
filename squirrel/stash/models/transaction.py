from django.db import models
from django.utils.timezone import now

from .product import Product
from .stash_location import StashLocation
from .user_custom import User


class Transaction(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    stash_location = models.ForeignKey(StashLocation, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=False, blank=False, default=now)
    amount = models.DecimalField(null=False, blank=False, max_digits=15, decimal_places=3)
