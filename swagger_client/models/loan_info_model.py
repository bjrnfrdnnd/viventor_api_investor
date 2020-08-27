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


class LoanInfoModel(object):
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
        'available_capital_for_investment': 'float',
        'company': 'str',
        'country_code': 'str',
        'date_end': 'datetime',
        'days_buyback': 'int',
        'guarantee': 'bool',
        'initial_capital': 'float',
        'interest': 'float',
        'loan_id': 'int',
        'loan_payments_status': 'str',
        'loan_purpose': 'str',
        'loan_rating': 'str',
        'loan_type': 'str',
        'ltv': 'float',
        'remaining_capital_after_paid_quote': 'float',
        'remaining_loan_term': 'int',
        'request_date': 'datetime',
        'request_term': 'int',
        'total_invested': 'float'
    }

    attribute_map = {
        'available_capital_for_investment': 'available_capital_for_investment',
        'company': 'company',
        'country_code': 'country_code',
        'date_end': 'date_end',
        'days_buyback': 'days_buyback',
        'guarantee': 'guarantee',
        'initial_capital': 'initial_capital',
        'interest': 'interest',
        'loan_id': 'loan_id',
        'loan_payments_status': 'loan_payments_status',
        'loan_purpose': 'loan_purpose',
        'loan_rating': 'loan_rating',
        'loan_type': 'loan_type',
        'ltv': 'ltv',
        'remaining_capital_after_paid_quote': 'remaining_capital_after_paid_quote',
        'remaining_loan_term': 'remaining_loan_term',
        'request_date': 'request_date',
        'request_term': 'request_term',
        'total_invested': 'total_invested'
    }

    def __init__(self, available_capital_for_investment=None, company=None, country_code=None, date_end=None, days_buyback=None, guarantee=None, initial_capital=None, interest=None, loan_id=None, loan_payments_status=None, loan_purpose=None, loan_rating=None, loan_type=None, ltv=None, remaining_capital_after_paid_quote=None, remaining_loan_term=None, request_date=None, request_term=None, total_invested=None):  # noqa: E501
        """LoanInfoModel - a model defined in Swagger"""  # noqa: E501

        self._available_capital_for_investment = None
        self._company = None
        self._country_code = None
        self._date_end = None
        self._days_buyback = None
        self._guarantee = None
        self._initial_capital = None
        self._interest = None
        self._loan_id = None
        self._loan_payments_status = None
        self._loan_purpose = None
        self._loan_rating = None
        self._loan_type = None
        self._ltv = None
        self._remaining_capital_after_paid_quote = None
        self._remaining_loan_term = None
        self._request_date = None
        self._request_term = None
        self._total_invested = None
        self.discriminator = None

        if available_capital_for_investment is not None:
            self.available_capital_for_investment = available_capital_for_investment
        if company is not None:
            self.company = company
        if country_code is not None:
            self.country_code = country_code
        if date_end is not None:
            self.date_end = date_end
        if days_buyback is not None:
            self.days_buyback = days_buyback
        if guarantee is not None:
            self.guarantee = guarantee
        if initial_capital is not None:
            self.initial_capital = initial_capital
        if interest is not None:
            self.interest = interest
        if loan_id is not None:
            self.loan_id = loan_id
        if loan_payments_status is not None:
            self.loan_payments_status = loan_payments_status
        if loan_purpose is not None:
            self.loan_purpose = loan_purpose
        if loan_rating is not None:
            self.loan_rating = loan_rating
        if loan_type is not None:
            self.loan_type = loan_type
        if ltv is not None:
            self.ltv = ltv
        if remaining_capital_after_paid_quote is not None:
            self.remaining_capital_after_paid_quote = remaining_capital_after_paid_quote
        if remaining_loan_term is not None:
            self.remaining_loan_term = remaining_loan_term
        if request_date is not None:
            self.request_date = request_date
        if request_term is not None:
            self.request_term = request_term
        if total_invested is not None:
            self.total_invested = total_invested

    @property
    def available_capital_for_investment(self):
        """Gets the available_capital_for_investment of this LoanInfoModel.  # noqa: E501


        :return: The available_capital_for_investment of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._available_capital_for_investment

    @available_capital_for_investment.setter
    def available_capital_for_investment(self, available_capital_for_investment):
        """Sets the available_capital_for_investment of this LoanInfoModel.


        :param available_capital_for_investment: The available_capital_for_investment of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._available_capital_for_investment = available_capital_for_investment

    @property
    def company(self):
        """Gets the company of this LoanInfoModel.  # noqa: E501


        :return: The company of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this LoanInfoModel.


        :param company: The company of this LoanInfoModel.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def country_code(self):
        """Gets the country_code of this LoanInfoModel.  # noqa: E501


        :return: The country_code of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this LoanInfoModel.


        :param country_code: The country_code of this LoanInfoModel.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def date_end(self):
        """Gets the date_end of this LoanInfoModel.  # noqa: E501


        :return: The date_end of this LoanInfoModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this LoanInfoModel.


        :param date_end: The date_end of this LoanInfoModel.  # noqa: E501
        :type: datetime
        """

        self._date_end = date_end

    @property
    def days_buyback(self):
        """Gets the days_buyback of this LoanInfoModel.  # noqa: E501


        :return: The days_buyback of this LoanInfoModel.  # noqa: E501
        :rtype: int
        """
        return self._days_buyback

    @days_buyback.setter
    def days_buyback(self, days_buyback):
        """Sets the days_buyback of this LoanInfoModel.


        :param days_buyback: The days_buyback of this LoanInfoModel.  # noqa: E501
        :type: int
        """

        self._days_buyback = days_buyback

    @property
    def guarantee(self):
        """Gets the guarantee of this LoanInfoModel.  # noqa: E501


        :return: The guarantee of this LoanInfoModel.  # noqa: E501
        :rtype: bool
        """
        return self._guarantee

    @guarantee.setter
    def guarantee(self, guarantee):
        """Sets the guarantee of this LoanInfoModel.


        :param guarantee: The guarantee of this LoanInfoModel.  # noqa: E501
        :type: bool
        """

        self._guarantee = guarantee

    @property
    def initial_capital(self):
        """Gets the initial_capital of this LoanInfoModel.  # noqa: E501


        :return: The initial_capital of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._initial_capital

    @initial_capital.setter
    def initial_capital(self, initial_capital):
        """Sets the initial_capital of this LoanInfoModel.


        :param initial_capital: The initial_capital of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._initial_capital = initial_capital

    @property
    def interest(self):
        """Gets the interest of this LoanInfoModel.  # noqa: E501


        :return: The interest of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this LoanInfoModel.


        :param interest: The interest of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._interest = interest

    @property
    def loan_id(self):
        """Gets the loan_id of this LoanInfoModel.  # noqa: E501


        :return: The loan_id of this LoanInfoModel.  # noqa: E501
        :rtype: int
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this LoanInfoModel.


        :param loan_id: The loan_id of this LoanInfoModel.  # noqa: E501
        :type: int
        """

        self._loan_id = loan_id

    @property
    def loan_payments_status(self):
        """Gets the loan_payments_status of this LoanInfoModel.  # noqa: E501


        :return: The loan_payments_status of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._loan_payments_status

    @loan_payments_status.setter
    def loan_payments_status(self, loan_payments_status):
        """Sets the loan_payments_status of this LoanInfoModel.


        :param loan_payments_status: The loan_payments_status of this LoanInfoModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLOSED", "CURRENT", "DELAYED_1_30", "DELAYED_31_60", "DELAYED_60_PLUS"]  # noqa: E501
        if loan_payments_status not in allowed_values:
            raise ValueError(
                "Invalid value for `loan_payments_status` ({0}), must be one of {1}"  # noqa: E501
                .format(loan_payments_status, allowed_values)
            )

        self._loan_payments_status = loan_payments_status

    @property
    def loan_purpose(self):
        """Gets the loan_purpose of this LoanInfoModel.  # noqa: E501


        :return: The loan_purpose of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._loan_purpose

    @loan_purpose.setter
    def loan_purpose(self, loan_purpose):
        """Sets the loan_purpose of this LoanInfoModel.


        :param loan_purpose: The loan_purpose of this LoanInfoModel.  # noqa: E501
        :type: str
        """

        self._loan_purpose = loan_purpose

    @property
    def loan_rating(self):
        """Gets the loan_rating of this LoanInfoModel.  # noqa: E501


        :return: The loan_rating of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._loan_rating

    @loan_rating.setter
    def loan_rating(self, loan_rating):
        """Sets the loan_rating of this LoanInfoModel.


        :param loan_rating: The loan_rating of this LoanInfoModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_GUARANTEE", "BUYBACK", "PAYMENT_GUARANTEE", "BANK_GUARANTEE"]  # noqa: E501
        if loan_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `loan_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(loan_rating, allowed_values)
            )

        self._loan_rating = loan_rating

    @property
    def loan_type(self):
        """Gets the loan_type of this LoanInfoModel.  # noqa: E501


        :return: The loan_type of this LoanInfoModel.  # noqa: E501
        :rtype: str
        """
        return self._loan_type

    @loan_type.setter
    def loan_type(self, loan_type):
        """Sets the loan_type of this LoanInfoModel.


        :param loan_type: The loan_type of this LoanInfoModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["MORTGAGE", "CONSUMER", "INVOICE_FINANCING", "BUSINESS", "LINE_OF_CREDIT", "PAWNBROKING"]  # noqa: E501
        if loan_type not in allowed_values:
            raise ValueError(
                "Invalid value for `loan_type` ({0}), must be one of {1}"  # noqa: E501
                .format(loan_type, allowed_values)
            )

        self._loan_type = loan_type

    @property
    def ltv(self):
        """Gets the ltv of this LoanInfoModel.  # noqa: E501


        :return: The ltv of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._ltv

    @ltv.setter
    def ltv(self, ltv):
        """Sets the ltv of this LoanInfoModel.


        :param ltv: The ltv of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._ltv = ltv

    @property
    def remaining_capital_after_paid_quote(self):
        """Gets the remaining_capital_after_paid_quote of this LoanInfoModel.  # noqa: E501


        :return: The remaining_capital_after_paid_quote of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._remaining_capital_after_paid_quote

    @remaining_capital_after_paid_quote.setter
    def remaining_capital_after_paid_quote(self, remaining_capital_after_paid_quote):
        """Sets the remaining_capital_after_paid_quote of this LoanInfoModel.


        :param remaining_capital_after_paid_quote: The remaining_capital_after_paid_quote of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._remaining_capital_after_paid_quote = remaining_capital_after_paid_quote

    @property
    def remaining_loan_term(self):
        """Gets the remaining_loan_term of this LoanInfoModel.  # noqa: E501


        :return: The remaining_loan_term of this LoanInfoModel.  # noqa: E501
        :rtype: int
        """
        return self._remaining_loan_term

    @remaining_loan_term.setter
    def remaining_loan_term(self, remaining_loan_term):
        """Sets the remaining_loan_term of this LoanInfoModel.


        :param remaining_loan_term: The remaining_loan_term of this LoanInfoModel.  # noqa: E501
        :type: int
        """

        self._remaining_loan_term = remaining_loan_term

    @property
    def request_date(self):
        """Gets the request_date of this LoanInfoModel.  # noqa: E501


        :return: The request_date of this LoanInfoModel.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this LoanInfoModel.


        :param request_date: The request_date of this LoanInfoModel.  # noqa: E501
        :type: datetime
        """

        self._request_date = request_date

    @property
    def request_term(self):
        """Gets the request_term of this LoanInfoModel.  # noqa: E501


        :return: The request_term of this LoanInfoModel.  # noqa: E501
        :rtype: int
        """
        return self._request_term

    @request_term.setter
    def request_term(self, request_term):
        """Sets the request_term of this LoanInfoModel.


        :param request_term: The request_term of this LoanInfoModel.  # noqa: E501
        :type: int
        """

        self._request_term = request_term

    @property
    def total_invested(self):
        """Gets the total_invested of this LoanInfoModel.  # noqa: E501


        :return: The total_invested of this LoanInfoModel.  # noqa: E501
        :rtype: float
        """
        return self._total_invested

    @total_invested.setter
    def total_invested(self, total_invested):
        """Sets the total_invested of this LoanInfoModel.


        :param total_invested: The total_invested of this LoanInfoModel.  # noqa: E501
        :type: float
        """

        self._total_invested = total_invested

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
        if issubclass(LoanInfoModel, dict):
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
        if not isinstance(other, LoanInfoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other