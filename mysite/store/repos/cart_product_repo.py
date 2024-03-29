import json
import logging

from rest_framework.views import exception_handler

from ..models import CartProduct, Product
from .product_repo import ProductRepo

logger = logging.getLogger('store')


class CartProductRepo:
    @staticmethod
    def get_cart_products(cart_pk=None, pk=None):
        try:
            if not pk:
                cart_products = CartProduct.objects.filter(cart_id=cart_pk).prefetch_related()
            else:
                cart_products = CartProduct.objects.filter(cart_id=cart_pk, product_id=pk).prefetch_related()
            return cart_products
        except Exception as e:
            logger.error(f"Error retrieving cart: {e}")
            return exception_handler(e, "Cart product")

    @staticmethod
    def create_cart_product(cart_product,product_id,cart_pk):
        try:
            cart_product.is_valid()
            return cart_product.save(product_id=product_id,cart_id=cart_pk)
        except Exception as e:
            logger.error(f"Error creating cart product: {e}")
            return exception_handler(e, "Cart product")

    @staticmethod
    def delete_cart_product(cart_pk=None, pk=None):
        try:
            cart_product = CartProduct.objects.filter(cart_id=cart_pk, product=pk).first()
            return cart_product.delete()
        except Exception as e:
            logger.error(f"Error deleting cart product: {e}")
            return exception_handler(e, "Cart product")

    @staticmethod
    def update_cart_product(request, cart_pk=None, pk=None):
        request_data = json.loads(request.body)
        try:
            return CartProduct.objects.filter(cart_id=cart_pk, product=pk).update(quantity=request_data.get('quantity'))

        except Exception as e:
            logger.error(f"Error updating Cart product: {e}")
            return exception_handler(e, "Cart product")
