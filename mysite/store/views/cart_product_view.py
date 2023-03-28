from rest_framework import viewsets
from django.http import JsonResponse

from ..components.cart_product_component import CartProductComponent


class CartProductView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart_product_component = CartProductComponent()

        # GET request: /store/carts  #get all carts

    def list(self, request,cart_pk=None):
        products = self.cart_product_component.get_cart_product(cart_pk=cart_pk)
        if not products:
            return JsonResponse({'error': 'Error while retrieving products of cart'}, safe=False, status=404)

        return JsonResponse(products, safe=False)

        # GET request: /store/carts/{pk}  #get cart of given id

    def retrieve(self, request, pk=None):
        carts = self.cart_product_component.get_cart_product(pk=None)
        if not carts:
            return JsonResponse({'error': 'Error while retrieving cart'}, safe=False, status=404)

        return JsonResponse(carts, safe=False)

        # POST request: /store/carts #create new cart

    # def create(self, request):
    #     cart = self.cart_product_component.create_cart_product(request)
    #     if cart:
    #         return JsonResponse("server: cart created successfully", safe=False, status=201)
    #     return JsonResponse("server: failed to creat cart", safe=False)
    #
    #     # DELETE request: /store/carts/{pk} #delete cart of given id
    #
    # def destroy(self, request, pk=None):
    #     cart = self.cart_component.delete_cart(pk)
    #     if cart:
    #         return JsonResponse("server: cart successfully deleted", safe=False, status=200)
    #     return JsonResponse("server: Error happened while deleting cart", safe=False)
    #
    #     # PUT request: /store/carts/{pk} #update cart of given id
    #
    # def update(self, request, pk=None):
    #     updated_cart = self.cart_component.update_cart(request, pk)
    #     if updated_cart:
    #         return JsonResponse({'server': 'cart successfully updated'})
    #     return JsonResponse({'error': 'Error while updating cart'})
