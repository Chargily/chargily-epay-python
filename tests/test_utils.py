import json

from src.chargily_lib.utils import *
from src.chargily_lib.invoice import *
from src.chargily_lib.constant import *


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# DONT CHANGE THIS VALUES !!!
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
secret_key = "secret_c8f88123debb3a4d9c56f6587fff51eecc8c1c555a33fc572fa894a2ff1df765"
body_response = {
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

signature_expacted = "c1a075fde1d3e7e0f43be74017cd3e9a40d380268687bcfee91b434901c26943"
wrong_signature = "c1a075fde15468443be74017cd3e9a40d380268687bcfee91b434901c26943"
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


def test_generate_signature():

    json_reponse = json.dumps(body_response.copy())
    signature = generate_signature(json_reponse.encode(), secret_key.encode())

    assert (
        signature == "c1a075fde1d3e7e0f43be74017cd3e9a40d380268687bcfee91b434901c26943"
    )


def test_signature_confirmation():
    json_reponse = json.dumps(body_response.copy())

    valide_signature = confirm_signature(
        json_reponse.encode(), secret_key.encode(), signature_expacted
    )

    assert valide_signature == True

    valide_signature = confirm_signature(
        json_reponse.encode(), secret_key.encode(), wrong_signature
    )

    assert valide_signature == False


def test_fake_response_payment():
    fake_response = fake_response_payment()

    invoice = fake_response.get("invoice")

    assert invoice != None
    assert isinstance(invoice, dict)

    invoice_keys = set(invoice.keys())
    required_paramaters = set(body_response.keys())

    assert invoice_keys.difference(required_paramaters) == set()
