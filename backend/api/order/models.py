import random
from decimal import Decimal
from django.db import models
from django.conf import settings
from backend.api.product.models import Product
from django.db.models.signals import pre_save, post_save, post_delete
# User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
User = get_user_model()


# class CartItem(models.Model):
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     line_item_total = models.DecimalField(
#         max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return '{} - {}'.format(self.product.name, self.quantity)

#     @property
#     def get_price(self):
#         return self.product.price * self.quantity


# def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
#     qty = instance.quantity
#     if qty >= 1:
#         price = instance.product.price
#         line_item_total = Decimal(qty) * Decimal(price)
#         instance.line_item_total = line_item_total


# pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)


# def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
#     instance.cart.update_subtotal()


# post_save.connect(cart_item_post_save_receiver, sender=CartItem)

# post_delete.connect(cart_item_post_save_receiver, sender=CartItem)


# class Cart(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     num_of_items = models.PositiveIntegerField(default=0)
#     # items = models.ManyToManyField('CartItem')
#     total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '{id} - {name}`s cart -- {price}$'.format(id=self.id, name=self.owner.username, price=self.total)

#     @classmethod
#     def create(cls, owner):
#         # self.owner = owner
#         cart = cls(owner=owner)
#         cart.save()
#         return cart

#     def update_subtotal(self):
#         # print "updating..."
#         subtotal = 0
#         items = self.cartitem_set.all()
#         self.num_of_items = self.cartitem_set.all().count()
#         for item in items:
#             subtotal += item.line_item_total
#         self.total = "%.2f" % (subtotal)
#         self.save()


class OrderItemManager(models.Manager):
    def create(self, *args, **kwargs):
        product_id = kwargs['id']
        quantity = kwargs['quantity']
        cur_product = Product.objects.get(id=product_id)
        t_price = Decimal(cur_product.price) * Decimal(quantity)

        order_itemed = super(OrderItemManager, self).create(
            order=kwargs['order'], product=cur_product, line_item_total=t_price, quantity=quantity)

        return order_itemed.order_item()


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    line_item_total = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.quantity)

    def order_item(self):
        self.product.quantity_avialable -= int(self.quantity)
        return self.product.save()

    objects = OrderItemManager()


class OrderManager(models.Manager):

    def create(self, *args, **kwargs):

        # omri = User.objects.get(id=1)
        order_total = kwargs.get('order_total')

        order = super(OrderManager, self).create(
            owner=kwargs['owner'],
            address=kwargs['address'],
            status=kwargs['status'],
            order_total=order_total
        )

        products = kwargs.get('products', [])
        for product in products:
            order_itemed = OrderItem.objects.create(
                order=order,
                id=product['id'],
                quantity=product['quantity']
            )

        order.save()
        return order


def get_unique_id():
    unique_id = random.randint(1000, 10000)

    # is_order = OrderManager.get(order_id=unique_id).count()
    # while(is_order == 1):
    #     unique_id = random.randint(0, 10000)
    return unique_id


class Order(models.Model):
    # order_id = models.CharField(
    #     max_length=200, unique=False,
    #     default=0
    # )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('refunded', 'Refunded'),
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
    )
    order_total = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrderManager()

    def __str__(self):
        return '{} {}`s order - {}$ - {}'.format(self.id, self.owner.username, self.order_total, self.status)
