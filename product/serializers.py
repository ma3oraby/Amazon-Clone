##form
from rest_framework import serializers
from .models import Product , Brand , ProductReview


class BrandSerializer (serializers.ModelSerializer):
    class Meta : 
        model = Brand
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class   Meta : 
        model = ProductReview
        fields = ['user','rate','review','date']


class ProductListSerializers (serializers.ModelSerializer):
    #brand = BrandSerializer() ##all brand detail 
    brand = serializers.StringRelatedField() ###brand name only 
    class Meta :
        model = Product
        fields = '__all__'


class ProductDetailSerializers (serializers.ModelSerializer):
    brand = serializers.StringRelatedField() ###brand name only 
    reviews = ProductReviewSerializer(source='product_review',many=True)
    class Meta :
        model = Product
        fields = '__all__'
        

