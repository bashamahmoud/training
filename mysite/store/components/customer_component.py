import json

from ..repos.customer_repo import CustomerRepo
from ..serializers import DefaultCustomerSerializer


class CustomerComponent:
    def __init__(self):
        self.customer_repo = CustomerRepo

    def get_customer(self, pk=None):
        customers = self.customer_repo.get_customers(pk)
        if customers and pk:
            serializer = DefaultCustomerSerializer(customers)
            return serializer.data
        else:
            serializer = DefaultCustomerSerializer(customers, many=True)
            return serializer.data

    def register_customer(self, request):
        serializer = DefaultCustomerSerializer(data=request.data)
        customers = self.customer_repo.register_customer(serializer)
        return customers

    def delete_customer(self, pk=None):
        customers = self.customer_repo.delete_customer(pk=pk)
        return customers

    def update_customer(self, request, pk=None):
        request_data = json.loads(request.body)
        get_updated_customer = self.customer_repo.update_customer(request_data, pk)

        return get_updated_customer
