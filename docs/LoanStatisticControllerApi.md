# swagger_client.LoanStatisticControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_count_by_country_using_get**](LoanStatisticControllerApi.md#get_count_by_country_using_get) | **GET** /api/ia/statistics/loan/country | getCountByCountry
[**get_count_by_extended_using_get**](LoanStatisticControllerApi.md#get_count_by_extended_using_get) | **GET** /api/ia/statistics/loan/extended | getCountByExtended
[**get_count_by_originator_using_get**](LoanStatisticControllerApi.md#get_count_by_originator_using_get) | **GET** /api/ia/statistics/loan/originator | getCountByOriginator
[**get_count_by_rating_using_get**](LoanStatisticControllerApi.md#get_count_by_rating_using_get) | **GET** /api/ia/statistics/loan/rating | getCountByRating
[**get_count_by_status_using_get**](LoanStatisticControllerApi.md#get_count_by_status_using_get) | **GET** /api/ia/statistics/loan/status | getCountByStatus
[**get_count_by_type_using_get**](LoanStatisticControllerApi.md#get_count_by_type_using_get) | **GET** /api/ia/statistics/loan/type | getCountByType
[**get_loan_statistics_using_get**](LoanStatisticControllerApi.md#get_loan_statistics_using_get) | **GET** /api/ia/statistics/loan | getLoanStatistics


# **get_count_by_country_using_get**
> dict(str, int) get_count_by_country_using_get()

getCountByCountry

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByCountry
    api_response = api_instance.get_count_by_country_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_country_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_by_extended_using_get**
> dict(str, int) get_count_by_extended_using_get()

getCountByExtended

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByExtended
    api_response = api_instance.get_count_by_extended_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_extended_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_by_originator_using_get**
> dict(str, int) get_count_by_originator_using_get()

getCountByOriginator

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByOriginator
    api_response = api_instance.get_count_by_originator_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_originator_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_by_rating_using_get**
> dict(str, int) get_count_by_rating_using_get()

getCountByRating

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByRating
    api_response = api_instance.get_count_by_rating_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_rating_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_by_status_using_get**
> dict(str, int) get_count_by_status_using_get()

getCountByStatus

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByStatus
    api_response = api_instance.get_count_by_status_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_status_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_by_type_using_get**
> dict(str, int) get_count_by_type_using_get()

getCountByType

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCountByType
    api_response = api_instance.get_count_by_type_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_count_by_type_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_statistics_using_get**
> list[LoanStatisticModel] get_loan_statistics_using_get(originator_ids, months=months)

getLoanStatistics

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
api_instance = swagger_client.LoanStatisticControllerApi(swagger_client.ApiClient(configuration))
originator_ids = [56] # list[int] | originatorIds
months = 6 # int | months (optional) (default to 6)

try:
    # getLoanStatistics
    api_response = api_instance.get_loan_statistics_using_get(originator_ids, months=months)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanStatisticControllerApi->get_loan_statistics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originator_ids** | [**list[int]**](int.md)| originatorIds | 
 **months** | **int**| months | [optional] [default to 6]

### Return type

[**list[LoanStatisticModel]**](LoanStatisticModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

