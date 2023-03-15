import logging

from rest_framework.views import exception_handler

from .models import Customer

logger = logging.getLogger('store')


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
            logger.error(f"Error getting customers: {e}")
            return exception_handler(e, "error")

    @staticmethod
    def register_customer(customer):
        try:
            customer.is_valid()
            return customer.save()
        except Exception as e:
            logger.error(f"Error registering customer: {e}")
            return exception_handler(e, "error")

    @staticmethod
    def delete_customer(pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()
            return True
        except Exception as e:
            logger.error(f"Error deleting customer: {e}")
            return exception_handler(e, "error")

    @staticmethod
    def update_customer(request_data, pk=None):
        try:
            return Customer.objects.filter(pk=pk).update(**request_data)

        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            return exception_handler(e, "error")
