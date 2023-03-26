from .cart_repo import CartRepo
from .serializers import CartSerializer


class CartComponent:
    def __init__(self):
        self.cart_repo = CartRepo()

    def create_cart(self, request):
        serializer = CartSerializer(data=request.data)
        cart = self.cart_repo.create_cart(serializer)
        return cart

    def get_cart(self, pk=None):
        carts = self.cart_repo.get_cart(pk)
        if carts and pk:
            serializer = CartSerializer(carts)

        else:
            serializer = CartSerializer(carts, many=True)

        return serializer.data

    def delete_cart(self, pk=None):
        cart = self.cart_repo.delete_cart(pk)
        return cart

    def update_cart(self, request, pk=None):
        updated_cart = self.cart_repo.update_cart(request, pk)

        return updated_cart
