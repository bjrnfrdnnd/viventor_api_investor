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
from swagger_client.api.loan_statistic_controller_api import LoanStatisticControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLoanStatisticControllerApi(unittest.TestCase):
    """LoanStatisticControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.loan_statistic_controller_api.LoanStatisticControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_count_by_country_using_get(self):
        """Test case for get_count_by_country_using_get

        getCountByCountry  # noqa: E501
        """
        pass

    def test_get_count_by_extended_using_get(self):
        """Test case for get_count_by_extended_using_get

        getCountByExtended  # noqa: E501
        """
        pass

    def test_get_count_by_originator_using_get(self):
        """Test case for get_count_by_originator_using_get

        getCountByOriginator  # noqa: E501
        """
        pass

    def test_get_count_by_rating_using_get(self):
        """Test case for get_count_by_rating_using_get

        getCountByRating  # noqa: E501
        """
        pass

    def test_get_count_by_status_using_get(self):
        """Test case for get_count_by_status_using_get

        getCountByStatus  # noqa: E501
        """
        pass

    def test_get_count_by_type_using_get(self):
        """Test case for get_count_by_type_using_get

        getCountByType  # noqa: E501
        """
        pass

    def test_get_loan_statistics_using_get(self):
        """Test case for get_loan_statistics_using_get

        getLoanStatistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
