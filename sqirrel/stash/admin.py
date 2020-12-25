from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Facility, InventoryItem, Product, ProductGroup, StashLocation, User

admin.site.register(Facility)
admin.site.register(InventoryItem)
admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(StashLocation)
admin.site.register(User, UserAdmin)
