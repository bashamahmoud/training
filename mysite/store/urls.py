from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views import cart_view, product_view, cart_product_view, customer_view

router = routers.SimpleRouter(trailing_slash=False)  # simple router
router.register(r'customers', customer_view.CustomerView, basename='customer')
router.register(r'products', product_view.ProductView, basename='product')
router.register(r'cart', cart_view.CartView, basename='cart')
cart_router = nested_routers.NestedSimpleRouter(router, r'cart', lookup='cart')
cart_router.register(r'products', cart_product_view.CartProductView, basename='cart-product')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
]
