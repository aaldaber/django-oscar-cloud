import random
import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def buy_one_item(self):
        response = self.client.get("/api/basket/")
        time.sleep(random.randint(1, 5))
        response = self.client.get('/api/products/')
        time.sleep(random.randint(1, 5))
        product = random.choice(response.json())
        data = {
            "url": product['url'],
            "quantity": 1,
        }
        if 1 == random.randint(1, 10):
            response = self.client.post('/api/basket/add-product/', data=data)
            time.sleep(random.randint(1, 5))
            response = self.client.get("/api/basket/")
            time.sleep(random.randint(1, 5))
            basket_data = response.json()
            guest_email = "foo@example.com"
            response = self.client.get("/api/countries/")
            countries = response.json()
            country_url = countries[1]['url']
            response = self.client.get("/api/basket/shipping-methods/")
            shipping_methods = response.json()
            shipping_method = shipping_methods[0]
            data = {
                "basket": basket_data['url'],
                "guest_email": guest_email,
                "total": basket_data['total_incl_tax'],
                "shipping_method_code": shipping_method['code'],
                # the shipping charge is optional, but we leave it here for example purposes
                "shipping_charge": {
                    "currency": basket_data['currency'],
                    "excl_tax": "0.0",
                    "tax": "0.0"
                },
                "shipping_address": {
                    "country": country_url,
                    "first_name": "Henk",
                    "last_name": "Van den Heuvel",
                    "line1": "Roemerlaan 44",
                    "line2": "",
                    "line3": "",
                    "line4": "Kroekingen",
                    "notes": "",
                    "phone_number": "+31 26 370 4887",
                    "postcode": "7777KK",
                    "state": "Gerendrecht",
                    "title": "Mr"
                }
            }
            response = self.client.post('/api/checkout/', json=data)
            if response.status_code != 200:
                print(data)
            # close request to start a new session
        time.sleep(random.randint(1, 5))
        self.client.close()
