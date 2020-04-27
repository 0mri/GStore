from django.urls import path, include
# from rest_framework.routers import DefaultRouter


from backend.api.product.api.views import ProductList, ProductDetail, CategoryList, CategoryDetail

# router = DefaultRouter()
# router.register("", ProductList)

urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<slug>', CategoryDetail.as_view(), name='category-detail'),
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<slug>/', ProductDetail.as_view(), name='product-detail'),

]
