from ..repos.cart_product_repo import CartProductRepo
from ..serializers import CartProductSerializer


class CartProductComponent:
    def __init__(self):
        self.cart_product_repo = CartProductRepo()

    def get_cart_product(self, cart_pk=None, pk=None):
        products = self.cart_product_repo.get_cart_products(cart_pk=cart_pk, pk=pk)
        if not pk:
            serializer = CartProductSerializer(products, many=True)

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
    def create_cart_product(self, request, cart_pk=None):
        request.data['cart'] = cart_pk
        serializer = CartProductSerializer(data=request.data)
        cart = self.cart_product_repo.create_cart_product(serializer)
        return cart

    def delete_cart_product(self,cart_pk=None, pk=None):
        cart_product= self.cart_product_repo.delete_cart_product(cart_pk=cart_pk,pk=pk)
        return cart_product

    def update_cart_product(self, request, cart_pk=None, pk=None):
        updated_cart = self.cart_product_repo.update_cart_product(request, cart_pk=cart_pk, pk=pk)

        return updated_cart

