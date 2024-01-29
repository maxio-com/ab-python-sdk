# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class MetafieldScope(object):

    """Implementation of the 'Metafield Scope' model.

    Warning: When updating a metafield's scope attribute, all scope attributes
    must be passed. Partially complete scope attributes will override the
    existing settings.

    Attributes:
        csv (IncludeOption): Include (1) or exclude (0) metafields from the
            csv export.
        invoices (IncludeOption): Include (1) or exclude (0) metafields from
            invoices.
        statements (IncludeOption): Include (1) or exclude (0) metafields from
            statements.
        portal (IncludeOption): Include (1) or exclude (0) metafields from the
            portal.
        public_show (IncludeOption): Include (1) or exclude (0) metafields
            from being viewable by your ecosystem.
        public_edit (IncludeOption): Include (1) or exclude (0) metafields
            from being edited by your ecosystem.
        hosted (List[str]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "csv": 'csv',
        "invoices": 'invoices',
        "statements": 'statements',
        "portal": 'portal',
        "public_show": 'public_show',
        "public_edit": 'public_edit',
        "hosted": 'hosted'
    }

    _optionals = [
        'csv',
        'invoices',
        'statements',
        'portal',
        'public_show',
        'public_edit',
        'hosted',
    ]

    def __init__(self,
                 csv=APIHelper.SKIP,
                 invoices=APIHelper.SKIP,
                 statements=APIHelper.SKIP,
                 portal=APIHelper.SKIP,
                 public_show=APIHelper.SKIP,
                 public_edit=APIHelper.SKIP,
                 hosted=APIHelper.SKIP):
        """Constructor for the MetafieldScope class"""

        # Initialize members of the class
        if csv is not APIHelper.SKIP:
            self.csv = csv 
        if invoices is not APIHelper.SKIP:
            self.invoices = invoices 
        if statements is not APIHelper.SKIP:
            self.statements = statements 
        if portal is not APIHelper.SKIP:
            self.portal = portal 
        if public_show is not APIHelper.SKIP:
            self.public_show = public_show 
        if public_edit is not APIHelper.SKIP:
            self.public_edit = public_edit 
        if hosted is not APIHelper.SKIP:
            self.hosted = hosted 

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
        csv = dictionary.get("csv") if dictionary.get("csv") else APIHelper.SKIP
        invoices = dictionary.get("invoices") if dictionary.get("invoices") else APIHelper.SKIP
        statements = dictionary.get("statements") if dictionary.get("statements") else APIHelper.SKIP
        portal = dictionary.get("portal") if dictionary.get("portal") else APIHelper.SKIP
        public_show = dictionary.get("public_show") if dictionary.get("public_show") else APIHelper.SKIP
        public_edit = dictionary.get("public_edit") if dictionary.get("public_edit") else APIHelper.SKIP
        hosted = dictionary.get("hosted") if dictionary.get("hosted") else APIHelper.SKIP
        # Return an object of this model
        return cls(csv,
                   invoices,
                   statements,
                   portal,
                   public_show,
                   public_edit,
                   hosted)

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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
