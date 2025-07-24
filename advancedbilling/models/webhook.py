# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class Webhook(object):

    """Implementation of the 'Webhook' model.

    Attributes:
        event (str): A string describing which event type produced the given
            webhook
        id (int): The unique identifier for the webhooks (unique across all of
            Chargify). This is not changed on a retry/replay of the same
            webhook, so it may be used to avoid duplicate action for the same
            event.
        created_at (datetime): Timestamp indicating when the webhook was
            created
        last_error (str): Text describing the status code and/or error from
            the last failed attempt to send the Webhook. When a webhook is
            retried and accepted, this field will be cleared.
        last_error_at (datetime): Timestamp indicating when the last
            non-acceptance occurred. If a webhook is later resent and
            accepted, this field will be cleared.
        accepted_at (datetime): Timestamp indicating when the webhook was
            accepted by the merchant endpoint. When a webhook is explicitly
            replayed by the merchant, this value will be cleared until it is
            accepted again.
        last_sent_at (datetime): Timestamp indicating when the most recent
            attempt was made to send the webhook
        last_sent_url (str): The url that the endpoint was last sent to.
        successful (bool): A boolean flag describing whether the webhook was
            accepted by the webhook endpoint for the most recent attempt.
            (Acceptance is defined by receiving a “200 OK” HTTP response
            within a reasonable timeframe, i.e. 15 seconds)
        body (str): The data sent within the webhook post
        signature (str): The calculated webhook signature
        signature_hmac_sha_256 (str): The calculated HMAC-SHA-256 webhook
            signature
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "event": 'event',
        "id": 'id',
        "created_at": 'created_at',
        "last_error": 'last_error',
        "last_error_at": 'last_error_at',
        "accepted_at": 'accepted_at',
        "last_sent_at": 'last_sent_at',
        "last_sent_url": 'last_sent_url',
        "successful": 'successful',
        "body": 'body',
        "signature": 'signature',
        "signature_hmac_sha_256": 'signature_hmac_sha_256'
    }

    _optionals = [
        'event',
        'id',
        'created_at',
        'last_error',
        'last_error_at',
        'accepted_at',
        'last_sent_at',
        'last_sent_url',
        'successful',
        'body',
        'signature',
        'signature_hmac_sha_256',
    ]

    _nullables = [
        'accepted_at',
    ]

    def __init__(self,
                 event=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 last_error=APIHelper.SKIP,
                 last_error_at=APIHelper.SKIP,
                 accepted_at=APIHelper.SKIP,
                 last_sent_at=APIHelper.SKIP,
                 last_sent_url=APIHelper.SKIP,
                 successful=APIHelper.SKIP,
                 body=APIHelper.SKIP,
                 signature=APIHelper.SKIP,
                 signature_hmac_sha_256=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Webhook class"""

        # Initialize members of the class
        if event is not APIHelper.SKIP:
            self.event = event 
        if id is not APIHelper.SKIP:
            self.id = id 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if last_error is not APIHelper.SKIP:
            self.last_error = last_error 
        if last_error_at is not APIHelper.SKIP:
            self.last_error_at = APIHelper.apply_datetime_converter(last_error_at, APIHelper.RFC3339DateTime) if last_error_at else None 
        if accepted_at is not APIHelper.SKIP:
            self.accepted_at = APIHelper.apply_datetime_converter(accepted_at, APIHelper.RFC3339DateTime) if accepted_at else None 
        if last_sent_at is not APIHelper.SKIP:
            self.last_sent_at = APIHelper.apply_datetime_converter(last_sent_at, APIHelper.RFC3339DateTime) if last_sent_at else None 
        if last_sent_url is not APIHelper.SKIP:
            self.last_sent_url = last_sent_url 
        if successful is not APIHelper.SKIP:
            self.successful = successful 
        if body is not APIHelper.SKIP:
            self.body = body 
        if signature is not APIHelper.SKIP:
            self.signature = signature 
        if signature_hmac_sha_256 is not APIHelper.SKIP:
            self.signature_hmac_sha_256 = signature_hmac_sha_256 

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
        event = dictionary.get("event") if dictionary.get("event") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        last_error = dictionary.get("last_error") if dictionary.get("last_error") else APIHelper.SKIP
        last_error_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_error_at")).datetime if dictionary.get("last_error_at") else APIHelper.SKIP
        if 'accepted_at' in dictionary.keys():
            accepted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("accepted_at")).datetime if dictionary.get("accepted_at") else None
        else:
            accepted_at = APIHelper.SKIP
        last_sent_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("last_sent_at")).datetime if dictionary.get("last_sent_at") else APIHelper.SKIP
        last_sent_url = dictionary.get("last_sent_url") if dictionary.get("last_sent_url") else APIHelper.SKIP
        successful = dictionary.get("successful") if "successful" in dictionary.keys() else APIHelper.SKIP
        body = dictionary.get("body") if dictionary.get("body") else APIHelper.SKIP
        signature = dictionary.get("signature") if dictionary.get("signature") else APIHelper.SKIP
        signature_hmac_sha_256 = dictionary.get("signature_hmac_sha_256") if dictionary.get("signature_hmac_sha_256") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(event,
                   id,
                   created_at,
                   last_error,
                   last_error_at,
                   accepted_at,
                   last_sent_at,
                   last_sent_url,
                   successful,
                   body,
                   signature,
                   signature_hmac_sha_256,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'event={(self.event if hasattr(self, "event") else None)!r}, '
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'last_error={(self.last_error if hasattr(self, "last_error") else None)!r}, '
                f'last_error_at={(self.last_error_at if hasattr(self, "last_error_at") else None)!r}, '
                f'accepted_at={(self.accepted_at if hasattr(self, "accepted_at") else None)!r}, '
                f'last_sent_at={(self.last_sent_at if hasattr(self, "last_sent_at") else None)!r}, '
                f'last_sent_url={(self.last_sent_url if hasattr(self, "last_sent_url") else None)!r}, '
                f'successful={(self.successful if hasattr(self, "successful") else None)!r}, '
                f'body={(self.body if hasattr(self, "body") else None)!r}, '
                f'signature={(self.signature if hasattr(self, "signature") else None)!r}, '
                f'signature_hmac_sha_256={(self.signature_hmac_sha_256 if hasattr(self, "signature_hmac_sha_256") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'event={(self.event if hasattr(self, "event") else None)!s}, '
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'last_error={(self.last_error if hasattr(self, "last_error") else None)!s}, '
                f'last_error_at={(self.last_error_at if hasattr(self, "last_error_at") else None)!s}, '
                f'accepted_at={(self.accepted_at if hasattr(self, "accepted_at") else None)!s}, '
                f'last_sent_at={(self.last_sent_at if hasattr(self, "last_sent_at") else None)!s}, '
                f'last_sent_url={(self.last_sent_url if hasattr(self, "last_sent_url") else None)!s}, '
                f'successful={(self.successful if hasattr(self, "successful") else None)!s}, '
                f'body={(self.body if hasattr(self, "body") else None)!s}, '
                f'signature={(self.signature if hasattr(self, "signature") else None)!s}, '
                f'signature_hmac_sha_256={(self.signature_hmac_sha_256 if hasattr(self, "signature_hmac_sha_256") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
