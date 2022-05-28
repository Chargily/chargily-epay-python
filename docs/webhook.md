# Webhook 
Depend of the type of library you installed `sync` or `async` the webhook can be found in:
#### Sync 
if you installed `chargily-epay` the module `webhook` will be in `chargily_lib.sync_lib.webhook`
```py
>>> from chargily_lib.sync_lib.webhook import *
```
#### Async
if you installed `chargily-epay-async` the module `webhook` will be in `chargily_lib.async_lib.webhook`
```py
>>> from chargily_lib.async_lib.webhook import *
```

## Functions

### make_payment
`make_payment` accept **2 required** parameter and **one optional** parameter

##### Parameters
- invoice type `dict` **required**
- api_key type `str` **rquired**
- chargily_api_url 'str' **not required**  default value `https://epay.chargily.com.dz/api/invoice`
##### Return 
return type is instance of `requests.Response` in `sync` mode and `aiohttp.ClientResponse` in `aysnc` mode.

- Responses:
    - 201 : payment created successffully

            >>> import json
            >>> from chargily_lib.sync_lib.webhook import make_payment
            >>> # other operation see quickstart section
            >>> response = make_payment(invoice, CHARGILY_API_KEY)
            >>> if response.status_code == 201:
            ...     data = json.loads(response.content)
            ...     print(data)
            {"checkout_url":"https://epay.chargily.com.dz/checkout/randome-text"}

    - 401 : Unauthorized 

            >>> import json
            >>> from chargily_lib.sync_lib.webhook import make_payment
            >>> # other operation see quickstart section
            >>> response = make_payment(invoice, CHARGILY_API_KEY)
            >>> if response.status_code == 401:
            ...     print(response.content)
            Invalid API_KEY

    - 422 : invalid parametters

            >>> import json
            >>> from chargily_lib.sync_lib.webhook import make_payment
            >>> # other operation see quickstart section
            >>> response = make_payment(invoice, CHARGILY_API_KEY)
            >>> if response.status_code == 422:
            ...     print(response.content)
            The request was well-formed but was unable to be followed due to semantic errors
            

### send_fake_payment_confirmation
this function help to mimic **chargily api** response, you can use this function for testing.
##### Parameters
- body type `dict` **required**, fake response data see `FAKE_PAYMENT_REPONSE` in `utils` module 
- secret_key type `str` **rquired**, Secret Key can be found in chargily dashboard [here](https://epay.chargily.com.dz/secure/admin/epay-api).
- request_url 'str' **required**  mimic response should be send, usually `webhook_url` provided in `invoice` request  

```py
>>> from chargily_lib.sync_lib.webhook import send_fake_payment_confirmation
>>> from chargily_lib.utils import FAKE_PAYMRNT_REPONSE
.... oprations make sure to 
>>> secret_key = "PUT-YOUR-SECRET-KEY-HERE"
>>> fake_data = FAKE_PAYMENT_REPONSE.copy() # make sure to create copy
>>> webhook_url = "https://example.com/payment/payment-confirmation/"
>>>
>>> send_fake_payment_confirmation(fake_data, secret_key, webhook_url)

```

## Classes
### PaymentManager
this class is used to simplify sending requet
- inserting `api_key`, `secret_key`, `api_url` the first time you create this manager 
#### Parameters
- api_key type `dict` **required**
- secret_key type `str` **rquired**
- api_url 'str' **required**  
<br>
#### Methods
##### make_payment
 require one parameter `invoice` type of `dict`

##### make_confirmation
 confirm signature sent from **chargily service** require two parameters `body` type `bytes` and `request_signature` type `str` 