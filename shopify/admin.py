from django.contrib import admin

# Register your models here.
from shopify.models import Order

admin.site.register(Order)