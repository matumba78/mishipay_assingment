from shopify.models import Inventory, Variant, Order
from shopify.services import ShopifySync


class UpdateInventory:

    def update_inventory(self, result):
        instances = []
        for data in result:
            shopify_listing_id = data.get("id", None)
            title = data.get("title")
            vendor = data.get("vendor")
            product_type = data.get("product_type")
            status = data.get("status")
            created_at = data.get("created_at")
            updated_at = data.get("updated_at")
            published_at = data.get("published_at")
            shopify_variant_id = data.get("variants")[0].get("id")
            variant_title = data.get("variants")[0].get("title")
            price = data.get("variants")[0].get("price")
            taxable = data.get("variants")[0].get("taxable")
            requires_shipping = data.get("variants")[0].get("requires_shipping")
            try:
                Inventory.objects.get(shopify_listing_id=shopify_listing_id)
            except Inventory.DoesNotExist:
                variant = Variant.objects.create(
                    shopify_variant_id=shopify_variant_id,
                    title=variant_title,
                    price=price,
                    taxable=taxable,
                    requires_shipping=requires_shipping
                )
                instances.append(Inventory(
                    shopify_listing_id = shopify_listing_id,
                    title = title,
                    vendor=vendor,
                    product_type=product_type,
                    status=status,
                    created_at=created_at,
                    variant_id=variant.id,
                    updated_at=updated_at,
                    published_at=published_at
                ))
        if instances:
            Inventory.objects.bulk_create(instances)


class CreateOrders:

    def create_orders(self, data):
        status, order_data = ShopifySync().create_order(data)
        if not status:
            return False, order_data
        order_id = order_data.get("id")
        created_at = order_data.get("created_at")
        confirmed = order_data.get("confirmed")
        total_price = order_data.get("total_price")
        order_status_url = order_data.get("order_status_url")
        status = order_data.get("status", None)
        order = Order.objects.create(
            order_id=order_id,
            created_at=created_at,
            confirmed=confirmed,
            total_price=total_price,
            order_status_url=order_status_url,
            status=status
        )
        return True, order


