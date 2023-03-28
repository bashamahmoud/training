from ..repos.cart_product_repo import CartProductRepo
from ..serializers import CartProductSerializer


class CartProductComponent:
    def __init__(self):
        self.cart_product_repo = CartProductRepo()

    # def create_cart(self, request):
    #     serializer = CartProductSerializer(data=request.data)
    #     cart = self.cart_product_repo.create_cart(serializer)
    #     return cart

    def get_cart_product(self, cart_pk=None, pk=None):
        products = self.cart_product_repo.get_cart_products(cart_pk=cart_pk, pk=pk)
        if not pk:
            serializer = CartProductSerializer(products)

        else:
            serializer = CartProductSerializer(products, many=True)

        return serializer.data

    # def delete_cart(self, pk=None):
    #     cart = self.cart_product_repo.delete_cart(pk)
    #     return cart
    #
    # def update_cart(self, request, pk=None):
    #     updated_cart = self.cart_product_repo.update_cart(request, pk)
    #
    #     return updated_cart
