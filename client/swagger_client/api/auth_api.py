# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST` methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token` parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Most API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible.   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: hello@getoutline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def auth_config_post(self, **kwargs):  # noqa: E501
        """Retrieve auth config  # noqa: E501

        Retrieve authentication options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_config_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.auth_config_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.auth_config_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def auth_config_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve auth config  # noqa: E501

        Retrieve authentication options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_config_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
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
                    " to method auth_config_post" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['http']  # noqa: E501

        return self.api_client.call_api(
            '/auth.config', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def auth_info_post(self, **kwargs):  # noqa: E501
        """Retrieve auth  # noqa: E501

        Retrieve authentication details for the current API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_info_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.auth_info_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.auth_info_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def auth_info_post_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve auth  # noqa: E501

        Retrieve authentication details for the current API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_info_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
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
                    " to method auth_info_post" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['http']  # noqa: E501

        return self.api_client.call_api(
            '/auth.info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
