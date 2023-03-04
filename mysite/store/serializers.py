from rest_framework import serializers
from .models import Customer


# using serializers for viewset
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'address', 'phone', 'credit_card']
        read_only_fields = ["id"]  # set id to read only
        extra_kwargs = {
            'password': {'write_only': True},
        }
