# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.change_invoice_collection_method_event_data import ChangeInvoiceCollectionMethodEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType


class ChangeInvoiceCollectionMethodEvent(object):

    """Implementation of the 'Change Invoice Collection Method Event' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        timestamp (datetime): TODO: type description here.
        invoice (Invoice): TODO: type description here.
        event_type (InvoiceEventType): TODO: type description here.
        event_data (ChangeInvoiceCollectionMethodEventData): Example schema
            for an `change_invoice_collection_method` event

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "timestamp": 'timestamp',
        "invoice": 'invoice',
        "event_type": 'event_type',
        "event_data": 'event_data'
    }

    def __init__(self,
                 id=None,
                 timestamp=None,
                 invoice=None,
                 event_type='change_invoice_collection_method',
                 event_data=None,
                 additional_properties={}):
        """Constructor for the ChangeInvoiceCollectionMethodEvent class"""

        # Initialize members of the class
        self.id = id 
        self.timestamp = APIHelper.apply_datetime_converter(timestamp, APIHelper.RFC3339DateTime) if timestamp else None 
        self.invoice = invoice 
        self.event_type = event_type 
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
        id = dictionary.get("id") if dictionary.get("id") else None
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        invoice = Invoice.from_dictionary(dictionary.get('invoice')) if dictionary.get('invoice') else None
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else 'change_invoice_collection_method'
        event_data = ChangeInvoiceCollectionMethodEventData.from_dictionary(dictionary.get('event_data')) if dictionary.get('event_data') else None
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
            return APIHelper.is_valid_type(value=dictionary.id,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.timestamp,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and APIHelper.is_valid_type(value=dictionary.invoice,
                                            type_callable=lambda value: Invoice.validate(value),
                                            is_model_dict=True) \
                and APIHelper.is_valid_type(value=dictionary.event_type,
                                            type_callable=lambda value: InvoiceEventType.validate(value)) \
                and APIHelper.is_valid_type(value=dictionary.event_data,
                                            type_callable=lambda value: ChangeInvoiceCollectionMethodEventData.validate(value),
                                            is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('id'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('timestamp'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('invoice'),
                                        type_callable=lambda value: Invoice.validate(value),
                                        is_model_dict=True) \
            and APIHelper.is_valid_type(value=dictionary.get('event_type'),
                                        type_callable=lambda value: InvoiceEventType.validate(value)) \
            and APIHelper.is_valid_type(value=dictionary.get('event_data'),
                                        type_callable=lambda value: ChangeInvoiceCollectionMethodEventData.validate(value),
                                        is_model_dict=True)
