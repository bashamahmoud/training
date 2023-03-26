from django.urls import path, include
from rest_framework import routers

from . import customer_view, product_view, cart_view

router = routers.SimpleRouter(trailing_slash=False)  # simple router
router.register(r'customers', customer_view.CustomerView, basename='customer')
router.register(r'products', product_view.ProductView, basename='product')
router.register(r'cart', cart_view.CartView, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
