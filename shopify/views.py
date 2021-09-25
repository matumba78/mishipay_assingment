from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from shopify.filters import OrderFilter
from shopify.models import Inventory, Order
from shopify.paginations import SmartPagination
from shopify.serializers import InventorySerializer, OrderSerializer
from shopify.services import ShopifySync
from shopify.tasks import create_orders
from shopify.utils import CreateOrders
import django_filters.rest_framework as filters


class InventoryListView(generics.ListAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all().order_by("-created_at")
    pagination_class = SmartPagination


class OrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-created_at")
    pagination_class = SmartPagination
    filter_class = OrderFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def post(self, request, *args, **kwargs):
        status, data = CreateOrders().create_orders(request.data)
        if not status:
            return Response(data.json())
        return Response({
            "status": "order places successfully",
            "data": OrderSerializer(data).data
        })


