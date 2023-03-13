from rest_framework import serializers

from .models import Customer


# using serializers for viewset
class DefaultCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'address', 'phone', 'credit_card']
        read_only_fields = ["id"]  # set id to read only
        extra_kwargs = {
            'password': {'write_only': True},
        }


# for Update method
class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'address', 'phone', 'credit_card']
        read_only_fields = ["id", "email", "password"]  # set id to read only

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class CartSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = Cart
#         fields = '__all__'
