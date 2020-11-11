# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import StorageManagementClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import StorageAccountsOperations
from .operations import DeletedAccountsOperations
from .operations import UsagesOperations
from .operations import ManagementPoliciesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ObjectReplicationPoliciesOperations
from .operations import EncryptionScopesOperations
from .operations import BlobServicesOperations
from .operations import BlobContainersOperations
from .operations import FileServicesOperations
from .operations import FileSharesOperations
from .operations import QueueServicesOperations
from .operations import QueueOperations
from .operations import TableServicesOperations
from .operations import TableOperations
from .. import models


class StorageManagementClient(object):
    """The Azure Storage Management API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2020_08_01_preview.aio.operations.Operations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.storage.v2020_08_01_preview.aio.operations.SkusOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts: azure.mgmt.storage.v2020_08_01_preview.aio.operations.StorageAccountsOperations
    :ivar deleted_accounts: DeletedAccountsOperations operations
    :vartype deleted_accounts: azure.mgmt.storage.v2020_08_01_preview.aio.operations.DeletedAccountsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.storage.v2020_08_01_preview.aio.operations.UsagesOperations
    :ivar management_policies: ManagementPoliciesOperations operations
    :vartype management_policies: azure.mgmt.storage.v2020_08_01_preview.aio.operations.ManagementPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.storage.v2020_08_01_preview.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.storage.v2020_08_01_preview.aio.operations.PrivateLinkResourcesOperations
    :ivar object_replication_policies: ObjectReplicationPoliciesOperations operations
    :vartype object_replication_policies: azure.mgmt.storage.v2020_08_01_preview.aio.operations.ObjectReplicationPoliciesOperations
    :ivar encryption_scopes: EncryptionScopesOperations operations
    :vartype encryption_scopes: azure.mgmt.storage.v2020_08_01_preview.aio.operations.EncryptionScopesOperations
    :ivar blob_services: BlobServicesOperations operations
    :vartype blob_services: azure.mgmt.storage.v2020_08_01_preview.aio.operations.BlobServicesOperations
    :ivar blob_containers: BlobContainersOperations operations
    :vartype blob_containers: azure.mgmt.storage.v2020_08_01_preview.aio.operations.BlobContainersOperations
    :ivar file_services: FileServicesOperations operations
    :vartype file_services: azure.mgmt.storage.v2020_08_01_preview.aio.operations.FileServicesOperations
    :ivar file_shares: FileSharesOperations operations
    :vartype file_shares: azure.mgmt.storage.v2020_08_01_preview.aio.operations.FileSharesOperations
    :ivar queue_services: QueueServicesOperations operations
    :vartype queue_services: azure.mgmt.storage.v2020_08_01_preview.aio.operations.QueueServicesOperations
    :ivar queue: QueueOperations operations
    :vartype queue: azure.mgmt.storage.v2020_08_01_preview.aio.operations.QueueOperations
    :ivar table_services: TableServicesOperations operations
    :vartype table_services: azure.mgmt.storage.v2020_08_01_preview.aio.operations.TableServicesOperations
    :ivar table: TableOperations operations
    :vartype table: azure.mgmt.storage.v2020_08_01_preview.aio.operations.TableOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_accounts = DeletedAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.object_replication_policies = ObjectReplicationPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.encryption_scopes = EncryptionScopesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_services = FileServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_shares = FileSharesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queue_services = QueueServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queue = QueueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table_services = TableServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.table = TableOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "StorageManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
