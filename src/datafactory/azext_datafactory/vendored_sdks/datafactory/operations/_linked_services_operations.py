# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6225, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class LinkedServicesOperations(object):
    """LinkedServicesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_factory_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_factory(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.LinkedServiceListResponse"
        """Lists linked services.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceListResponse or the result of cls(response)
        :rtype: ~data_factory_management_client.models.LinkedServiceListResponse
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.LinkedServiceListResponse"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-06-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_factory.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
                    'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern='^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('LinkedServiceListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.CloudErrorException.from_response(response, self._deserialize)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices'}

    def create_or_update(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        linked_service_name,  # type: str
        type,  # type: str
        reference_name,  # type: str
        if_match=None,  # type: Optional[str]
        parameters=None,  # type: Optional[Dict[str, object]]
        description=None,  # type: Optional[str]
        parameters_properties=None,  # type: Optional[Dict[str, "ParameterSpecification"]]
        annotations=None,  # type: Optional[List["LinkedServiceAnnotationsItem"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.LinkedServiceResource"
        """Creates or updates a linked service.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param type: Type of linked service.
        :type type: str
        :param reference_name: Reference integration runtime name.
        :type reference_name: str
        :param if_match: ETag of the factory entity. Should only be specified for update, for which it
         should match existing entity or can be * for unconditional update.
        :type if_match: str
        :param parameters: An object mapping parameter names to argument values.
        :type parameters: dict[str, object]
        :param description: Linked service description.
        :type description: str
        :param parameters_properties: Definition of all parameters for an entity.
        :type parameters_properties: dict[str, ~data_factory_management_client.models.ParameterSpecification]
        :param annotations: List of tags that can be used for describing the linked service.
        :type annotations: list[~data_factory_management_client.models.LinkedServiceAnnotationsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceResource or the result of cls(response)
        :rtype: ~data_factory_management_client.models.LinkedServiceResource
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.LinkedServiceResource"]
        error_map = kwargs.pop('error_map', {})

        linked_service = models.LinkedServiceResource(type=type, reference_name=reference_name, parameters=parameters, description=description, parameters_properties=parameters_properties, annotations=annotations)
        api_version = "2018-06-01"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern='^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern='^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(linked_service, 'LinkedServiceResource')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName}'}

    def get(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        linked_service_name,  # type: str
        if_none_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.LinkedServiceResource"
        """Gets a linked service.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param if_none_match: ETag of the factory entity. Should only be specified for get. If the ETag
         matches the existing entity tag, or if * was provided, then no content will be returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceResource or  or the result of cls(response)
        :rtype: ~data_factory_management_client.models.LinkedServiceResource or None
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.LinkedServiceResource"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-06-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern='^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern='^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName}'}

    def delete(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        linked_service_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a linked service.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~data_factory_management_client.models.CloudErrorException:
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-06-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern='^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern='^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName}'}
