# coding: utf-8

"""
    Investor API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.token import Token  # noqa: E501
from swagger_client.rest import ApiException


class TestToken(unittest.TestCase):
    """Token unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testToken(self):
        """Test Token"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.token.Token()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
