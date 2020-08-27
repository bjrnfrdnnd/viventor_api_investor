# swagger_client.PasswordControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_using_post**](PasswordControllerApi.md#change_password_using_post) | **POST** /api/ia/clients/change-password | changePassword
[**reset_password_step1_using_post**](PasswordControllerApi.md#reset_password_step1_using_post) | **POST** /api/ia/clients/reset-password/step1 | resetPasswordStep1
[**reset_password_step2_using_post**](PasswordControllerApi.md#reset_password_step2_using_post) | **POST** /api/ia/clients/reset-password/step2 | resetPasswordStep2


# **change_password_using_post**
> change_password_using_post(model)

changePassword

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
api_instance = swagger_client.PasswordControllerApi(swagger_client.ApiClient(configuration))
model = swagger_client.ChangePasswordModel() # ChangePasswordModel | model

try:
    # changePassword
    api_instance.change_password_using_post(model)
except ApiException as e:
    print("Exception when calling PasswordControllerApi->change_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ChangePasswordModel**](ChangePasswordModel.md)| model | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_step1_using_post**
> reset_password_step1_using_post(model)

resetPasswordStep1

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
api_instance = swagger_client.PasswordControllerApi(swagger_client.ApiClient(configuration))
model = swagger_client.ResetPasswordStep1Model() # ResetPasswordStep1Model | model

try:
    # resetPasswordStep1
    api_instance.reset_password_step1_using_post(model)
except ApiException as e:
    print("Exception when calling PasswordControllerApi->reset_password_step1_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ResetPasswordStep1Model**](ResetPasswordStep1Model.md)| model | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_step2_using_post**
> reset_password_step2_using_post(model)

resetPasswordStep2

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
api_instance = swagger_client.PasswordControllerApi(swagger_client.ApiClient(configuration))
model = swagger_client.ResetPasswordStep2Model() # ResetPasswordStep2Model | model

try:
    # resetPasswordStep2
    api_instance.reset_password_step2_using_post(model)
except ApiException as e:
    print("Exception when calling PasswordControllerApi->reset_password_step2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ResetPasswordStep2Model**](ResetPasswordStep2Model.md)| model | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

