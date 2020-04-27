from django.urls import path, include
from .views import make_payment, get_client_token

urlpatterns = [
    path('checkout/new', get_client_token),
    path('checkout/', make_payment),
]
