from ..repos.cart_product_repo import CartProductRepo
from ..serializers import CartProductSerializer


class CartProductComponent:
    def __init__(self):
        self.cart_product_repo = CartProductRepo()

    def get_cart_product(self, cart_pk=None, pk=None):
        products = self.cart_product_repo.get_cart_products(cart_pk=cart_pk, pk=pk)
        serializer = CartProductSerializer(products, many=True)
        return serializer.data

    def create_cart_product(self, request, cart_pk=None):
        product_id = request.data["product"]
        serializer = CartProductSerializer(data=request.data)
        cart = self.cart_product_repo.create_cart_product(serializer, product_id, cart_pk)
        return cart

    def delete_cart_product(self, cart_pk=None, pk=None):
        cart_product = self.cart_product_repo.delete_cart_product(cart_pk=cart_pk, pk=pk)
        return cart_product

    def update_cart_product(self, request, cart_pk=None, pk=None):
        updated_cart = self.cart_product_repo.update_cart_product(request, cart_pk=cart_pk, pk=pk)

        return updated_cart
