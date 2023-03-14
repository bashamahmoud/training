
from .product_repo import ProductRepo


class ProductComponent:
    def __init__(self):
        self.product_repo = ProductRepo()

    def create_product(self, request):
        product = self.product_repo.create_product(request)
        return product

    def get_product(self, pk=None):
        products = self.product_repo.get_product(pk)
        return products

    def delete_product(self, pk=None):
        product = self.product_repo.delete_product(pk)
        return product

    def update_product(self, request, pk=None):
        updated_product = self.product_repo.update_product(request, pk)

        return updated_product
