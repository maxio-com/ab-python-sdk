# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class DunningStepData(object):

    """Implementation of the 'Dunning Step Data' model.

    TODO: type model description here.

    Attributes:
        day_threshold (int): TODO: type description here.
        action (str): TODO: type description here.
        email_body (str): TODO: type description here.
        email_subject (str): TODO: type description here.
        send_email (bool): TODO: type description here.
        send_bcc_email (bool): TODO: type description here.
        send_sms (bool): TODO: type description here.
        sms_body (str): TODO: type description here.

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
                 sms_body=APIHelper.SKIP):
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
        day_threshold = dictionary.get("day_threshold") if dictionary.get("day_threshold") else None
        action = dictionary.get("action") if dictionary.get("action") else None
        send_email = dictionary.get("send_email") if "send_email" in dictionary.keys() else None
        send_bcc_email = dictionary.get("send_bcc_email") if "send_bcc_email" in dictionary.keys() else None
        send_sms = dictionary.get("send_sms") if "send_sms" in dictionary.keys() else None
        email_body = dictionary.get("email_body") if "email_body" in dictionary.keys() else APIHelper.SKIP
        email_subject = dictionary.get("email_subject") if "email_subject" in dictionary.keys() else APIHelper.SKIP
        sms_body = dictionary.get("sms_body") if "sms_body" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(day_threshold,
                   action,
                   send_email,
                   send_bcc_email,
                   send_sms,
                   email_body,
                   email_subject,
                   sms_body)

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
            return APIHelper.is_valid_type(value=dictionary.day_threshold, type_callable=lambda value: isinstance(value, int)) \
                and APIHelper.is_valid_type(value=dictionary.action, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.send_email, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.send_bcc_email, type_callable=lambda value: isinstance(value, bool)) \
                and APIHelper.is_valid_type(value=dictionary.send_sms, type_callable=lambda value: isinstance(value, bool))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('day_threshold'), type_callable=lambda value: isinstance(value, int)) \
            and APIHelper.is_valid_type(value=dictionary.get('action'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_email'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_bcc_email'), type_callable=lambda value: isinstance(value, bool)) \
            and APIHelper.is_valid_type(value=dictionary.get('send_sms'), type_callable=lambda value: isinstance(value, bool))
