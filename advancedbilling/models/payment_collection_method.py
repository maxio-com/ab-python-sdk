# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PaymentCollectionMethod(object):

    """Implementation of the 'Payment Collection Method' enum.

    The type of payment collection to be used in the subscription. For legacy
    Statements Architecture valid options are - `invoice`, `automatic`. For
    current Relationship Invoicing Architecture valid options are -
    `remittance`, `automatic`, `prepaid`.

    Attributes:
        AUTOMATIC: TODO: type description here.
        REMITTANCE: TODO: type description here.
        PREPAID: TODO: type description here.
        INVOICE: TODO: type description here.

    """
    _all_values = ['automatic', 'remittance', 'prepaid', 'invoice']
    AUTOMATIC = 'automatic'

    REMITTANCE = 'remittance'

    PREPAID = 'prepaid'

    INVOICE = 'invoice'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values
