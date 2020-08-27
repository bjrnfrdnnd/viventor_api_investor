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


class LoanGraphDataModel(object):
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
        'company': 'str',
        'company_capital': 'float',
        'invested_capital': 'float',
        'not_invested_capital': 'float'
    }

    attribute_map = {
        'company': 'company',
        'company_capital': 'company_capital',
        'invested_capital': 'invested_capital',
        'not_invested_capital': 'not_invested_capital'
    }

    def __init__(self, company=None, company_capital=None, invested_capital=None, not_invested_capital=None):  # noqa: E501
        """LoanGraphDataModel - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._company_capital = None
        self._invested_capital = None
        self._not_invested_capital = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if company_capital is not None:
            self.company_capital = company_capital
        if invested_capital is not None:
            self.invested_capital = invested_capital
        if not_invested_capital is not None:
            self.not_invested_capital = not_invested_capital

    @property
    def company(self):
        """Gets the company of this LoanGraphDataModel.  # noqa: E501


        :return: The company of this LoanGraphDataModel.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this LoanGraphDataModel.


        :param company: The company of this LoanGraphDataModel.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def company_capital(self):
        """Gets the company_capital of this LoanGraphDataModel.  # noqa: E501


        :return: The company_capital of this LoanGraphDataModel.  # noqa: E501
        :rtype: float
        """
        return self._company_capital

    @company_capital.setter
    def company_capital(self, company_capital):
        """Sets the company_capital of this LoanGraphDataModel.


        :param company_capital: The company_capital of this LoanGraphDataModel.  # noqa: E501
        :type: float
        """

        self._company_capital = company_capital

    @property
    def invested_capital(self):
        """Gets the invested_capital of this LoanGraphDataModel.  # noqa: E501


        :return: The invested_capital of this LoanGraphDataModel.  # noqa: E501
        :rtype: float
        """
        return self._invested_capital

    @invested_capital.setter
    def invested_capital(self, invested_capital):
        """Sets the invested_capital of this LoanGraphDataModel.


        :param invested_capital: The invested_capital of this LoanGraphDataModel.  # noqa: E501
        :type: float
        """

        self._invested_capital = invested_capital

    @property
    def not_invested_capital(self):
        """Gets the not_invested_capital of this LoanGraphDataModel.  # noqa: E501


        :return: The not_invested_capital of this LoanGraphDataModel.  # noqa: E501
        :rtype: float
        """
        return self._not_invested_capital

    @not_invested_capital.setter
    def not_invested_capital(self, not_invested_capital):
        """Sets the not_invested_capital of this LoanGraphDataModel.


        :param not_invested_capital: The not_invested_capital of this LoanGraphDataModel.  # noqa: E501
        :type: float
        """

        self._not_invested_capital = not_invested_capital

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
        if issubclass(LoanGraphDataModel, dict):
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
        if not isinstance(other, LoanGraphDataModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
