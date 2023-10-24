# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice import Invoice


class InvoiceEvent(object):

    """Implementation of the 'Invoice Event' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        event_type (InvoiceEventType): Invoice Event Type
        event_data (ApplyCreditNoteEventData | ApplyDebitNoteEventData |
            ApplyPaymentEventData | ChangeInvoiceCollectionMethodEventData |
            IssueInvoiceEventData | RefundInvoiceEventData |
            RemovePaymentEventData | VoidInvoiceEventData |
            VoidInvoiceEventDataAnyOf8 | None): The event data is the data
            that, when combined with the command, results in the output
            invoice found in the invoice field.
        timestamp (str): TODO: type description here.
        invoice (Invoice): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "event_type": 'event_type',
        "event_data": 'event_data',
        "timestamp": 'timestamp',
        "invoice": 'invoice'
    }

    _optionals = [
        'id',
        'event_type',
        'event_data',
        'timestamp',
        'invoice',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 event_type=APIHelper.SKIP,
                 event_data=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 invoice=APIHelper.SKIP):
        """Constructor for the InvoiceEvent class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if event_type is not APIHelper.SKIP:
            self.event_type = event_type 
        if event_data is not APIHelper.SKIP:
            self.event_data = event_data 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if invoice is not APIHelper.SKIP:
            self.invoice = invoice 

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else APIHelper.SKIP
        event_data = APIHelper.deserialize_union_type(UnionTypeLookUp.get('InvoiceEventEventData'), dictionary.get('event_data'), False) if dictionary.get('event_data') is not None else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        invoice = Invoice.from_dictionary(dictionary.get('invoice')) if 'invoice' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   event_type,
                   event_data,
                   timestamp,
                   invoice)
