from django.http import JsonResponse
from rest_framework import viewsets

from .product_component import ProductComponent


class ProductView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_component = ProductComponent()

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        product = self.product_component.create_product(request)
        if product:
            return JsonResponse("server: product created successfully")
        return JsonResponse("server: failed to creat product")


    def destroy(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass
