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
from swagger_client.api.strategy_controller_api import StrategyControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStrategyControllerApi(unittest.TestCase):
    """StrategyControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.strategy_controller_api.StrategyControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_using_post(self):
        """Test case for activate_using_post

        activate  # noqa: E501
        """
        pass

    def test_count_matching_loans_using_post(self):
        """Test case for count_matching_loans_using_post

        countMatchingLoans  # noqa: E501
        """
        pass

    def test_create_using_post3(self):
        """Test case for create_using_post3

        create  # noqa: E501
        """
        pass

    def test_delete_using_post(self):
        """Test case for delete_using_post

        delete  # noqa: E501
        """
        pass

    def test_read_using_get2(self):
        """Test case for read_using_get2

        read  # noqa: E501
        """
        pass

    def test_read_using_get3(self):
        """Test case for read_using_get3

        read  # noqa: E501
        """
        pass

    def test_stop_using_post(self):
        """Test case for stop_using_post

        stop  # noqa: E501
        """
        pass

    def test_update_using_post(self):
        """Test case for update_using_post

        update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
