# Invoice module 
this module contain class and functions that helps you to create and store invoice object

## Exceptions
#### MissingFieldException
Raised when there is missing field in `Invoice` class

#### BadConfigException
Raised when a you pass a value of not accepted type 

<br>
## Functions
#### new_invoice
return a new empty invoice dict 

```py
>>> from chargily_lib.invoice import new_invoice
>>> new_invoice()
{'client': '', 'client_email': '', 'invoice_number': '', 'amount': '', 'discount': '', 'back_url': '', 'webhook_url': '', 'mode': '', 'comment': ''}
```

<br>

## Classes
#### Invoice
Invoice class come with more future than `new_invoice` function it can
- Detect missing fields
- Detect bad values
- Make it easy to insert value to a fields
- Extend from `UserDict` so its just a `dict` 

We can use `Invoice` class without validation *by default strict paramater is disable* 
```py
>>> from chargily_lib.invoice import Invoice
>>> invoice = Invoice() # strict = False  by default
>>> dict(invoice)
{'client': '', 'client_email': '', 'invoice_number': '', 'amount': '', 'discount': '', 'back_url': '', 'webhook_url': '', 'mode': '', 'comment': ''}
```
<br>
using `Invioce` class with `strict` pramater enabled.

by default all fields are empty if you use `strict` mode **Make sure to fill all required fields**
```py
>>> invoice = Invoice(strict=True) # strict = False  by default
>>> invoice.is_valide()
raise BadConfigException("Email entered is not valide")
src.chargily_lib.invoice.BadConfigException: Email entered is not valide

>>> invoice.client_email # empty field not valide 
'' 
```
<br>
If at any point one of the filed is removed runing validation method `is_valide` will raise `MissingFieldException`
```py
>>> del invoice['client_email'] # we remove client_email from invoice dict 
>>> invoice.is_valide() # this will raise MissingFieldException | no client_email field found
raise MissingFieldException(f"Field {parm} is required")
chargily_lib.invoice.MissingFieldException: Field client_email is required
```
<br>

If all field are filled correctly running `is_valid` method will be result of nothing, thats mean everything is okey.

```py
>>> invoice = Invoice(strict=True)
>>> invoice.client = "Tarek berkane"
>>> invoice.client_email = 'example@gmail.com'
>>> invoice.invoice_number = '1'
>>> invoice.mode = EDAHABIA
>>> invoice.amount = 10000 
>>> invoice.discount = 0
>>> invoice.comment = 'my first invoice payment.'
>>> invoice.back_url = 'https://example.com/'
>>> invoice.webhook_url = 'https://example.com/'

>>> invoice.is_valide() # will do nothing, no error found.
```