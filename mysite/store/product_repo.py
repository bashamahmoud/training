import json

from django.forms import model_to_dict
from rest_framework.views import exception_handler
import logging

logger = logging.getLogger('store')

from .models import Product


class ProductRepo:
    @staticmethod
    def create_product(request):
        try:

            product = Product(name=request.data.get("name"),
                              description=request.data.get("description"),
                              price=int(request.data.get("price")),
                              in_inventory=int(request.data.get("in_inventory"))
                              )
            product.save()
            return request
        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            return exception_handler(e, "Product")

    @staticmethod
    def get_product(pk=None):
        try:
            if pk:
                products = model_to_dict(Product.objects.get(pk=pk))

            else:
                products = list(Product.objects.all().values())
            return products
        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            return exception_handler(e, "Product")

    @staticmethod
    def delete_product(pk=None):
        try:
            products = Product.objects.get(pk=pk)
            products.delete()
            return True
        except Exception as e:
            logger.error(f"Error updating customer: {e}")

            return exception_handler(e, "Product")

    @staticmethod
    def update_product(request, pk=None):
        request_data = json.loads(request.body)
        try:
            return Product.objects.filter(pk=pk).update(**request_data)

        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            return exception_handler(e, "error")
