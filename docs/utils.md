# Utils
this module contain helper functions and constants 

## Constants 
### FAKE_PAYMENT_REPONSE 
this constant is a mimic of `chargily service` reponse 

```py
FAKE_PAYMENT_REPONSE = {
    "id": 5800215,
    "client": "Client name",
    "invoice_number": "123456789",
    "due_date": "2022-01-01 00:00:00",
    "status": "paid",
    "amount": 75,
    "fee": 25,
    "discount": 0,
    "comment": "Payment description",
    "tos": 1,
    "mode": "EDAHABIA",
    "invoice_token": "randoom_token_here",
    "due_amount": 10000,
    "created_at": "2022-01-01 00:30:00",
    "updated_at": "2022-01-01 00:31:06",
    "back_url": "https://www.mydomain.com/success",
    "new": 1,
}
```

## Functions
### fake_response_payment
generate fake response, you can insert any feilds with value as paramter
```py
>>> fake_response_payment()
{"id": 5800215, "client": "Client name", "invoice_number": "123456789", "due_date": "2022-01-01 00:00:00", "status": "paid", # etc
>>> fake_response_payment(id=10, client='Tarek Berkane')
{"id": 10, "client": "Tarek Berkane", "invoice_number": "123456789", "due_date": "2022-01-01 00:00:00", "status": "paid", # etc
```

### generate_signature
create a signature using `Secret_key` and `body`

### confirm_signature
confirm signature using `Secret_key` and `body` and signature

### extract_redirect_url
helper function to extract url from http response of `chargily service`
```py
from chargily_lib.constant import EDAHABIA
from chargily_lib.invoice import Invoice
from chargily_lib.utils import extract_redirect_url
from chargily_lib.sync_lib.webhook import make_payment

API_KEY = "api_yOdfdsawe5re5wDrvFF2f4dafAqxxX7FRii1dgXfRd8ectfI4IaTpFbHxdAUeu2IdB"


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
#    data = json.dumps(response.content)
#    print(data['checkout_url'])
    print(extract_redirect_url(response.content))
```