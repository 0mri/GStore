from django.contrib import admin
from .models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
