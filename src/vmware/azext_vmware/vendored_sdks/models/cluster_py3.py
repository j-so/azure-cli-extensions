# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class Cluster(Resource):
    """A cluster resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param sku: Required. The cluster SKU
    :type sku: ~vendored_sdks.models.Sku
    :param cluster_size: The cluster size
    :type cluster_size: int
    :ivar cluster_id: The identity
    :vartype cluster_id: int
    :ivar hosts: The hosts
    :vartype hosts: list[str]
    :ivar provisioning_state: The state of the cluster provisioning. Possible
     values include: 'Succeeded', 'Failed', 'Cancelled', 'Deleting', 'Updating'
    :vartype provisioning_state: str or
     ~vendored_sdks.models.ClusterProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'sku': {'required': True},
        'cluster_id': {'readonly': True},
        'hosts': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'cluster_size': {'key': 'properties.clusterSize', 'type': 'int'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'int'},
        'hosts': {'key': 'properties.hosts', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, sku, cluster_size: int=None, **kwargs) -> None:
        super(Cluster, self).__init__(**kwargs)
        self.sku = sku
        self.cluster_size = cluster_size
        self.cluster_id = None
        self.hosts = None
        self.provisioning_state = None
