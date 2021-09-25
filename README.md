#Description
* This is a web application which retrieves and stores product information from
the Shopify API in a database, and allows users to place orders that are sent to Shopify.

## Running the project
* Clone the project
* Install python 3.7 and above
* Install Rabbitmq
* create virtual environment (virtualenv -p python3 env)
* Run pip install -r requirements.py
* Run celery celery -A mishipay_assingment worker --loglevel=debug

## Tasks
* Asynchronous task which will update product list from Shopify in
 background every 5 mins

## API
* get product list from db
* create order for a particular product variant id
* Fetch order with filters on date 
* Postman collection link - https://www.getpostman.com/collections/b2a5e5ea72d1d857a6fb
