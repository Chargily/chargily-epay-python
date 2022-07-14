import pytest

from src.chargily_lib.invoice import *
from src.chargily_lib.constant import *


class TestInvoice:
    def test_new_invoice_dict_type(self):
        invoice = new_invoice()
        assert isinstance(invoice, dict)

    def test_all_required_paramter_exist(self):
        invoice: dict = new_invoice()
        keys = set(invoice.keys())
        assert keys.difference(REQUIRED_PARAMTERS) == set()

    def test_invoice_class(self):
        invoice = Invoice()
        keys = set(dict(invoice))
        assert keys.difference(REQUIRED_PARAMTERS) == set()

    # -------------------------
    # Invoice fileds validators
    # -------------------------
    def test_invoice_client_value_validators(self):
        invoice = Invoice()
        with pytest.raises(BadConfigException):
            invoice.client = 0  # client should be value of str

    def test_invoice_client_email_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.client_email = 0  # client should be value of str

        with pytest.raises(BadConfigException):
            invoice.client_email = "not-valid-email"  # client_email should contain @

    def test_invoice_invoice_number_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.invoice_number = 0  # invoice_number should type of str

    def test_invoice_amount_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.amount = -1  # amount should be > 0

        with pytest.raises(BadConfigException):
            invoice.amount = "not int type"  # amount should type of int or float

    def test_invoice_discount_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.discount = -1  # discount should be >= 0 or <= 0.99

        with pytest.raises(BadConfigException):
            invoice.discount = 1  # discount should be >= 0 or <= 0.99

        with pytest.raises(BadConfigException):
            invoice.discount = -0.99  # discount should be >= 0 or <= 0.99

        with pytest.raises(BadConfigException):
            invoice.discount = "not int type"  # discount should type of int

    def test_invoice_back_url_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.back_url = -1  # back_url should type of str

    def test_invoice_webhook_url_value_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.webhook_url = -1  # webhook url should type of str

    def test_invoice_mode_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.mode = -1  # back_url should type of str

        with pytest.raises(BadConfigException):
            invoice.mode = (
                "unknown option"  # mode value should be one of EDAHABIA or CIB
            )

    def test_invoice_comment_validators(self):
        invoice = Invoice()

        with pytest.raises(BadConfigException):
            invoice.comment = -1  # comment should type of str

    def test_invoice_strict_mode_value_empty_validators(self):
        invoice = Invoice(strict=True)  # Strict = True

        with pytest.raises(BadConfigException):
            # Some value are empty
            invoice_dict = dict(invoice)

    def test_invoice_manuale_insert_value_validators(self):

        invoice = Invoice()

        invoice.invoice_number = "1"
        invoice.client = "client name"
        invoice.client_email = "client_email@gamil.com"
        invoice.amount = 1000
        invoice.discount = 0
        invoice.back_url = "https://example.com"
        invoice.webhook_url = "https://example.com"
        invoice.comment = ""
        invoice.mode = EDAHABIA

        invoice_dict = dict(invoice)
        assert isinstance(invoice_dict, dict)

    # ------------------
    # Using Strict mode
    # ------------------
    def test_invoice_strict_mode_constructure_validators(self):
        data = {}
        data[INVOICE_NUMBER] = "1"
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(strict=True, **data)  # Strict = True

        invoice_dict = dict(invoice)
        assert isinstance(invoice_dict, dict)

    def test_invoice_strict_mode_constructure_bad_config_value_validators(self):
        data = {}
        data[INVOICE_NUMBER] = 1000  # NOT VALIDE !
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(strict=True, **data)  # Strict = True

        with pytest.raises(BadConfigException):
            # Some value are empty
            invoice_dict = dict(invoice)

    def test_invoice_strict_mode_constructure_missing_filed_value_validators(self):
        data = {}
        data[INVOICE_NUMBER] = "12345"
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(strict=True, **data)  # Strict = True

        del invoice.data[INVOICE_NUMBER]

        with pytest.raises(MissingFieldException):
            # Some value are empty
            invoice_dict = dict(invoice)

    # ---------------------
    # Not using strict mode
    # ---------------------
    def test_invoice_strict_mode_disabled_constructure_validators(self):
        data = {}
        data[INVOICE_NUMBER] = "1"
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(**data)  # Strict = True

        invoice_dict = dict(invoice)
        assert isinstance(invoice_dict, dict)

    def test_invoice_strict_mode_disabled_constructure_bad_config_value_validators(
        self,
    ):
        data = {}
        data[INVOICE_NUMBER] = 1000  # NOT VALIDE !
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(**data)  # Strict = True

        invoice_dict = dict(invoice)
        assert isinstance(invoice_dict, dict)

    def test_invoice_strict_mode_disabled_constructure_missing_filed_value_validators(
        self,
    ):
        data = {}
        data[INVOICE_NUMBER] = "12345"
        data[CLIENT] = "client name"
        data[CLIENT_EMAIL] = "client_email@gamil.com"
        data[AMOUNT] = 1000
        data[DISCOUNT] = 0
        data[BACK_URL] = "https://example.com"
        data[WEBHOOK_URL] = "https://example.com"
        data[COMMENT] = ""
        data[MODE] = EDAHABIA

        invoice = Invoice(**data)  # Strict = True

        del invoice.data[INVOICE_NUMBER]

        invoice_dict = dict(invoice)
        assert isinstance(invoice_dict, dict)
