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
from swagger_client.api.registration_controller_api import RegistrationControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRegistrationControllerApi(unittest.TestCase):
    """RegistrationControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.registration_controller_api.RegistrationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_confirm_using_post(self):
        """Test case for confirm_using_post

        Registration confirmation  # noqa: E501
        """
        pass

    def test_confirmation_resend_using_post(self):
        """Test case for confirmation_resend_using_post

        confirmationResend  # noqa: E501
        """
        pass

    def test_step1_using_post(self):
        """Test case for step1_using_post

        Registration first step  # noqa: E501
        """
        pass

    def test_step2_using_post(self):
        """Test case for step2_using_post

        Registration second step  # noqa: E501
        """
        pass

    def test_step3_using_post(self):
        """Test case for step3_using_post

        Registration third step  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
