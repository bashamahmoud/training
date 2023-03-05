from django.urls import path, include
from rest_framework import routers

from .views import CustomerView

router = routers.SimpleRouter()  # simple router
router.register(r'customers', CustomerView, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
