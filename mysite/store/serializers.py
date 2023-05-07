from rest_framework import serializers

from .models import Customer, Product, Cart, CartProduct


# using serializers for viewset
class DefaultCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'address', 'phone', 'credit_card']
        read_only_fields = ["id"]  # set id to read only
        extra_kwargs = {
            'password': {'write_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'in_inventory']


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer_id', 'products']


class CartProductSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ['id', 'quantity', 'cart', 'product']
