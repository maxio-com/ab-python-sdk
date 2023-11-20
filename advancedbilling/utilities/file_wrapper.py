# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.types.file_wrapper import FileWrapper


class FileWrapper(FileWrapper):
    """A wrapper to allow passing in content type for file uploads."""

    def __init__(self, file, content_type='application/octet-stream'):
        super().__init__(file, content_type)
