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


class ActivityAreaDescription(object):
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
        'description': 'str',
        'name': 'str',
        'occupation_required': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'occupation_required': 'occupation_required'
    }

    def __init__(self, description=None, name=None, occupation_required=None):  # noqa: E501
        """ActivityAreaDescription - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._occupation_required = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if occupation_required is not None:
            self.occupation_required = occupation_required

    @property
    def description(self):
        """Gets the description of this ActivityAreaDescription.  # noqa: E501


        :return: The description of this ActivityAreaDescription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActivityAreaDescription.


        :param description: The description of this ActivityAreaDescription.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ActivityAreaDescription.  # noqa: E501


        :return: The name of this ActivityAreaDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityAreaDescription.


        :param name: The name of this ActivityAreaDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def occupation_required(self):
        """Gets the occupation_required of this ActivityAreaDescription.  # noqa: E501


        :return: The occupation_required of this ActivityAreaDescription.  # noqa: E501
        :rtype: bool
        """
        return self._occupation_required

    @occupation_required.setter
    def occupation_required(self, occupation_required):
        """Sets the occupation_required of this ActivityAreaDescription.


        :param occupation_required: The occupation_required of this ActivityAreaDescription.  # noqa: E501
        :type: bool
        """

        self._occupation_required = occupation_required

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
        if issubclass(ActivityAreaDescription, dict):
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
        if not isinstance(other, ActivityAreaDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
