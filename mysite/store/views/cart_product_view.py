from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from ..components.cart_product_component import CartProductComponent
from ..forms import CartProductForm


class CartProductView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart_product_component = CartProductComponent()

        # GET request: /store/cart/{cart_id}/products  #get all carts products

    def list(self, request, cart_pk=None):
        products = self.cart_product_component.get_cart_product(cart_pk=cart_pk)
        if not products:
            return JsonResponse({'error': 'Error while retrieving products of cart'}, safe=False, status=404)

        return render(request, 'cart_product/list.html', {'cart_products': products})

        # GET request: /store/carts/{cart_id}/products/{pk}  #get cart product of given id

    def retrieve(self, request, cart_pk=None, pk=None):
        carts = self.cart_product_component.get_cart_product(cart_pk=cart_pk, pk=pk)
        if not carts:
            return JsonResponse({'error': 'Error while retrieving cart'}, safe=False, status=404)

        return render(request, 'cart_product/retrieve.html', {'cart_product': carts})

        # POST request: /store/carts/{cart_id}/products #create new cart product

    def create(self, request, cart_pk=None):
        cart = self.cart_product_component.create_cart_product(request, cart_pk=cart_pk)
        if cart:
            return JsonResponse("server: cart product added successfully", safe=False, status=201)
        return JsonResponse("server: failed to add product to cart", safe=False)

    #     # DELETE request: /store/carts/{cart_id}/products/{pk} #delete cart product

    def destroy(self, request, cart_pk=None, pk=None):
        cart = self.cart_product_component.delete_cart_product(cart_pk=cart_pk, pk=pk)
        if cart:
            return JsonResponse("server: cart successfully deleted", safe=False, status=200)
        return JsonResponse("server: Error happened while deleting cart", safe=False)

    #     # PUT request: /store/carts/{cart_id}/products/{pk} #update cart product of given id

    def update(self, request, cart_pk=None, pk=None):
        updated_cart = self.cart_product_component.update_cart_product(request, cart_pk=cart_pk, pk=pk)
        if updated_cart:
            return JsonResponse({'server': 'cart successfully updated'})
        return JsonResponse({'error': 'Error while updating cart'})

    @action(detail=False, methods=['GET'])
    def create_cart_product(self, request, cart_pk=None):
        form = CartProductForm()
        context = {'form': form, 'cart_pk': cart_pk}
        return render(request, 'cart_product/create.html', context)
