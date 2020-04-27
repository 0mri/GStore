from rest_framework import serializers
from decimal import Decimal
from backend.api.order.models import Order, OrderItem
from backend.api.product.models import Product
from backend.api.product.api.serializers import DetialedProductSerializer, ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = DetialedProductSerializer(
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    products = serializers.ListField(write_only=True)

    class Meta:
        model = Order
        fields = ['url', 'id', 'owner', 'status',
                  'order_total', 'address', 'created_at', 'products']
        read_only_fields = ['owner']

    def calc_amount(self, products):
        order_total = 0
        for product in products:
            prod = Product.objects.get(id=product['id']).price

            order_total += Decimal(prod * int(product['quantity']))

        return order_total

    def get_num_of_items(self, obj):
        return obj.cartitem_set.all().count()

    def validate_products(self, data):
        if len(data) == 0:
            raise serializers.ValidationError("Can't order empty cart")

        try:
            for d in data:
                d['id']
                d['quantity']
            return data
        except:
            raise serializers.ValidationError("Incorrct type of list")

    def create(self, validated_data):
        new_order = Order.objects.create(
            owner=self.context.get('request').user,
            **validated_data
        )
        # new_order = Order.objects.create(
        #     **validated_data
        # )
        # print(new_order)
        return new_order


class DetailOrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(read_only=True, many=True)
    owner = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'owner', 'orderitem_set', 'status',
                  'order_total', 'address', 'created_at']
        read_only_fields = ['owner', 'status', 'order_total', 'orderitem_set']

    def get_num_of_items(self, obj):
        return obj.cartitem_set.all().count()
