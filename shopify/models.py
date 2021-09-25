from django.db import models

# Create your models here.


class Variant(models.Model):
    shopify_variant_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    taxable = models.BooleanField(null=True)
    requires_shipping = models.BooleanField(null=True)


class Inventory(models.Model):
    shopify_listing_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.CharField(max_length=100, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    variant = models.ForeignKey(Variant, on_delete=models.PROTECT)


class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(null=True)
    confirmed = models.BooleanField(null=True)
    total_price = models.CharField(max_length=100, blank=True, null=True)
    order_status_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=50, null=True, blank=True)

