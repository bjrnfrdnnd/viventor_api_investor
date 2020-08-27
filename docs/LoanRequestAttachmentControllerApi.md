# swagger_client.LoanRequestAttachmentControllerApi

All URIs are relative to *https://api.viventor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_using_get13**](LoanRequestAttachmentControllerApi.md#list_using_get13) | **GET** /api/ia/clients/attachments/loan | list
[**upload_using_post2**](LoanRequestAttachmentControllerApi.md#upload_using_post2) | **POST** /api/ia/clients/attachments/loan | upload


# **list_using_get13**
> list[Attachment] list_using_get13()

list

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
api_instance = swagger_client.LoanRequestAttachmentControllerApi(swagger_client.ApiClient(configuration))

try:
    # list
    api_response = api_instance.list_using_get13()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoanRequestAttachmentControllerApi->list_using_get13: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Attachment]**](Attachment.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_using_post2**
> upload_using_post2(file)

upload

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
api_instance = swagger_client.LoanRequestAttachmentControllerApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | file

try:
    # upload
    api_instance.upload_using_post2(file)
except ApiException as e:
    print("Exception when calling LoanRequestAttachmentControllerApi->upload_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

