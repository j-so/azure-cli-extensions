# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ImpactType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The impact type
    """

    NONE = "None"
    FREEZE = "Freeze"
    RESTART = "Restart"
    REDEPLOY = "Redeploy"

class MaintenanceScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets maintenanceScope of the configuration
    """

    ALL = "All"
    HOST = "Host"
    RESOURCE = "Resource"
    IN_RESOURCE = "InResource"
    OS_IMAGE = "OSImage"
    EXTENSION = "Extension"
    IN_GUEST_PATCH = "InGuestPatch"
    SQLDB = "SQLDB"
    SQL_MANAGED_INSTANCE = "SQLManagedInstance"

class UpdateStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status
    """

    PENDING = "Pending"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    RETRY_NOW = "RetryNow"
    RETRY_LATER = "RetryLater"

class Visibility(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the visibility of the configuration
    """

    CUSTOM = "Custom"
    PUBLIC = "Public"
