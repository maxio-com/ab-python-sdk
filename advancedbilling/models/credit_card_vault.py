# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreditCardVault(object):

    """Implementation of the 'Credit Card Vault' enum.

    The vault that stores the payment profile with the provided `vault_token`.
    Use `bogus` for testing.

    Attributes:
        ADYEN: The enum member of type str.
        AUTHORIZENET: The enum member of type str.
        BEANSTREAM: The enum member of type str.
        BLUE_SNAP: The enum member of type str.
        BOGUS: The enum member of type str.
        BRAINTREE1: The enum member of type str.
        BRAINTREE_BLUE: The enum member of type str.
        CHECKOUT: The enum member of type str.
        CYBERSOURCE: The enum member of type str.
        ELAVON: The enum member of type str.
        EWAY: The enum member of type str.
        EWAY_RAPID: The enum member of type str.
        EWAY_RAPID_STD: The enum member of type str.
        FIRSTDATA: The enum member of type str.
        FORTE: The enum member of type str.
        LITLE: The enum member of type str.
        MAXIO_PAYMENTS: The enum member of type str.
        MAXP: The enum member of type str.
        MODUSLINK: The enum member of type str.
        MONERIS: The enum member of type str.
        NMI: The enum member of type str.
        ORBITAL: The enum member of type str.
        PAYMENT_EXPRESS: The enum member of type str.
        PAYMILL: The enum member of type str.
        PAYPAL: The enum member of type str.
        PAYPAL_COMPLETE: The enum member of type str.
        PIN: The enum member of type str.
        SQUARE: The enum member of type str.
        STRIPE: The enum member of type str.
        STRIPE_CONNECT: The enum member of type str.
        TRUST_COMMERCE: The enum member of type str.
        UNIPAAS: The enum member of type str.
        WIRECARD: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """
    _all_values = ['adyen', 'authorizenet', 'beanstream', 'blue_snap', 'bogus', 'braintree1', 'braintree_blue', 'checkout', 'cybersource', 'elavon', 'eway', 'eway_rapid', 'eway_rapid_std', 'firstdata', 'forte', 'litle', 'maxio_payments', 'maxp', 'moduslink', 'moneris', 'nmi', 'orbital', 'payment_express', 'paymill', 'paypal', 'paypal_complete', 'pin', 'square', 'stripe', 'stripe_connect', 'trust_commerce', 'unipaas', 'wirecard']
    ADYEN = 'adyen'

    AUTHORIZENET = 'authorizenet'

    BEANSTREAM = 'beanstream'

    BLUE_SNAP = 'blue_snap'

    BOGUS = 'bogus'

    BRAINTREE1 = 'braintree1'

    BRAINTREE_BLUE = 'braintree_blue'

    CHECKOUT = 'checkout'

    CYBERSOURCE = 'cybersource'

    ELAVON = 'elavon'

    EWAY = 'eway'

    EWAY_RAPID = 'eway_rapid'

    EWAY_RAPID_STD = 'eway_rapid_std'

    FIRSTDATA = 'firstdata'

    FORTE = 'forte'

    LITLE = 'litle'

    MAXIO_PAYMENTS = 'maxio_payments'

    MAXP = 'maxp'

    MODUSLINK = 'moduslink'

    MONERIS = 'moneris'

    NMI = 'nmi'

    ORBITAL = 'orbital'

    PAYMENT_EXPRESS = 'payment_express'

    PAYMILL = 'paymill'

    PAYPAL = 'paypal'

    PAYPAL_COMPLETE = 'paypal_complete'

    PIN = 'pin'

    SQUARE = 'square'

    STRIPE = 'stripe'

    STRIPE_CONNECT = 'stripe_connect'

    TRUST_COMMERCE = 'trust_commerce'

    UNIPAAS = 'unipaas'

    WIRECARD = 'wirecard'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
   