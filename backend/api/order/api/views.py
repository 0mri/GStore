from rest_framework import generics
from backend.api.order.models import Order, OrderItem
from backend.api.product.models import Product
from .serializers import OrderSerializer, DetailOrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from backend.account.permissions import IsOwner


class ListOrderView(generics.ListAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)


class DetailOrderView(generics.RetrieveAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = DetailOrderSerializer
    queryset = Order.objects.all()

    # def perform_create(self, serializer):
    #     user = None
    #     if self.request and hasattr(self.request, "user"):
    #         user = self.request.user
    #     product = Product.objects.all().first()
    #     pk = self.kwargs['pk']
    #     print(pk)

    #     serializer.save(owner=user, order_total=4)


# class DetailCartView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwner, IsAuthenticated]
#     serializer_class = CartSerializer
#     queryset = Cart.objects.all()
#     lookup_field = 'owner__username'

# class AddToCart(generics.CreateAPIView):
#     permission_classes = [IsOwner, IsAuthenticated]
#     serializer_class = CartItemSerializer
#     # queryset = CartItem.objects.all()
#     lookup_field = ''
#     # def get_queryset(self):
#     #     return Cart.objects.get(owner=self.request.user)

#     def perform_create(self,serializer):
#         serializer.save(user=self.request.user)
