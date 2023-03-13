import json

from rest_framework.views import exception_handler

from .models import Product


class ProductRepo:
    @staticmethod
    def create_product(request):
        try:

            product = Product(name=request.POST["name"],
                              description=request.POST["description"],
                              price=request.POST["price"],
                              in_invetory=request.POST["in_inventory"], )
            product.save()
        except Exception as e:
            exception_handler(e, "Product")
