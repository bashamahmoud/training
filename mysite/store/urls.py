from django.urls import path, include
from rest_framework import routers

from .views import CustomerView

router = routers.SimpleRouter()
router.register(r'customers', CustomerView, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
