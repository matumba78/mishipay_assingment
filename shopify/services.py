import requests

STORE_URL = "mishipaytestdevelopmentemptystore.myshopify.com"
API_KEY = "a38f4a6a8cb713fe2bebdbf3df331f54"
PASSWORD = "3182dcd29ff6c3f6f2dd325ba99b4216"


class ShopifySync:

    def get_products_list(self, sync_time=None, limit=50):
        params = {
            "limit": 50,
            "created_at_min": sync_time
        }
        response = requests.get("https://{}:{}@{}/admin/api/2021-01/products.json".format(API_KEY, PASSWORD, STORE_URL), params=params)
        if response.status_code == 200:
            return response.json().get('products')
        return None

    def create_order(self, data):
        payload = {
            "order":
                {
                    "line_items": data
                }
        }
        response = requests.post('https://{}:{}@{}/admin/api/2021-01/orders.json'.format(API_KEY, PASSWORD, STORE_URL), json=payload)
        if response.status_code == 201:
            return True, response.json().get('order')
        return False, response