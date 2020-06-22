# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ApplicationOperations:
    """ApplicationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~desktop_virtualization_api_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        application_group_name: str,
        application_name: str,
        **kwargs
    ) -> "models.Application":
        """Get an application.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param application_name: The name of the application within the specified application group.
        :type application_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Application, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.Application
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Application"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Application', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        application_group_name: str,
        application_name: str,
        command_line_setting: Union[str, "models.CommandLineSetting"],
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        file_path: Optional[str] = None,
        command_line_arguments: Optional[str] = None,
        show_in_portal: Optional[bool] = None,
        icon_path: Optional[str] = None,
        icon_index: Optional[int] = None,
        **kwargs
    ) -> "models.Application":
        """Create or update an application.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param application_name: The name of the application within the specified application group.
        :type application_name: str
        :param command_line_setting: Specifies whether this published application can be launched with
         command line arguments provided by the client, command line arguments specified at publish
         time, or no command line arguments at all.
        :type command_line_setting: str or ~desktop_virtualization_api_client.models.CommandLineSetting
        :param description: Description of Application.
        :type description: str
        :param friendly_name: Friendly name of Application.
        :type friendly_name: str
        :param file_path: Specifies a path for the executable file for the application.
        :type file_path: str
        :param command_line_arguments: Command Line Arguments for Application.
        :type command_line_arguments: str
        :param show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access
         server.
        :type show_in_portal: bool
        :param icon_path: Path to icon.
        :type icon_path: str
        :param icon_index: Index of the icon.
        :type icon_index: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Application, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.Application
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Application"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _application = models.Application(description=description, friendly_name=friendly_name, file_path=file_path, command_line_setting=command_line_setting, command_line_arguments=command_line_arguments, show_in_portal=show_in_portal, icon_path=icon_path, icon_index=icon_index)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_application, 'Application')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Application', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Application', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        application_group_name: str,
        application_name: str,
        **kwargs
    ) -> None:
        """Remove an application.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param application_name: The name of the application within the specified application group.
        :type application_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}'}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        application_group_name: str,
        application_name: str,
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        file_path: Optional[str] = None,
        command_line_setting: Optional[Union[str, "models.CommandLineSetting"]] = None,
        command_line_arguments: Optional[str] = None,
        show_in_portal: Optional[bool] = None,
        icon_path: Optional[str] = None,
        icon_index: Optional[int] = None,
        **kwargs
    ) -> "models.Application":
        """Update an application.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :param application_name: The name of the application within the specified application group.
        :type application_name: str
        :param tags: tags to be updated.
        :type tags: dict[str, str]
        :param description: Description of Application.
        :type description: str
        :param friendly_name: Friendly name of Application.
        :type friendly_name: str
        :param file_path: Specifies a path for the executable file for the application.
        :type file_path: str
        :param command_line_setting: Specifies whether this published application can be launched with
         command line arguments provided by the client, command line arguments specified at publish
         time, or no command line arguments at all.
        :type command_line_setting: str or ~desktop_virtualization_api_client.models.CommandLineSetting
        :param command_line_arguments: Command Line Arguments for Application.
        :type command_line_arguments: str
        :param show_in_portal: Specifies whether to show the RemoteApp program in the RD Web Access
         server.
        :type show_in_portal: bool
        :param icon_path: Path to icon.
        :type icon_path: str
        :param icon_index: Index of the icon.
        :type icon_index: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Application, or the result of cls(response)
        :rtype: ~desktop_virtualization_api_client.models.Application
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Application"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _application = models.ApplicationPatch(tags=tags, description=description, friendly_name=friendly_name, file_path=file_path, command_line_setting=command_line_setting, command_line_arguments=command_line_arguments, show_in_portal=show_in_portal, icon_path=icon_path, icon_index=icon_index)
        api_version = "2019-12-10-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
            'applicationName': self._serialize.url("application_name", application_name, 'str', max_length=24, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if _application is not None:
            body_content = self._serialize.body(_application, 'ApplicationPatch')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Application', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications/{applicationName}'}  # type: ignore

    def list(
        self,
        resource_group_name: str,
        application_group_name: str,
        **kwargs
    ) -> AsyncIterable["models.ApplicationList"]:
        """List applications.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param application_group_name: The name of the application group.
        :type application_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ApplicationList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~desktop_virtualization_api_client.models.ApplicationList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-10-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'applicationGroupName': self._serialize.url("application_group_name", application_group_name, 'str', max_length=24, min_length=3),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ApplicationList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/applicationGroups/{applicationGroupName}/applications'}  # type: ignore
