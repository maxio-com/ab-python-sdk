# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.types.file_wrapper import FileWrapper as CoreFileWrapper


class FileWrapper(CoreFileWrapper):
    """A wrapper to allow passing in content type for file uploads."""

    def __init__(self, file, content_type='application/octet-stream'):
        super().__init__(file, content_type)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'file={self._file_stream!r}, '
                f'content_type={self.content_type!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'file={self._file_stream!s}, '
                f'content_type={self.content_type!s})')
