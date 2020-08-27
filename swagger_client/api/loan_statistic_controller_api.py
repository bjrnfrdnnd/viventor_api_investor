# coding: utf-8

"""
    Investor API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LoanStatisticControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_count_by_country_using_get(self, **kwargs):  # noqa: E501
        """getCountByCountry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_country_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_country_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_country_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_country_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByCountry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_country_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_country_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/country', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_by_extended_using_get(self, **kwargs):  # noqa: E501
        """getCountByExtended  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_extended_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_extended_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_extended_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_extended_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByExtended  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_extended_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_extended_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/extended', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_by_originator_using_get(self, **kwargs):  # noqa: E501
        """getCountByOriginator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_originator_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_originator_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_originator_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_originator_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByOriginator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_originator_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_originator_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/originator', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_by_rating_using_get(self, **kwargs):  # noqa: E501
        """getCountByRating  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_rating_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_rating_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_rating_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_rating_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByRating  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_rating_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_rating_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/rating', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_by_status_using_get(self, **kwargs):  # noqa: E501
        """getCountByStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_status_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_status_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_status_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_status_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_status_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_by_type_using_get(self, **kwargs):  # noqa: E501
        """getCountByType  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_type_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_by_type_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_count_by_type_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_count_by_type_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getCountByType  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_by_type_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, int)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_by_type_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan/type', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, int)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_loan_statistics_using_get(self, originator_ids, **kwargs):  # noqa: E501
        """getLoanStatistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loan_statistics_using_get(originator_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] originator_ids: originatorIds (required)
        :param int months: months
        :return: list[LoanStatisticModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_loan_statistics_using_get_with_http_info(originator_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_loan_statistics_using_get_with_http_info(originator_ids, **kwargs)  # noqa: E501
            return data

    def get_loan_statistics_using_get_with_http_info(self, originator_ids, **kwargs):  # noqa: E501
        """getLoanStatistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_loan_statistics_using_get_with_http_info(originator_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] originator_ids: originatorIds (required)
        :param int months: months
        :return: list[LoanStatisticModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['originator_ids', 'months']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_loan_statistics_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'originator_ids' is set
        if ('originator_ids' not in params or
                params['originator_ids'] is None):
            raise ValueError("Missing the required parameter `originator_ids` when calling `get_loan_statistics_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'originator_ids' in params:
            query_params.append(('originatorIds', params['originator_ids']))  # noqa: E501
            collection_formats['originatorIds'] = 'multi'  # noqa: E501
        if 'months' in params:
            query_params.append(('months', params['months']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/ia/statistics/loan', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LoanStatisticModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
