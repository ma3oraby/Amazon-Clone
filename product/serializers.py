##form
from rest_framework import serializers
from .models import Product , Brand , ProductReview , ProductImages

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductImages 
        fields = ['image']


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
    price_with_tax = serializers.SerializerMethodField()
    class Meta :
        model = Product
        fields = '__all__'

    def get_price_with_tax (self,product):
        return product.price*1.1


class ProductDetailSerializers (serializers.ModelSerializer):
    brand = serializers.StringRelatedField() ###brand name only 
    reviews = ProductReviewSerializer(source='product_review',many=True)
    images = ProductImageSerializer(source='product_images',many=True)
    class Meta :
        model = Product
        fields = '__all__'
        

class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializers(source='product_brand',many=True)
    class Meta : 
        model = Brand
        fields = '__all__'