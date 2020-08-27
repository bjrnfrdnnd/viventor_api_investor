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


class ResetPasswordStep2Model(object):
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
        'code': 'str',
        'password': 'PasswordModel'
    }

    attribute_map = {
        'code': 'code',
        'password': 'password'
    }

    def __init__(self, code=None, password=None):  # noqa: E501
        """ResetPasswordStep2Model - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._password = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if password is not None:
            self.password = password

    @property
    def code(self):
        """Gets the code of this ResetPasswordStep2Model.  # noqa: E501


        :return: The code of this ResetPasswordStep2Model.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ResetPasswordStep2Model.


        :param code: The code of this ResetPasswordStep2Model.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def password(self):
        """Gets the password of this ResetPasswordStep2Model.  # noqa: E501


        :return: The password of this ResetPasswordStep2Model.  # noqa: E501
        :rtype: PasswordModel
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ResetPasswordStep2Model.


        :param password: The password of this ResetPasswordStep2Model.  # noqa: E501
        :type: PasswordModel
        """

        self._password = password

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
        if issubclass(ResetPasswordStep2Model, dict):
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
        if not isinstance(other, ResetPasswordStep2Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
