import json

import requests

from chargily_lib.constant import CHARGILY_API_URL

from ..utils import confirm_signature, generate_signature


def make_payment(invoice: dict, api_key: str, chargily_api_url=CHARGILY_API_URL) -> requests.Response:
    headers = {"X-Authorization": api_key, "Accept": "application/json"}

    response = requests.post(chargily_api_url, data=invoice, headers=headers,timeout=5)
    return response


def send_fake_payment_confirmation(body: dict, secret_key: str, request_url: str):
    encoded_body = json.dumps(body).encode()
    encoded_key = secret_key.encode()

    signature = generate_signature(encoded_body, encoded_key)

    headers = {
        "Signature": signature,
        "Accept": "application/json",
    }

    requests.post(request_url, headers=headers, json=body)


class PaymentManager:
    def __init__(self, api_key, secret_key, api_url) -> None:
        self._api_key = api_key
        self._secret_key: str = secret_key
        self._api_url = api_url

    def make_payment(self, invoice: dict) -> requests.Response:
        return make_payment(invoice, self._api_key, self._api_url)

    def make_confirmation(self, body, request_signature):
        return confirm_signature(body, self._secret_key.encode(), request_signature)


