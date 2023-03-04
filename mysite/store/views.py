from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer


class CustomerView(ModelViewSet):  # using a viewset insted of view
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # POST request: http://127.0.0.1:8000/store/customers/
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Customer updated successfully'}, status=status.HTTP_201_CREATED, headers=headers)

    # PUT request: http://127.0.0.1:8000/store/customers/{pk}/
    def update(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(customer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Customer updated successfully'})

    # DELETE request: http://127.0.0.1:8000/store/customers/{pk}/
    def destroy(self, request, pk=None):
        customer = self.get_object()
        customer.delete()
        return Response({'message': 'Customer deleted successfully'})

    # GET request: http://127.0.0.1:8000/store/customers/
    # GET request: http://127.0.0.1:8000/store/customers/{pk}/
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
