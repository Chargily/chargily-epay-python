# Constants
### CHARGILY_API_URL
url to send payment request default value `https://epay.chargily.com.dz/api/invoice`

### Request Parameters
required keyword used in chargily service 
```py
CLIENT = "client"
CLIENT_EMAIL = "client_email"
INVOICE_NUMBER = "invoice_number"
AMOUNT = "amount"
DISCOUNT = "discount"
BACK_URL = "back_url"
WEBHOOK_URL = "webhook_url"
MODE = "mode"
COMMENT = "comment"
```

### Payment mode
```py
CIB = "CIB"
EDAHABIA = "EDAHABIA"
```

### Required fileds   
required fileds used in chargily service 
```py
REQUIRED_PARAMTERS = {
    INVOICE_NUMBER,
    AMOUNT,
    DISCOUNT,
    CLIENT,
    CLIENT_EMAIL,
    COMMENT,
    MODE,
    WEBHOOK_URL,
    BACK_URL,
}
```

### Payment status
```py
PAYMENT_PAID = "paid"
PAYMENT_FAILED = "failed"
PAYMENT_CANCELED = "canceled"
PAYMENT_IN_PROGRESS = "progress" 
```