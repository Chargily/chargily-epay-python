from collections import UserDict

from .constant import *


_invoice = {
    CLIENT: "",
    CLIENT_EMAIL: "",
    INVOICE_NUMBER: "",
    AMOUNT: "",
    DISCOUNT: "",
    BACK_URL: "",
    WEBHOOK_URL: "",
    MODE: "",
    COMMENT: "",
}


class MissingFieldException(Exception):
    pass


class BadConfigException(Exception):
    pass


def new_invoice(**kwargs) -> dict:
    invoice = _invoice.copy()
    invoice.update(kwargs)
    return invoice


class Invoice(UserDict):
    def __init__(self, strict: bool = False, **kwargs) -> None:
        self.strict = strict
        self.data: dict = new_invoice(**kwargs)

    # CLIENT
    @property
    def client(self):
        return self.data[CLIENT]

    @client.setter
    def client(self, client_name: str):
        self.client_validator(client_name)
        self.data[CLIENT] = client_name

    def client_validator(self, client_name: str):
        if not isinstance(client_name, str):
            raise BadConfigException("Client should be type of str")

    # CLIENT EMAIL
    @property
    def client_email(self):
        return self.data[CLIENT_EMAIL]

    @client_email.setter
    def client_email(self, email: str):
        self.client_email_validator(email)
        self.data[CLIENT_EMAIL] = email

    def client_email_validator(self, email: str):
        if not isinstance(email, str):
            raise BadConfigException("Client email should be type of String")

        if "@" not in email:
            raise BadConfigException("Email entered is not valide")

    # INVOICE_NUMBER
    @property
    def invoice_number(self):
        return self.data[INVOICE_NUMBER]

    @invoice_number.setter
    def invoice_number(self, invoice_number: str):
        self.invoice_number_validator(invoice_number)
        self.data[INVOICE_NUMBER] = invoice_number

    def invoice_number_validator(self, invoice_number: str):
        if not isinstance(invoice_number, str):
            raise BadConfigException("Invoice number should be type of str")

    # AMOUNT
    @property
    def amount(self):
        return self.data[AMOUNT]

    @amount.setter
    def amount(self, amount: float):
        self.amount_validator(amount)
        self.data[AMOUNT] = amount

    def amount_validator(self, amount):
        if not isinstance(amount, (int, float)):
            raise BadConfigException("Amount should be type of int or float")
        if amount <= 0:
            raise BadConfigException("Amount should be > 0")

    # DISCOUNT
    @property
    def discount(self):
        return self.data[DISCOUNT]

    @discount.setter
    def discount(self, discount: float):
        self.discount_validator(discount)
        self.data[DISCOUNT] = discount

    def discount_validator(self, discount: float):
        if not isinstance(discount, (float, int)):
            raise BadConfigException("Discount should be type of int, float")

        if 0 > discount or discount >= 1:
            raise BadConfigException(
                "Discount should be bigger or equal 0 or smaller than 1"
            )

    # BACK_URL
    @property
    def back_url(self):
        return self.data[BACK_URL]

    @back_url.setter
    def back_url(self, url):
        self.back_url_validator(url)
        self.data[BACK_URL] = url

    def back_url_validator(self, url):
        if not isinstance(url, str):
            raise BadConfigException("Back url should be type of str")

    # WEBHOOK_URL
    @property
    def webhook_url(self):
        return self.data[WEBHOOK_URL]

    @webhook_url.setter
    def webhook_url(self, url):
        self.webhook_url_validator(url)
        self.data[WEBHOOK_URL] = url

    def webhook_url_validator(self, url):
        if not isinstance(url, str):
            raise BadConfigException("Webhook url should be type of str")

    # MODE
    @property
    def mode(self):
        return self.data[MODE]

    @mode.setter
    def mode(self, payment_mode: str):
        self.mode_validator(payment_mode)
        self.data[MODE] = payment_mode

    def mode_validator(self, payment_mode: str):
        if not isinstance(payment_mode, str):
            raise BadConfigException("Mode should be type of str")
        if payment_mode not in [EDAHABIA, CIB]:
            raise BadConfigException("Mode value should be on of EDAHABIA, CIB")

    # COMMENT
    @property
    def comment(self):
        return self.data[COMMENT]

    @comment.setter
    def comment(self, comment_text: str):
        self.comment_validator(comment_text)
        self.data[COMMENT] = comment_text

    def comment_validator(self, comment_text: str):
        if not isinstance(comment_text, str):
            raise BadConfigException("Comment should be type of str")

    # VALIDATORS
    def _validate_required_pramters(self):
        data_keys = self.data.keys()
        for parm in REQUIRED_PARAMTERS:
            if parm not in data_keys:
                raise MissingFieldException(f"Field {parm} is required")

    def _validate_paramters_value(self):
        for key, value in self.data.items():
            if hasattr(self, f"{key}_validator"):
                validator = getattr(self, f"{key}_validator")
                validator(value)

    def is_valide(self):
        if self.strict:
            self._validate_required_pramters()
            self._validate_paramters_value()

    def __dict__(self):
        self.is_valide()
        return self.data

    def __iter__(self):
        self.is_valide()
        return super().__iter__()
