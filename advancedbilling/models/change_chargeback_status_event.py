# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.change_chargeback_status_event_data import ChangeChargebackStatusEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType


class ChangeChargebackStatusEvent(object):

    """Implementation of the 'Change Chargeback Status Event' model.

    Attributes:
        id (int): The model property of type int.
        timestamp (datetime): The model property of type datetime.
        invoice (Invoice): The model property of type Invoice.
        event_type (InvoiceEventType): The model property of type
            InvoiceEventType.
        event_data (ChangeChargebackStatusEventData): Example schema for an
            `change_chargeback_status` event
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 event_type='change_chargeback_status',
                 event_data=None,
                 additional_properties=None):
        """Constructor for the ChangeChargebackStatusEvent class"""

        # Initialize members of the class
        self.id = id 
        self.timestamp = APIHelper.apply_datetime_converter(timestamp, APIHelper.RFC3339DateTime) if timestamp else None 
        self.invoice = invoice 
        self.event_type = event_type 
        self.event_data = event_data 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        invoice = Invoice.from_dictionary(dictionary.get('invoice')) if dictionary.get('invoice') else None
        event_type = dictionary.get("event_type") if dictionary.get("event_type") else 'change_chargeback_status'
        event_data = ChangeChargebackStatusEventData.from_dictionary(dictionary.get('event_data')) if dictionary.get('event_data') else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   timestamp,
                   invoice,
                   event_type,
                   event_data,
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
                                            type_callable=lambda value: ChangeChargebackStatusEventData.validate(value),
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
                                        type_callable=lambda value: ChangeChargebackStatusEventData.validate(value),
                                        is_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'timestamp={self.timestamp!r}, '
                f'invoice={self.invoice!r}, '
                f'event_type={self.event_type!r}, '
                f'event_data={self.event_data!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'timestamp={self.timestamp!s}, '
                f'invoice={self.invoice!s}, '
                f'event_type={self.event_type!s}, '
                f'event_data={self.event_data!s}, '
                f'additional_properties={self.additional_properties!s})')
