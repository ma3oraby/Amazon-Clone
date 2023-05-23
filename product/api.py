###view
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductListSerializers , ProductDetailSerializers ,BrandSerializer

@api_view(['GET'])
def product_list_api (request):
    query = Product.objects.all()[:20]
    data = ProductListSerializers(query,many=True).data
    return Response({'data':data})

class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()[:20]

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()
    lookup_field = 'slug'