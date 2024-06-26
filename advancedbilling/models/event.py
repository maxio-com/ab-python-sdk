# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Event(object):

    """Implementation of the 'Event' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        key (str): TODO: type description here.
        message (str): TODO: type description here.
        subscription_id (int): TODO: type description here.
        customer_id (int): TODO: type description here.
        created_at (datetime): TODO: type description here.
        event_specific_data (SubscriptionProductChange |
            SubscriptionStateChange | PaymentRelatedEvents | RefundSuccess |
            ComponentAllocationChange | MeteredUsage | PrepaidUsage |
            DunningStepReached | InvoiceIssued | PendingCancellationChange |
            PrepaidSubscriptionBalanceChanged | ProformaInvoiceIssued |
            SubscriptionGroupSignupSuccess | SubscriptionGroupSignupFailure |
            CreditAccountBalanceChanged | PrepaymentAccountBalanceChanged |
            PaymentCollectionMethodChanged | ItemPricePointChanged |
            CustomFieldValueChange | None): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "key": 'key',
        "message": 'message',
        "subscription_id": 'subscription_id',
        "customer_id": 'customer_id',
        "created_at": 'created_at',
        "event_specific_data": 'event_specific_data'
    }

    _nullables = [
        'subscription_id',
        'customer_id',
        'event_specific_data',
    ]

    def __init__(self,
                 id=None,
                 key=None,
                 message=None,
                 subscription_id=None,
                 customer_id=None,
                 created_at=None,
                 event_specific_data=None,
                 additional_properties={}):
        """Constructor for the Event class"""

        # Initialize members of the class
        self.id = id 
        self.key = key 
        self.message = message 
        self.subscription_id = subscription_id 
        self.customer_id = customer_id 
        self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        self.event_specific_data = event_specific_data 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if dictionary.get("id") else None
        key = dictionary.get("key") if dictionary.get("key") else None
        message = dictionary.get("message") if dictionary.get("message") else None
        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        event_specific_data = APIHelper.deserialize_union_type(UnionTypeLookUp.get('EventEventSpecificData'), dictionary.get('event_specific_data'), False) if dictionary.get('event_specific_data') is not None else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   key,
                   message,
                   subscription_id,
                   customer_id,
                   created_at,
                   event_specific_data,
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.id,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.key,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.message,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.subscription_id,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.customer_id,
                                            type_callable=lambda value: isinstance(value, int),
                                            is_value_nullable=True) \
                and APIHelper.is_valid_type(value=dictionary.created_at,
                                            type_callable=lambda value: isinstance(value, APIHelper.RFC3339DateTime)) \
                and UnionTypeLookUp.get('EventEventSpecificData').validate(dictionary.event_specific_data).is_valid

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('id'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('key'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('message'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('subscription_id'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('customer_id'),
                                        type_callable=lambda value: isinstance(value, int),
                                        is_value_nullable=True) \
            and APIHelper.is_valid_type(value=dictionary.get('created_at'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('EventEventSpecificData').validate(dictionary.get('event_specific_data')).is_valid
