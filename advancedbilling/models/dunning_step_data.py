# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DunningStepData(object):

    """Implementation of the 'Dunning Step Data' model.

    Attributes:
        day_threshold (int): The model property of type int.
        action (str): The model property of type str.
        email_body (str): The model property of type str.
        email_subject (str): The model property of type str.
        send_email (bool): The model property of type bool.
        send_bcc_email (bool): The model property of type bool.
        send_sms (bool): The model property of type bool.
        sms_body (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day_threshold": 'day_threshold',
        "action": 'action',
        "send_email": 'send_email',
        "send_bcc_email": 'send_bcc_email',
        "send_sms": 'send_sms',
        "email_body": 'email_body',
        "email_subject": 'email_subject',
        "sms_body": 'sms_body'
    }

    _optionals = [
        'email_body',
        'email_subject',
        'sms_body',
    ]

    _nullables = [
        'email_body',
        'email_subject',
        'sms_body',
    ]

    def __init__(self,
                 day_threshold=None,
                 action=None,
                 send_email=None,
                 send_bcc_email=None,
                 send_sms=None,
                 email_body=APIHelper.SKIP,
                 email_subject=APIHelper.SKIP,
                 sms_body=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the DunningStepData class"""

        # Initialize members of the class
        self.day_threshold = day_threshold 
        self.action = action 
        if email_body is not APIHelper.SKIP:
            self.email_body = email_body 
        if email_subject is not APIHelper.SKIP:
            self.email_subject = email_subject 
        self.send_email = send_email 
        self.send_bcc_email = send_bcc_email 
        self.send_sms = send_sms 
        if sms_body is not APIHelper.SKIP:
            self.sms_body = sms_body 

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
        day_threshold = dictionary.get("day_threshold") if dictionary.get("day_threshold") else None
        action = dictionary.get("action") if dictionary.get("action") else None
        send_email = dictionary.get("send_email") if "send_email" in dictionary.keys() else None
        send_bcc_email = dictionary.get("send_bcc_email") if "send_bcc_email" in dictionary.keys() else None
        send_sms = dictionary.get("send_sms") if "send_sms" in dictionary.keys() else None
        email_body = dictionary.get("email_body") if "email_body" in dictionary.keys() else APIHelper.SKIP
        email_subject = dictionary.get("email_subject") if "email_subject" in dictionary.keys() else APIHelper.SKIP
        sms_body = dictionary.get("sms_body") if "sms_body" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(day_threshold,
                   action,
                   send_email,
                   send_bcc_email,
                   send_sms,
                   email_body,
                   email_subject,
                   sms_body,
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
            return APIHelper.is_valid_type(value=dictionary.day_threshold,
                                           type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.action,
                                            type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.send_email,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.send_bcc_email,
                                            type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.send_sms,
                                            type_callable=lambda value: isinstance(value, bool))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('day_threshold'),
                                       type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('action'),
                                        type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_email'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_bcc_email'),
                                        type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_sms'),
                                        type_callable=lambda value: isinstance(value, bool))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'day_threshold={self.day_threshold!r}, '
                f'action={self.action!r}, '
                f'email_body={(self.email_body if hasattr(self, "email_body") else None)!r}, '
                f'email_subject={(self.email_subject if hasattr(self, "email_subject") else None)!r}, '
                f'send_email={self.send_email!r}, '
                f'send_bcc_email={self.send_bcc_email!r}, '
                f'send_sms={self.send_sms!r}, '
                f'sms_body={(self.sms_body if hasattr(self, "sms_body") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'day_threshold={self.day_threshold!s}, '
                f'action={self.action!s}, '
                f'email_body={(self.email_body if hasattr(self, "email_body") else None)!s}, '
                f'email_subject={(self.email_subject if hasattr(self, "email_subject") else None)!s}, '
                f'send_email={self.send_email!s}, '
                f'send_bcc_email={self.send_bcc_email!s}, '
                f'send_sms={self.send_sms!s}, '
                f'sms_body={(self.sms_body if hasattr(self, "sms_body") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
