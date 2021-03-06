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


class TransactionSummaryModel(object):
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
        'bonuses': 'float',
        'fit_interest': 'float',
        'funds_invested': 'float',
        'interest_received': 'float',
        'investments_made': 'int',
        'late_fee_received': 'float',
        'loan_parts_currently_held': 'int',
        'loans_repaid': 'int',
        'loans_sold_on_secondary_market': 'int',
        'normalized_xirr': 'float',
        'principal_repaid': 'float',
        'xirr': 'float'
    }

    attribute_map = {
        'bonuses': 'bonuses',
        'fit_interest': 'fit_interest',
        'funds_invested': 'funds_invested',
        'interest_received': 'interest_received',
        'investments_made': 'investments_made',
        'late_fee_received': 'late_fee_received',
        'loan_parts_currently_held': 'loan_parts_currently_held',
        'loans_repaid': 'loans_repaid',
        'loans_sold_on_secondary_market': 'loans_sold_on_secondary_market',
        'normalized_xirr': 'normalized_xirr',
        'principal_repaid': 'principal_repaid',
        'xirr': 'xirr'
    }

    def __init__(self, bonuses=None, fit_interest=None, funds_invested=None, interest_received=None, investments_made=None, late_fee_received=None, loan_parts_currently_held=None, loans_repaid=None, loans_sold_on_secondary_market=None, normalized_xirr=None, principal_repaid=None, xirr=None):  # noqa: E501
        """TransactionSummaryModel - a model defined in Swagger"""  # noqa: E501

        self._bonuses = None
        self._fit_interest = None
        self._funds_invested = None
        self._interest_received = None
        self._investments_made = None
        self._late_fee_received = None
        self._loan_parts_currently_held = None
        self._loans_repaid = None
        self._loans_sold_on_secondary_market = None
        self._normalized_xirr = None
        self._principal_repaid = None
        self._xirr = None
        self.discriminator = None

        if bonuses is not None:
            self.bonuses = bonuses
        if fit_interest is not None:
            self.fit_interest = fit_interest
        if funds_invested is not None:
            self.funds_invested = funds_invested
        if interest_received is not None:
            self.interest_received = interest_received
        if investments_made is not None:
            self.investments_made = investments_made
        if late_fee_received is not None:
            self.late_fee_received = late_fee_received
        if loan_parts_currently_held is not None:
            self.loan_parts_currently_held = loan_parts_currently_held
        if loans_repaid is not None:
            self.loans_repaid = loans_repaid
        if loans_sold_on_secondary_market is not None:
            self.loans_sold_on_secondary_market = loans_sold_on_secondary_market
        if normalized_xirr is not None:
            self.normalized_xirr = normalized_xirr
        if principal_repaid is not None:
            self.principal_repaid = principal_repaid
        if xirr is not None:
            self.xirr = xirr

    @property
    def bonuses(self):
        """Gets the bonuses of this TransactionSummaryModel.  # noqa: E501


        :return: The bonuses of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._bonuses

    @bonuses.setter
    def bonuses(self, bonuses):
        """Sets the bonuses of this TransactionSummaryModel.


        :param bonuses: The bonuses of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._bonuses = bonuses

    @property
    def fit_interest(self):
        """Gets the fit_interest of this TransactionSummaryModel.  # noqa: E501


        :return: The fit_interest of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._fit_interest

    @fit_interest.setter
    def fit_interest(self, fit_interest):
        """Sets the fit_interest of this TransactionSummaryModel.


        :param fit_interest: The fit_interest of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._fit_interest = fit_interest

    @property
    def funds_invested(self):
        """Gets the funds_invested of this TransactionSummaryModel.  # noqa: E501


        :return: The funds_invested of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._funds_invested

    @funds_invested.setter
    def funds_invested(self, funds_invested):
        """Sets the funds_invested of this TransactionSummaryModel.


        :param funds_invested: The funds_invested of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._funds_invested = funds_invested

    @property
    def interest_received(self):
        """Gets the interest_received of this TransactionSummaryModel.  # noqa: E501


        :return: The interest_received of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._interest_received

    @interest_received.setter
    def interest_received(self, interest_received):
        """Sets the interest_received of this TransactionSummaryModel.


        :param interest_received: The interest_received of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._interest_received = interest_received

    @property
    def investments_made(self):
        """Gets the investments_made of this TransactionSummaryModel.  # noqa: E501


        :return: The investments_made of this TransactionSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._investments_made

    @investments_made.setter
    def investments_made(self, investments_made):
        """Sets the investments_made of this TransactionSummaryModel.


        :param investments_made: The investments_made of this TransactionSummaryModel.  # noqa: E501
        :type: int
        """

        self._investments_made = investments_made

    @property
    def late_fee_received(self):
        """Gets the late_fee_received of this TransactionSummaryModel.  # noqa: E501


        :return: The late_fee_received of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._late_fee_received

    @late_fee_received.setter
    def late_fee_received(self, late_fee_received):
        """Sets the late_fee_received of this TransactionSummaryModel.


        :param late_fee_received: The late_fee_received of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._late_fee_received = late_fee_received

    @property
    def loan_parts_currently_held(self):
        """Gets the loan_parts_currently_held of this TransactionSummaryModel.  # noqa: E501


        :return: The loan_parts_currently_held of this TransactionSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._loan_parts_currently_held

    @loan_parts_currently_held.setter
    def loan_parts_currently_held(self, loan_parts_currently_held):
        """Sets the loan_parts_currently_held of this TransactionSummaryModel.


        :param loan_parts_currently_held: The loan_parts_currently_held of this TransactionSummaryModel.  # noqa: E501
        :type: int
        """

        self._loan_parts_currently_held = loan_parts_currently_held

    @property
    def loans_repaid(self):
        """Gets the loans_repaid of this TransactionSummaryModel.  # noqa: E501


        :return: The loans_repaid of this TransactionSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._loans_repaid

    @loans_repaid.setter
    def loans_repaid(self, loans_repaid):
        """Sets the loans_repaid of this TransactionSummaryModel.


        :param loans_repaid: The loans_repaid of this TransactionSummaryModel.  # noqa: E501
        :type: int
        """

        self._loans_repaid = loans_repaid

    @property
    def loans_sold_on_secondary_market(self):
        """Gets the loans_sold_on_secondary_market of this TransactionSummaryModel.  # noqa: E501


        :return: The loans_sold_on_secondary_market of this TransactionSummaryModel.  # noqa: E501
        :rtype: int
        """
        return self._loans_sold_on_secondary_market

    @loans_sold_on_secondary_market.setter
    def loans_sold_on_secondary_market(self, loans_sold_on_secondary_market):
        """Sets the loans_sold_on_secondary_market of this TransactionSummaryModel.


        :param loans_sold_on_secondary_market: The loans_sold_on_secondary_market of this TransactionSummaryModel.  # noqa: E501
        :type: int
        """

        self._loans_sold_on_secondary_market = loans_sold_on_secondary_market

    @property
    def normalized_xirr(self):
        """Gets the normalized_xirr of this TransactionSummaryModel.  # noqa: E501


        :return: The normalized_xirr of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._normalized_xirr

    @normalized_xirr.setter
    def normalized_xirr(self, normalized_xirr):
        """Sets the normalized_xirr of this TransactionSummaryModel.


        :param normalized_xirr: The normalized_xirr of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._normalized_xirr = normalized_xirr

    @property
    def principal_repaid(self):
        """Gets the principal_repaid of this TransactionSummaryModel.  # noqa: E501


        :return: The principal_repaid of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._principal_repaid

    @principal_repaid.setter
    def principal_repaid(self, principal_repaid):
        """Sets the principal_repaid of this TransactionSummaryModel.


        :param principal_repaid: The principal_repaid of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._principal_repaid = principal_repaid

    @property
    def xirr(self):
        """Gets the xirr of this TransactionSummaryModel.  # noqa: E501


        :return: The xirr of this TransactionSummaryModel.  # noqa: E501
        :rtype: float
        """
        return self._xirr

    @xirr.setter
    def xirr(self, xirr):
        """Sets the xirr of this TransactionSummaryModel.


        :param xirr: The xirr of this TransactionSummaryModel.  # noqa: E501
        :type: float
        """

        self._xirr = xirr

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
        if issubclass(TransactionSummaryModel, dict):
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
        if not isinstance(other, TransactionSummaryModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
