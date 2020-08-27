# swagger_client.StrategyControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_using_post**](StrategyControllerApi.md#activate_using_post) | **POST** /api/ia/strategies/{id}/activate | activate
[**count_matching_loans_using_post**](StrategyControllerApi.md#count_matching_loans_using_post) | **POST** /api/ia/strategies/loans/count | countMatchingLoans
[**create_using_post3**](StrategyControllerApi.md#create_using_post3) | **POST** /api/ia/strategies | create
[**delete_using_post**](StrategyControllerApi.md#delete_using_post) | **POST** /api/ia/strategies/{id}/delete | delete
[**read_using_get2**](StrategyControllerApi.md#read_using_get2) | **GET** /api/ia/strategies/{id} | read
[**read_using_get3**](StrategyControllerApi.md#read_using_get3) | **GET** /api/ia/strategies | read
[**stop_using_post**](StrategyControllerApi.md#stop_using_post) | **POST** /api/ia/strategies/{id}/stop | stop
[**update_using_post**](StrategyControllerApi.md#update_using_post) | **POST** /api/ia/strategies/{id} | update


# **activate_using_post**
> StrategyModel activate_using_post(id)

activate

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # activate
    api_response = api_instance.activate_using_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->activate_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**StrategyModel**](StrategyModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_matching_loans_using_post**
> int count_matching_loans_using_post(model)

countMatchingLoans

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
model = swagger_client.StrategyModel() # StrategyModel | model

try:
    # countMatchingLoans
    api_response = api_instance.count_matching_loans_using_post(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->count_matching_loans_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**StrategyModel**](StrategyModel.md)| model | 

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post3**
> StrategyModel create_using_post3(model)

create

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
model = swagger_client.StrategyModel() # StrategyModel | model

try:
    # create
    api_response = api_instance.create_using_post3(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->create_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**StrategyModel**](StrategyModel.md)| model | 

### Return type

[**StrategyModel**](StrategyModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_post**
> delete_using_post(id)

delete

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # delete
    api_instance.delete_using_post(id)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->delete_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_using_get2**
> StrategyModel read_using_get2(id)

read

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # read
    api_response = api_instance.read_using_get2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->read_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**StrategyModel**](StrategyModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_using_get3**
> list[StrategyListModel] read_using_get3()

read

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))

try:
    # read
    api_response = api_instance.read_using_get3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->read_using_get3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StrategyListModel]**](StrategyListModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_using_post**
> StrategyModel stop_using_post(id)

stop

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # stop
    api_response = api_instance.stop_using_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->stop_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**StrategyModel**](StrategyModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_post**
> StrategyModel update_using_post(id, model)

update

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
api_instance = swagger_client.StrategyControllerApi(swagger_client.ApiClient(configuration))
id = 789 # int | id
model = swagger_client.StrategyModel() # StrategyModel | model

try:
    # update
    api_response = api_instance.update_using_post(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StrategyControllerApi->update_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **model** | [**StrategyModel**](StrategyModel.md)| model | 

### Return type

[**StrategyModel**](StrategyModel.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

