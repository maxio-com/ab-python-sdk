# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AllVaults(object):

    """Implementation of the 'All Vaults' enum.

    The vault that stores the payment profile with the provided `vault_token`.
    Use `bogus` for testing.

    Attributes:
        ADYEN: TODO: type description here.
        AUTHORIZENET: TODO: type description here.
        BEANSTREAM: TODO: type description here.
        BLUE_SNAP: TODO: type description here.
        BOGUS: TODO: type description here.
        BRAINTREE1: TODO: type description here.
        BRAINTREE_BLUE: TODO: type description here.
        CHECKOUT: TODO: type description here.
        CYBERSOURCE: TODO: type description here.
        ELAVON: TODO: type description here.
        EWAY: TODO: type description here.
        EWAY_RAPID: TODO: type description here.
        EWAY_RAPID_STD: TODO: type description here.
        FIRSTDATA: TODO: type description here.
        FORTE: TODO: type description here.
        GOCARDLESS: TODO: type description here.
        LITLE: TODO: type description here.
        MAXIO_PAYMENTS: TODO: type description here.
        MAXP: TODO: type description here.
        MODUSLINK: TODO: type description here.
        MONERIS: TODO: type description here.
        NMI: TODO: type description here.
        ORBITAL: TODO: type description here.
        PAYMENT_EXPRESS: TODO: type description here.
        PAYMILL: TODO: type description here.
        PAYPAL: TODO: type description here.
        PAYPAL_COMPLETE: TODO: type description here.
        PIN: TODO: type description here.
        SQUARE: TODO: type description here.
        STRIPE: TODO: type description here.
        STRIPE_CONNECT: TODO: type description here.
        TRUST_COMMERCE: TODO: type description here.
        UNIPAAS: TODO: type description here.
        WIRECARD: TODO: type description here.

    """
    _all_values = ['adyen', 'authorizenet', 'beanstream', 'blue_snap', 'bogus', 'braintree1', 'braintree_blue', 'checkout', 'cybersource', 'elavon', 'eway', 'eway_rapid', 'eway_rapid_std', 'firstdata', 'forte', 'gocardless', 'litle', 'maxio_payments', 'maxp', 'moduslink', 'moneris', 'nmi', 'orbital', 'payment_express', 'paymill', 'paypal', 'paypal_complete', 'pin', 'square', 'stripe', 'stripe_connect', 'trust_commerce', 'unipaas', 'wirecard']
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

    GOCARDLESS = 'gocardless'

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
   