from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserGroup, Product, ProductGroup

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(UserGroup)
admin.site.register(Product)
admin.site.register(ProductGroup)
