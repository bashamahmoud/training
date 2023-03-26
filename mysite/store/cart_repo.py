import json
import logging

from rest_framework.views import exception_handler

from .models import Cart

logger = logging.getLogger('store')


class CartRepo:
    @staticmethod
    def create_cart(cart):
        try:
            cart.is_valid()
            return cart.save()
        except Exception as e:
            logger.error(f"Error creating cart: {e}")
            return exception_handler(e, "Cart")

    @staticmethod
    def get_cart(pk=None):
        try:
            if pk:
                return Cart.objects.get(pk=pk)
            else:
                return Cart.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving Cart : {e}")
            return exception_handler(e, "Cart")

    @staticmethod
    def delete_cart(pk=None):
        try:
            cart = Cart.objects.get(pk=pk)
            cart.delete()
            return True
        except Exception as e:
            logger.error(f"Error deleting Cart: {e}")

            return exception_handler(e, "Cart")

    @staticmethod
    def update_cart(request, pk=None):
        request_data = json.loads(request.body)
        try:
            return Cart.objects.filter(pk=pk).update(**request_data)

        except Exception as e:
            logger.error(f"Error updating Cart: {e}")
            return exception_handler(e, "Cart")
