from django.urls import path, include
from .views import ListOrderView,DetailOrderView

urlpatterns = [
    path('order/', ListOrderView.as_view(), name='order-list'),
    path('order/<pk>', DetailOrderView.as_view(), name='order-detail'),
    # path('cart/<>', CartItemList.as_view(), name='cart-list'),
    # path('cart/add', AddToCart.as_view(), name='cart-add'),
    # path('cart/<owner__username>', DetailCartView.as_view(), name='cart-detail'),


]
