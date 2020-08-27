# swagger_client.AccountDashboardControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_time_transaction_summary_using_get**](AccountDashboardControllerApi.md#get_all_time_transaction_summary_using_get) | **GET** /api/ia/accounts/all-time-transaction-summary | Get all-time transaction summary for current client
[**get_expected_cash_flows_for_period_using_post**](AccountDashboardControllerApi.md#get_expected_cash_flows_for_period_using_post) | **POST** /api/ia/accounts/expected-cash-flows | Get the cash flows expected by the current client for the next four weeks (28 days)
[**get_funds_in_transit_summary_by_loan_originator_using_post**](AccountDashboardControllerApi.md#get_funds_in_transit_summary_by_loan_originator_using_post) | **POST** /api/ia/accounts/fit-summary | Get funds in transit summary by loan originator for current client
[**get_investment_summary_by_country_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_country_using_post) | **POST** /api/ia/accounts/investment-summary-by-country | Get investment summary by country for current client and given filter
[**get_investment_summary_by_interest_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_interest_using_post) | **POST** /api/ia/accounts/investment-summary-by-interest | Get investment summary by interest for current client and given filter
[**get_investment_summary_by_loan_originator_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_loan_originator_using_post) | **POST** /api/ia/accounts/investment-summary-by-loan-originator | Get investment summary by loan originator for current client and given filter
[**get_investment_summary_by_loan_status_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_loan_status_using_post) | **POST** /api/ia/accounts/investment-summary-by-loan-status | Get investment summary by loan status for current client and given filter
[**get_investment_summary_by_loan_type_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_loan_type_using_post) | **POST** /api/ia/accounts/investment-summary-by-loan-type | Get investment summary by loan type for current client and given filter
[**get_investment_summary_by_maturity_using_post**](AccountDashboardControllerApi.md#get_investment_summary_by_maturity_using_post) | **POST** /api/ia/accounts/investment-summary-by-maturity | Get investment summary by maturity for current client and given filter
[**get_outstanding_balance_using_get**](AccountDashboardControllerApi.md#get_outstanding_balance_using_get) | **GET** /api/ia/accounts/outstanding-balance | Get outstanding balance for current client
[**get_xirr_using_post**](AccountDashboardControllerApi.md#get_xirr_using_post) | **POST** /api/ia/accounts/xirr | Calculate XIRR for current client and given filter


# **get_all_time_transaction_summary_using_get**
> TransactionSummaryModel get_all_time_transaction_summary_using_get()

Get all-time transaction summary for current client

Returns transaction summary model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get all-time transaction summary for current client
    api_response = api_instance.get_all_time_transaction_summary_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_all_time_transaction_summary_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionSummaryModel**](TransactionSummaryModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expected_cash_flows_for_period_using_post**
> list[DailyCashFlowModel] get_expected_cash_flows_for_period_using_post()

Get the cash flows expected by the current client for the next four weeks (28 days)

Returns list of daily expected cash flow models, which include the principal, interest and total for each date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get the cash flows expected by the current client for the next four weeks (28 days)
    api_response = api_instance.get_expected_cash_flows_for_period_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_expected_cash_flows_for_period_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DailyCashFlowModel]**](DailyCashFlowModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funds_in_transit_summary_by_loan_originator_using_post**
> list[FitInfo] get_funds_in_transit_summary_by_loan_originator_using_post()

Get funds in transit summary by loan originator for current client

Returns list of funds in transit info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get funds in transit summary by loan originator for current client
    api_response = api_instance.get_funds_in_transit_summary_by_loan_originator_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_funds_in_transit_summary_by_loan_originator_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FitInfo]**](FitInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_country_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_country_using_post(filter)

Get investment summary by country for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by country for current client and given filter
    api_response = api_instance.get_investment_summary_by_country_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_country_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_interest_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_interest_using_post(filter)

Get investment summary by interest for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by interest for current client and given filter
    api_response = api_instance.get_investment_summary_by_interest_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_interest_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_loan_originator_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_loan_originator_using_post(filter)

Get investment summary by loan originator for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by loan originator for current client and given filter
    api_response = api_instance.get_investment_summary_by_loan_originator_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_loan_originator_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_loan_status_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_loan_status_using_post(filter)

Get investment summary by loan status for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by loan status for current client and given filter
    api_response = api_instance.get_investment_summary_by_loan_status_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_loan_status_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_loan_type_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_loan_type_using_post(filter)

Get investment summary by loan type for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by loan type for current client and given filter
    api_response = api_instance.get_investment_summary_by_loan_type_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_loan_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investment_summary_by_maturity_using_post**
> list[CategorizedInvestmentModel] get_investment_summary_by_maturity_using_post(filter)

Get investment summary by maturity for current client and given filter

Returns list of categorized investment models

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.InvestmentFilterModel() # InvestmentFilterModel | filter

try:
    # Get investment summary by maturity for current client and given filter
    api_response = api_instance.get_investment_summary_by_maturity_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_investment_summary_by_maturity_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestmentFilterModel**](InvestmentFilterModel.md)| filter | 

### Return type

[**list[CategorizedInvestmentModel]**](CategorizedInvestmentModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outstanding_balance_using_get**
> BalanceModel get_outstanding_balance_using_get()

Get outstanding balance for current client

Returns balance model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get outstanding balance for current client
    api_response = api_instance.get_outstanding_balance_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_outstanding_balance_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BalanceModel**](BalanceModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xirr_using_post**
> XirrModel get_xirr_using_post(filter)

Calculate XIRR for current client and given filter

Returns XIRR model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountDashboardControllerApi(swagger_client.ApiClient(configuration))
filter = swagger_client.XirrFilterModel() # XirrFilterModel | filter

try:
    # Calculate XIRR for current client and given filter
    api_response = api_instance.get_xirr_using_post(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDashboardControllerApi->get_xirr_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**XirrFilterModel**](XirrFilterModel.md)| filter | 

### Return type

[**XirrModel**](XirrModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

