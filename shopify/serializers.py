from rest_framework import serializers

from shopify.models import Inventory, Variant, Order


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variant
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    variant = VariantSerializer()

    class Meta:
        model = Inventory
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

