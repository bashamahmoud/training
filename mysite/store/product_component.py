from .product_repo import ProductRepo


class ProductComponent:
    def __init__(self):
        self.product_repo = ProductRepo()

    def create_product(self, request):
        product = self.product_repo.create_product(request)
        return product
