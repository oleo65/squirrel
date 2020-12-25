from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Facility, Product, ProductGroup

# Register your models here.

admin.site.register(Facility)
admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(User, UserAdmin)
