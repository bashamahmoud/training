from django.contrib import admin

from .models import Admin, Customer, Cart, Product, CartProduct

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartProduct)
