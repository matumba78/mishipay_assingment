from celery import shared_task
from django.conf import settings
from django.utils import timezone
from celery import Celery

from shopify.services import ShopifySync
from shopify.utils import CreateOrders

app = Celery()
limit = 50

@shared_task
def create_orders(data):
    CreateOrders().create_orders(data)

@shared_task()
def sync_shopify_listing_products():
    buffer = timezone.now() - timezone.timedelta(minutes=5)
    now_time = str(buffer.replace(tzinfo=timezone.utc)).split(' ')
    sync_time = f"{now_time[0]}T{now_time[1]}"
    ShopifySync().get_products_list(sync_time, limit)
