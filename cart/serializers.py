from rest_framework import serializers
from cart import models
from product.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer( read_only = True)

    class Meta :
        model = models.Cart
        exclude = ['userId','created_at','updated_at']