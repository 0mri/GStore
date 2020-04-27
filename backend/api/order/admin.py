from django.contrib import admin
from .models import Order, OrderItem

# admin.site.register(Cart)
# admin.site.register(CartItem)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['order_total']


admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)
