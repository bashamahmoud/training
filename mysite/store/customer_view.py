from django.db import IntegrityError
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Customer
from . import serializers


class CustomerView(View):
    queryset = Customer.objects.all()

    @classmethod
    def get_extra_actions(cls):
        return []

    @action(methods=["GET"], detail=True)
    def get(self, request, pk=None):
        if pk is None:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.get(pk=pk)
        serializer = serializers.DefaultCustomerSerializer(queryset, many=True)
        return HttpResponse(serializer.data)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
