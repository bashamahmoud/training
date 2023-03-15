from django.http import JsonResponse
from rest_framework import viewsets

from .customer_component import CustomerComponent


class CustomerView(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.customer_component = CustomerComponent()

    # GET request: /store/customers  #get all customers accounts
    def list(self, request):
        customers = self.customer_component.get_customer()
        if not customers:
            return JsonResponse({'error': 'Error while retrieving customers list'}, status=404)

        return JsonResponse(customers, safe=False, status=200)

    # GET request: /store/customers/{pk}  #get customer account of given id
    def retrieve(self, request, pk=None):
        customers = self.customer_component.get_customer(pk)
        if not customers:
            return JsonResponse(
                {'error': 'there is an error in request please make sure everything alright and try again'}, status=404)

        return JsonResponse(customers, safe=False, status=200)

    # POST request: /store/customers #create new customer
    def create(self, request):
        customers = self.customer_component.register_customer(request)
        if customers:
            return JsonResponse({'server': 'Customer created successfully'}, safe=False, status=201)
        return JsonResponse({'error': 'error on creating a customer please try again'})

    # DELETE request: /store/customers/{pk} #DELETE customer of given id
    def destroy(self, request, pk=None):
        customer = self.customer_component.delete_customer(pk)
        if customer:
            return JsonResponse({'server': 'Customer deleted successfully'})
        return JsonResponse({'error': 'error on deleting a customer'}, status=404)

    # PUT request: /store/customers/{pk} #UPDATE customer of given id
    def update(self, request, pk=None):
        updated_customer = self.customer_component.update_customer(request, pk)
        if updated_customer:
            return JsonResponse({'server': 'Customer updated'})
        return JsonResponse({'error': 'error on updating customer'}, status=404)
