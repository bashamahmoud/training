from .product_repo import ProductRepo
from .serializers import ProductSerializer


class ProductComponent:
    def __init__(self):
        self.product_repo = ProductRepo()

    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        product = self.product_repo.create_product(serializer)
        return product

    def get_product(self, pk=None):
        products = self.product_repo.get_product(pk)
        if products and pk:
            serializer = ProductSerializer(products)

        else:
            serializer = ProductSerializer(products, many=True)

        return serializer.data

    def delete_product(self, pk=None):
        product = self.product_repo.delete_product(pk)
        return product

    def update_product(self, request, pk=None):
        updated_product = self.product_repo.update_product(request, pk)

        return updated_product
