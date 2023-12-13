import requests
import random

# this will persist the session cookies automatically for us
session = requests.Session()

response = session.get('http://localhost:1777/api/basket/')

print(response.content)

response = session.get('http://localhost:1777/api/products/')

product = random.choice(response.json())

print(product)

data = {
    "url": product['url'],
    "quantity": 1,
}

response = session.post('http://localhost:1777/api/basket/add-product/', json=data)

print(response.content)

response = session.get('http://localhost:1777/api/basket/')

print(response.content)

guest_email = "foo@example.com"

# get our basket information
response = session.get('http://localhost:1777/api/basket/')
basket_data = response.json()

# oscar needs a country for the shipping address. You can get a list of
# the available countries with the api
response = session.get('http://localhost:1777/api/countries/')
countries = response.json()
print(countries)

# we need the country url in the shipping address
country_url = countries[1]['url']

# we need to check the available shipping options
response = session.get('http://localhost:1777/api/basket/shipping-methods/')
shipping_methods = response.json()
print(shipping_methods)

# pick one
shipping_method = shipping_methods[0]

# let's fill out the request data
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

# now we can place the order
response = session.post('http://localhost:1777/api/checkout/', json=data)

# and the api should give us a response with all info needed
print(response.content)
