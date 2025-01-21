# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class SaleRepSubscription(object):

    """Implementation of the 'Sale Rep Subscription' model.

    Attributes:
        id (int): The model property of type int.
        site_name (str): The model property of type str.
        subscription_url (str): The model property of type str.
        customer_name (str): The model property of type str.
        created_at (str): The model property of type str.
        mrr (str): The model property of type str.
        usage (str): The model property of type str.
        recurring (str): The model property of type str.
        last_payment (str): The model property of type str.
        churn_date (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "site_name": 'site_name',
        "subscription_url": 'subscription_url',
        "customer_name": 'customer_name',
        "created_at": 'created_at',
        "mrr": 'mrr',
        "usage": 'usage',
        "recurring": 'recurring',
        "last_payment": 'last_payment',
        "churn_date": 'churn_date'
    }

    _optionals = [
        'id',
        'site_name',
        'subscription_url',
        'customer_name',
        'created_at',
        'mrr',
        'usage',
        'recurring',
        'last_payment',
        'churn_date',
    ]

    _nullables = [
        'churn_date',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 site_name=APIHelper.SKIP,
                 subscription_url=APIHelper.SKIP,
                 customer_name=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 mrr=APIHelper.SKIP,
                 usage=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 last_payment=APIHelper.SKIP,
                 churn_date=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SaleRepSubscription class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if site_name is not APIHelper.SKIP:
            self.site_name = site_name 
        if subscription_url is not APIHelper.SKIP:
            self.subscription_url = subscription_url 
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if mrr is not APIHelper.SKIP:
            self.mrr = mrr 
        if usage is not APIHelper.SKIP:
            self.usage = usage 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if last_payment is not APIHelper.SKIP:
            self.last_payment = last_payment 
        if churn_date is not APIHelper.SKIP:
            self.churn_date = churn_date 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else APIHelper.SKIP
        subscription_url = dictionary.get("subscription_url") if dictionary.get("subscription_url") else APIHelper.SKIP
        customer_name = dictionary.get("customer_name") if dictionary.get("customer_name") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        mrr = dictionary.get("mrr") if dictionary.get("mrr") else APIHelper.SKIP
        usage = dictionary.get("usage") if dictionary.get("usage") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if dictionary.get("recurring") else APIHelper.SKIP
        last_payment = dictionary.get("last_payment") if dictionary.get("last_payment") else APIHelper.SKIP
        churn_date = dictionary.get("churn_date") if "churn_date" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   site_name,
                   subscription_url,
                   customer_name,
                   created_at,
                   mrr,
                   usage,
                   recurring,
                   last_payment,
                   churn_date,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'site_name={self.site_name!r}, '
                f'subscription_url={self.subscription_url!r}, '
                f'customer_name={self.customer_name!r}, '
                f'created_at={self.created_at!r}, '
                f'mrr={self.mrr!r}, '
                f'usage={self.usage!r}, '
                f'recurring={self.recurring!r}, '
                f'last_payment={self.last_payment!r}, '
                f'churn_date={self.churn_date!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'site_name={self.site_name!s}, '
                f'subscription_url={self.subscription_url!s}, '
                f'customer_name={self.customer_name!s}, '
                f'created_at={self.created_at!s}, '
                f'mrr={self.mrr!s}, '
                f'usage={self.usage!s}, '
                f'recurring={self.recurring!s}, '
                f'last_payment={self.last_payment!s}, '
                f'churn_date={self.churn_date!s}, '
                f'additional_properties={self.additional_properties!s})')
