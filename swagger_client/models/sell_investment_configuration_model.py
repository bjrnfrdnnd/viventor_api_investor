# coding: utf-8

"""
    Investor API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SellInvestmentConfigurationModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'max_discount': 'int',
        'max_premium': 'int'
    }

    attribute_map = {
        'max_discount': 'max_discount',
        'max_premium': 'max_premium'
    }

    def __init__(self, max_discount=None, max_premium=None):  # noqa: E501
        """SellInvestmentConfigurationModel - a model defined in Swagger"""  # noqa: E501

        self._max_discount = None
        self._max_premium = None
        self.discriminator = None

        if max_discount is not None:
            self.max_discount = max_discount
        if max_premium is not None:
            self.max_premium = max_premium

    @property
    def max_discount(self):
        """Gets the max_discount of this SellInvestmentConfigurationModel.  # noqa: E501


        :return: The max_discount of this SellInvestmentConfigurationModel.  # noqa: E501
        :rtype: int
        """
        return self._max_discount

    @max_discount.setter
    def max_discount(self, max_discount):
        """Sets the max_discount of this SellInvestmentConfigurationModel.


        :param max_discount: The max_discount of this SellInvestmentConfigurationModel.  # noqa: E501
        :type: int
        """

        self._max_discount = max_discount

    @property
    def max_premium(self):
        """Gets the max_premium of this SellInvestmentConfigurationModel.  # noqa: E501


        :return: The max_premium of this SellInvestmentConfigurationModel.  # noqa: E501
        :rtype: int
        """
        return self._max_premium

    @max_premium.setter
    def max_premium(self, max_premium):
        """Sets the max_premium of this SellInvestmentConfigurationModel.


        :param max_premium: The max_premium of this SellInvestmentConfigurationModel.  # noqa: E501
        :type: int
        """

        self._max_premium = max_premium

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SellInvestmentConfigurationModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SellInvestmentConfigurationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
