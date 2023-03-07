from django.urls import path, include
from rest_framework import routers

from . import customer_view

router = routers.SimpleRouter()  # simple router
router.register(r'customers', customer_view.CustomerView, basename='customer')
# router.register(r'products', productView.ProductView, basename='product')
# router.register(r'cart', cartView.CartView, basename='cart')
print(router.get_urls())
urlpatterns = [
    path('', include(router.urls)),
]
