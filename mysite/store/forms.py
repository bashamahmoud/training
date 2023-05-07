from django import forms

from .models import Customer, Product, Cart, CartProduct


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'address', 'phone', 'credit_card']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CartForm(forms.ModelForm):
    products = ProductForm()

    class Meta:
        model = Cart
        fields = '__all__'


class CartProductForm(forms.ModelForm):
    products = ProductForm()
    cart=CartForm()

    class Meta:
        model = CartProduct
        fields = '__all__'
