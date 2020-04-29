from django.contrib import admin
from .models import Product,Category, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]


# admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]
    inlines = [ProductImageAdmin]

admin.site.register(Product, ProductAdmin)
# @admin.register(Product, ProductAdmin)
# # class ProductAdmin(admin.ModelAdmin):
# #     inlines = [ProductImageAdmin]

# @admin.register(CaseFile)
# class CaseFileAdmin(admin.ModelAdmin):
#     pass