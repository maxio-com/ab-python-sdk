# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.apply_credit_note_event_data_1 import ApplyCreditNoteEventData1
from advancedbilling.models.invoice_1 import Invoice1


class InvoiceEvent(object):

    """Implementation of the 'Invoice Event' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        timestamp (datetime): TODO: type description here.
        invoice (Invoice1): TODO: type description here.
        event_type (str): TODO: type description here.
        event_data (ApplyCreditNoteEventData1): Example schema for an
            `apply_credit_note` event

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "timestamp": 'timestamp',
        "invoice": 'invoice',
        "event_type": 'event_type',
        "event_data": 'event_data'
    }

    _optionals = [
        'id',
        'timestamp',
        'invoice',
        'event_type',
        'event_data',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 invoice=APIHelper.SKIP,
                 event_type='Invoice Event',
                 event_data=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the InvoiceEvent class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = APIHelper.apply_datetime_converter(timestamp, APIHelper.RFC3339DateTime) if timestamp else None 
        if invoice is not APIHelper.SKIP:
            self.invoice = invoice 
        self.event_type = event_type 
        if event_data is not APIHelper.SKIP:
            self.event_data = event_data 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else APIHelper.SKIP
        invoice = Invoice1.from_dictionary(dictionary.get('invoice')) if 'invoice' in dictionary.keys() else APIHelper.SKIP
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else 'Invoice Event'
        event_data = ApplyCreditNoteEventData1.from_dictionary(dictionary.get('event_data')) if 'event_data' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   timestamp,
                   invoice,
                   event_type,
                   event_data,
                   dictionary)
