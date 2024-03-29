from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from ..components.product_component import ProductComponent
from ..forms import ProductForm


class ProductView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_component = ProductComponent()

    # GET request: /store/products  #get all products
    def list(self, request):
        products = self.product_component.get_product()
        if not products:
            return JsonResponse({'error': 'Error while retrieving products list'}, safe=False, status=404)

        return render(request, 'product/list.html', {'products': products})

    # GET request: /store/products/{pk}  #get product of given id
    def retrieve(self, request, pk=None):
        products = self.product_component.get_product(pk)
        if not products:
            return JsonResponse({'error': 'Error while retrieving product'}, safe=False, status=404)

        return render(request, 'product/retrieve.html', {'product': products})

    # POST request: /store/products #create new product
    def create(self, request):
        product = self.product_component.create_product(request)
        if product:
            return JsonResponse("server: product created successfully", safe=False, status=201)
        return JsonResponse("server: failed to creat product", safe=False)

    # DELETE request: /store/products/{pk} #delete product of given id
    def destroy(self, request, pk=None):
        product = self.product_component.delete_product(pk)
        if product:
            return JsonResponse("server: product successfully deleted", safe=False, status=200)
        return JsonResponse("server: Error happened while deleting product", safe=False)

    # PUT request: /store/products/{pk} #update product of given id
    def update(self, request, pk=None):
        updated_product = self.product_component.update_product(request, pk)
        if updated_product:
            return JsonResponse({'server': 'product successfully updated'})
        return JsonResponse({'error': 'Error while updating product'})

    @action(detail=False, methods=['GET'])
    def create_product(self, request):
        form = ProductForm()
        return render(request, 'product/create.html', {'form': form})
