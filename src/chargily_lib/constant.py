CHARGILY_API_URL = "https://epay.chargily.com.dz/api/invoice"


# Request Parameters
CLIENT = "client"
CLIENT_EMAIL = "client_email"
INVOICE_NUMBER = "invoice_number"
AMOUNT = "amount"
DISCOUNT = "discount"
BACK_URL = "back_url"
WEBHOOK_URL = "webhook_url"
MODE = "mode"
COMMENT = "comment"


# PAYMENT mode
CIB = "CIB"
EDAHABIA = "EDAHABIA"


#   
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


PAYMENT_EXPIRED = "expired"
PAYMENT_PAID = "paid"
PAYMENT_FAILED = "failed"
PAYMENT_CANCELED = "canceled"
PAYMENT_IN_PROGRESS = "progress"