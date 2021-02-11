from rest_framework import serializers
from .models import ProductModel, Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id','name','brand','category']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','brand','category']