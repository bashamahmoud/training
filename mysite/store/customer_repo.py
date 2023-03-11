
from .models import Customer
from rest_framework.views import exception_handler


class CustomerRepo:
    @staticmethod
    def get_customers(pk=None):
        try:
            if pk:
                customer = Customer.objects.get(pk=pk)
                return customer
            else:
                return Customer.objects.all()
        except Exception as e:
            return exception_handler(e, "error")

    @staticmethod
    def register_customer(customer):
        try:
            customer.save()
        except Exception as e:
            return exception_handler(e, "error")

    @staticmethod
    def delete_customer(pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()
            return True
        except Exception as e:
            return exception_handler(e, "error")

    @staticmethod
    def update_customer(request_data, pk=None):
        try:
            Customer.objects.filter(pk=pk).update(**request_data)
            return True
        except Exception as e:
            return exception_handler(e, "error")
