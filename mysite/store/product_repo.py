import json
import logging

from rest_framework.views import exception_handler

from .models import Product

logger = logging.getLogger('store')


class ProductRepo:
    @staticmethod
    def create_product(product):
        try:
            product.is_valid()
            return product.save()
        except Exception as e:
            logger.error(f"Error creating product: {e}")
            return exception_handler(e, "Product")

    @staticmethod
    def get_product(pk=None):
        try:
            if pk:
                return Product.objects.get(pk=pk)
            else:
                return Product.objects.all()
        except Exception as e:
            logger.error(f"Error retrieving product : {e}")
            return exception_handler(e, "Product")

    @staticmethod
    def delete_product(pk=None):
        try:
            products = Product.objects.get(pk=pk)
            products.delete()
            return True
        except Exception as e:
            logger.error(f"Error deleting product: {e}")

            return exception_handler(e, "Product")

    @staticmethod
    def update_product(request, pk=None):
        request_data = json.loads(request.body)
        try:
            return Product.objects.filter(pk=pk).update(**request_data)

        except Exception as e:
            logger.error(f"Error updating product: {e}")
            return exception_handler(e, "product")
