# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class StandingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_standing_types(self, **kwargs):  # noqa: E501
        """Get all available NHL standing types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standing_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StandingTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_standing_types_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_standing_types_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_standing_types_with_http_info(self, **kwargs):  # noqa: E501
        """Get all available NHL standing types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standing_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StandingTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_standing_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/standingsTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandingTypes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_standings(self, **kwargs):  # noqa: E501
        """Get NHL division standings.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date season: Standings for a specified season.
        :param date date: Standings on a specified date.
        :return: Standings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_standings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_standings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_standings_with_http_info(self, **kwargs):  # noqa: E501
        """Get NHL division standings.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date season: Standings for a specified season.
        :param date date: Standings on a specified date.
        :return: Standings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['season', 'date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_standings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'season' in local_var_params:
            query_params.append(('season', local_var_params['season']))  # noqa: E501
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/standings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Standings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_standings_by_type(self, type, **kwargs):  # noqa: E501
        """Get NHL standings for a specific standing type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standings_by_type(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Standing types:   * `byConference` - Standings by Conference   * `byDivision` - Standings by Division   * `byLeague` - Standings by League   * `divisionLeaders` - Division Leader standings   * `postseason` - Postseason Standings   * `preseason` - Preseason Standings   * `regularSeason` - Regular Season Standings   * `wildCard` - Wild card standings   * `wildCardWithLeaders` - Wild card standings with Division Leaders  (required)
        :return: Standings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_standings_by_type_with_http_info(type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_standings_by_type_with_http_info(type, **kwargs)  # noqa: E501
            return data

    def get_standings_by_type_with_http_info(self, type, **kwargs):  # noqa: E501
        """Get NHL standings for a specific standing type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_standings_by_type_with_http_info(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Standing types:   * `byConference` - Standings by Conference   * `byDivision` - Standings by Division   * `byLeague` - Standings by League   * `divisionLeaders` - Division Leader standings   * `postseason` - Postseason Standings   * `preseason` - Preseason Standings   * `regularSeason` - Regular Season Standings   * `wildCard` - Wild card standings   * `wildCardWithLeaders` - Wild card standings with Division Leaders  (required)
        :return: Standings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_standings_by_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in local_var_params or
                local_var_params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_standings_by_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/standings/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Standings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
