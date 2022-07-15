# epay-chargily-python
Chargily ePay Gateway (Python Library)

![Chargily ePay Gateway](https://raw.githubusercontent.com/Chargily/epay-gateway-php/main/assets/banner-1544x500.png "Chargily ePay Gateway")

This Plugin is to integrate ePayment gateway with Chargily easily.
- Currently support payment by **CIB / EDAHABIA** cards and soon by **Visa / Mastercard** 
- This repo is recently created for **Python Library**, If you are a developer and want to collaborate to the development of this library, you are welcomed!

# Instalation
## chargily-epay
this is `sync` version using `requests` library 
```
pip install chargily-epay-python
```


## chargily-epay-async
this is `async` version using `aiohttp` library
```
pip install chargily-epay-Async
```

## Quickstart 
Simple example
```py
from chargily_lib.constant import EDAHABIA
from chargily_lib.invoice import Invoice
from chargily_lib.utils import extract_redirect_url
from chargily_lib.sync_lib.webhook import make_payment

API_KEY = "YOUR-API-KEY"

invoice = Invoice()
invoice.client = "Tarek berkane"
invoice.client_email = 'example@gmail.com'
invoice.invoice_number = '1'
invoice.mode = EDAHABIA
invoice.amount = 10000 
invoice.discount = 0
invoice.comment = 'my first invoice payment.'
invoice.back_url = 'https://example.com/'
invoice.webhook_url = 'https://example.com/'


response = make_payment(invoice, API_KEY)

if response.status_code == 201:
    print(extract_redirect_url(response.content))
```

# Contribution tips
1. Make a fork of this repo.
2. Take a tour to our [API documentation here](http://dev.codingdz.com/python-chargily-epay/)
3. Get your API Key/Secret from [ePay by Chargily](https://epay.chargily.com) dashboard for free.
4. Start developing.
5. Finished? Push and merge.
