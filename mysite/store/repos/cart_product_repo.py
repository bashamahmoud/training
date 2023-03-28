from ..models import CartProduct


class CartProductRepo:
    @staticmethod
    def get_cart_products(cart_pk=None, pk=None):
        if not pk:
            cart_products = CartProduct.objects.filter(cart_id=cart_pk)
        else:
            cart = CartProduct.objects.filter(cart_id=cart_pk)
            cart_products = cart.products.filter(pk=pk)
        return cart_products
