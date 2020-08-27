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
from swagger_client.api.authentication_controller_api import AuthenticationControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthenticationControllerApi(unittest.TestCase):
    """AuthenticationControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.authentication_controller_api.AuthenticationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate_using_post(self):
        """Test case for authenticate_using_post

        authenticate  # noqa: E501
        """
        pass

    def test_refresh_using_post(self):
        """Test case for refresh_using_post

        refresh  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
