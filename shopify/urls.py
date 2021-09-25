from django.urls import path
from shopify.views import *

urlpatterns = [
    path('get_products/', InventoryListView.as_view(), name="get_products"),
    path('order/', OrderCreateView.as_view(), name="order_products"),
]