# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_status import InvoiceStatus


class ChangeInvoiceStatusEventData(object):

    """Implementation of the 'Change Invoice Status Event Data' model.

    Example schema for an `change_invoice_status` event

    Attributes:
        gateway_trans_id (str): Identifier for the transaction within the
            payment gateway.
        amount (str): The monetary value associated with the linked payment,
            expressed in dollars.
        from_status (InvoiceStatus): The status of the invoice before any
            changes occurred. See [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        to_status (InvoiceStatus): The updated status of the invoice after
            changes have been made. See [Invoice
            Statuses](https://maxio.zendesk.com/hc/en-us/articles/2425228782964
            5-Advanced-Billing-Invoices-Overview#invoice-statuses) for more.
        consolidation_level (InvoiceConsolidationLevel): TODO: type
            description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "from_status": 'from_status',
        "to_status": 'to_status',
        "gateway_trans_id": 'gateway_trans_id',
        "amount": 'amount',
        "consolidation_level": 'consolidation_level'
    }

    _optionals = [
        'gateway_trans_id',
        'amount',
        'consolidation_level',
    ]

    def __init__(self,
                 from_status=None,
                 to_status=None,
                 gateway_trans_id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 consolidation_level=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ChangeInvoiceStatusEventData class"""

        # Initialize members of the class
        if gateway_trans_id is not APIHelper.SKIP:
            self.gateway_trans_id = gateway_trans_id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        self.from_status = from_status 
        self.to_status = to_status 
        if consolidation_level is not APIHelper.SKIP:
            self.consolidation_level = consolidation_level 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        from_status = dictionary.get("from_status") if dictionary.get("from_status") else None
        to_status = dictionary.get("to_status") if dictionary.get("to_status") else None
        gateway_trans_id = dictionary.get("gateway_trans_id") if dictionary.get("gateway_trans_id") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        consolidation_level = dictionary.get("consolidation_level") if dictionary.get("consolidation_level") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(from_status,
                   to_status,
                   gateway_trans_id,
                   amount,
                   consolidation_level,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.from_status,
                                           type_callable=lambda value: InvoiceStatus.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.to_status,
                                            type_callable=lambda value: InvoiceStatus.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('from_status'),
                                       type_callable=lambda value: InvoiceStatus.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('to_status'),
                                        type_callable=lambda value: InvoiceStatus.validate(value))
