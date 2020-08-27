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


class FitInfo(object):
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
        'amount': 'float',
        'max_fit_days': 'int',
        'originator_id': 'int',
        'originator_name': 'str',
        'pending_fit_interest': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'max_fit_days': 'maxFitDays',
        'originator_id': 'originatorId',
        'originator_name': 'originatorName',
        'pending_fit_interest': 'pendingFitInterest'
    }

    def __init__(self, amount=None, max_fit_days=None, originator_id=None, originator_name=None, pending_fit_interest=None):  # noqa: E501
        """FitInfo - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._max_fit_days = None
        self._originator_id = None
        self._originator_name = None
        self._pending_fit_interest = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if max_fit_days is not None:
            self.max_fit_days = max_fit_days
        if originator_id is not None:
            self.originator_id = originator_id
        if originator_name is not None:
            self.originator_name = originator_name
        if pending_fit_interest is not None:
            self.pending_fit_interest = pending_fit_interest

    @property
    def amount(self):
        """Gets the amount of this FitInfo.  # noqa: E501


        :return: The amount of this FitInfo.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FitInfo.


        :param amount: The amount of this FitInfo.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def max_fit_days(self):
        """Gets the max_fit_days of this FitInfo.  # noqa: E501


        :return: The max_fit_days of this FitInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_fit_days

    @max_fit_days.setter
    def max_fit_days(self, max_fit_days):
        """Sets the max_fit_days of this FitInfo.


        :param max_fit_days: The max_fit_days of this FitInfo.  # noqa: E501
        :type: int
        """

        self._max_fit_days = max_fit_days

    @property
    def originator_id(self):
        """Gets the originator_id of this FitInfo.  # noqa: E501


        :return: The originator_id of this FitInfo.  # noqa: E501
        :rtype: int
        """
        return self._originator_id

    @originator_id.setter
    def originator_id(self, originator_id):
        """Sets the originator_id of this FitInfo.


        :param originator_id: The originator_id of this FitInfo.  # noqa: E501
        :type: int
        """

        self._originator_id = originator_id

    @property
    def originator_name(self):
        """Gets the originator_name of this FitInfo.  # noqa: E501


        :return: The originator_name of this FitInfo.  # noqa: E501
        :rtype: str
        """
        return self._originator_name

    @originator_name.setter
    def originator_name(self, originator_name):
        """Sets the originator_name of this FitInfo.


        :param originator_name: The originator_name of this FitInfo.  # noqa: E501
        :type: str
        """

        self._originator_name = originator_name

    @property
    def pending_fit_interest(self):
        """Gets the pending_fit_interest of this FitInfo.  # noqa: E501


        :return: The pending_fit_interest of this FitInfo.  # noqa: E501
        :rtype: float
        """
        return self._pending_fit_interest

    @pending_fit_interest.setter
    def pending_fit_interest(self, pending_fit_interest):
        """Sets the pending_fit_interest of this FitInfo.


        :param pending_fit_interest: The pending_fit_interest of this FitInfo.  # noqa: E501
        :type: float
        """

        self._pending_fit_interest = pending_fit_interest

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
        if issubclass(FitInfo, dict):
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
        if not isinstance(other, FitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
