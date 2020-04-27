from django.urls import path, include
from backend.account.api.views import token_obtain_pair

urlpatterns = [
    # comments
    path('comment/', include('backend.api.comment.api.urls')),

    # authentication
    path('auth/', include('djoser.urls')),
    path('auth/jwt/create', token_obtain_pair, name='token_create'),
    path('auth/', include('djoser.urls.jwt')),
    # # order
    path('', include('backend.api.order.api.urls')),
    # # product
    path('', include('backend.api.product.api.urls')),
    # # payment
    path('payment/', include('backend.api.payment.api.urls'))

]
