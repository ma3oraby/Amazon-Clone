###view
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Product ,Brand
from .serializers import ProductListSerializers , ProductDetailSerializers ,BrandSerializer , BrandDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .mypagination import ProductPagination
from rest_framework import filters





@api_view(['GET'])
def product_list_api (request):
    query = Product.objects.all()[:20]
    data = ProductListSerializers(query,many=True).data
    return Response({'data':data})

class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name', 'brand','price']
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name', 'brand']
    ordering_fields = ['price', 'brand']

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()
    lookup_field = 'slug'

class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'