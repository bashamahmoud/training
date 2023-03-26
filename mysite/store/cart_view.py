from django.http import JsonResponse
from rest_framework import viewsets

from .cart_component import CartComponent


class CartView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart_component = CartComponent()

    # GET request: /store/carts  #get all carts
    def list(self, request):
        carts = self.cart_component.get_cart()
        if not carts:
            return JsonResponse({'error': 'Error while retrieving carts list'}, safe=False, status=404)

        return JsonResponse(carts, safe=False)

    # GET request: /store/carts/{pk}  #get cart of given id
    def retrieve(self, request, pk=None):
        carts = self.cart_component.get_cart(pk)
        if not carts:
            return JsonResponse({'error': 'Error while retrieving cart'}, safe=False, status=404)

        return JsonResponse(carts, safe=False)

    # POST request: /store/carts #create new cart
    def create(self, request):
        cart = self.cart_component.create_cart(request)
        if cart:
            return JsonResponse("server: cart created successfully", safe=False, status=201)
        return JsonResponse("server: failed to creat cart", safe=False)

    # DELETE request: /store/carts/{pk} #delete cart of given id
    def destroy(self, request, pk=None):
        cart = self.cart_component.delete_cart(pk)
        if cart:
            return JsonResponse("server: cart successfully deleted", safe=False, status=200)
        return JsonResponse("server: Error happened while deleting cart", safe=False)

    # PUT request: /store/carts/{pk} #update cart of given id
    def update(self, request, pk=None):
        updated_cart = self.cart_component.update_cart(request, pk)
        if updated_cart:
            return JsonResponse({'server': 'cart successfully updated'})
        return JsonResponse({'error': 'Error while updating cart'})
