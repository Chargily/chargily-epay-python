import json
import hmac


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


def generate_signature(body: bytes, secret_key: bytes):
    data = hmac.new(key=secret_key, msg=body, digestmod="sha256")
    return data.hexdigest()


def confirm_signature(body: bytes, secret_key: bytes, request_signature: str):
    signature = generate_signature(body, secret_key)
    if signature == request_signature:
        return True
    return False


def extract_redirect_url(response_content):
    data = json.loads(response_content)
    return data["checkout_url"]


def fake_response_payment(**kwargs):
    fake_date: dict = FAKE_PAYMENT_REPONSE.copy()
    fake_date.update(**kwargs)
    return {"invoice": fake_date}
