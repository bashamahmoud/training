import json

from rest_framework.views import exception_handler

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
            exception_handler(e, "Product")
