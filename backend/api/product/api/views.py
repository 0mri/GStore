from rest_framework import generics, mixins, permissions
from backend.api.product.models import Product, Category
from .serializers import ProductSerializer, DetialedProductSerializer, CategorySerialiser, DetailCategorySerialiser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import filters
# class ProductList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class CategoryList(generics.ListAPIView,):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiser
    permission_classes = [permissions.AllowAny]


class CategoryDetail(generics.RetrieveAPIView):
    # queryset = Category.objects.all()
    serializer_class = DetailCategorySerialiser
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        cat_obj = Category.objects.all()
        return cat_obj
        # queryset = Product.objects.filter(category=self.category)
        # return (queryset)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = DetialedProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = ('slug')


class StandardResultsSetPagination(LimitOffsetPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 8

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })


class CustomSearchFilter(filters.SearchFilter):
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.all(age=search_term_as_int)
        return queryset, use_distinct


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination
    filter_backends = [CustomSearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        if category and category != 'all':
            return Product.objects.all().filter(category__slug=category)
        return Product.objects.all()

    # def get(self,request):
    #     serializer = ProductSerializer(context={'request': self.request})
    #     Response('as')

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)
