# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['redisenterprise operation-status'] = """
    type: group
    short-summary: Manage operation status with redisenterprise
"""

helps['redisenterprise operation-status show'] = """
    type: command
    short-summary: "Gets the status of operation."
    examples:
      - name: OperationsStatusGet
        text: |-
               az redisenterprise operation-status show --operation-id "testoperationid" --location "West US"
"""

helps['redisenterprise'] = """
    type: group
    short-summary: Manage redis enterprise with redisenterprise
"""

helps['redisenterprise list'] = """
    type: command
    short-summary: "Lists all RedisEnterprise clusters in a resource group. And Gets all RedisEnterprise clusters in \
the specified subscription."
    examples:
      - name: RedisEnterpriseListByResourceGroup
        text: |-
               az redisenterprise list --resource-group "rg1"
      - name: RedisEnterpriseList
        text: |-
               az redisenterprise list
"""

helps['redisenterprise show'] = """
    type: command
    short-summary: "Gets information about a RedisEnterprise cluster."
    examples:
      - name: RedisEnterpriseGet
        text: |-
               az redisenterprise show --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise create'] = """
    type: command
    short-summary: "Creates or updates an existing (overwrite/recreate, with potential downtime) cache cluster."
    examples:
      - name: RedisEnterpriseCreate
        text: |-
               az redisenterprise create --cluster-name "cache1" --location "West US" --minimum-tls-version "1.2" \
--sku "EnterpriseFlash_F300" --capacity 3 --tags tag1="value1" --zones "1" "2" "3" --resource-group "rg1"
"""

helps['redisenterprise update'] = """
    type: command
    short-summary: "Updates an existing RedisEnterprise cluster."
    examples:
      - name: RedisEnterpriseUpdate
        text: |-
               az redisenterprise update --cluster-name "cache1" --minimum-tls-version "1.2" --sku \
"EnterpriseFlash_F300" --capacity 9 --tags tag1="value1" --resource-group "rg1"
"""

helps['redisenterprise delete'] = """
    type: command
    short-summary: "Deletes a RedisEnterprise cache cluster."
    examples:
      - name: RedisEnterpriseDelete
        text: |-
               az redisenterprise delete --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the redisenterprise is met.
    examples:
      - name: Pause executing next line of CLI script until the redisenterprise is successfully created.
        text: |-
               az redisenterprise wait --cluster-name "cache1" --resource-group "rg1" --created
      - name: Pause executing next line of CLI script until the redisenterprise is successfully updated.
        text: |-
               az redisenterprise wait --cluster-name "cache1" --resource-group "rg1" --updated
      - name: Pause executing next line of CLI script until the redisenterprise is successfully deleted.
        text: |-
               az redisenterprise wait --cluster-name "cache1" --resource-group "rg1" --deleted
"""

helps['redisenterprise database'] = """
    type: group
    short-summary: Manage database with redisenterprise
"""

helps['redisenterprise database list'] = """
    type: command
    short-summary: "Gets all databases in the specified RedisEnterprise cluster."
    examples:
      - name: RedisEnterpriseDatabasesListByCluster
        text: |-
               az redisenterprise database list --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise database show'] = """
    type: command
    short-summary: "Gets information about a database in a RedisEnterprise cluster."
    examples:
      - name: RedisEnterpriseDatabasesGet
        text: |-
               az redisenterprise database show --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise database create'] = """
    type: command
    short-summary: "Creates a database."
    parameters:
      - name: --persistence
        short-summary: "Persistence settings"
        long-summary: |
            Usage: --persistence aof-enabled=XX rdb-enabled=XX aof-frequency=XX rdb-frequency=XX

            aof-enabled: Sets whether AOF is enabled.
            rdb-enabled: Sets whether RDB is enabled.
            aof-frequency: Sets the frequency at which data is written to disk.
            rdb-frequency: Sets the frequency at which a snapshot of the database is created.
      - name: --modules
        short-summary: "Optional set of redis modules to enable in this database - modules can only be added at \
creation time."
        long-summary: |
            Usage: --modules name=XX args=XX

            name: Required. The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
            args: Configuration options for the module, e.g. 'ERROR_RATE 0.00 INITIAL_SIZE 400'.

            Multiple actions can be specified by using more than one --modules argument.
    examples:
      - name: RedisEnterpriseDatabasesCreate
        text: |-
               az redisenterprise database create --cluster-name "cache1" --client-protocol "Encrypted" \
--clustering-policy "EnterpriseCluster" --eviction-policy "AllKeysLRU" --modules name="RedisBloom" args="ERROR_RATE \
0.00 INITIAL_SIZE 400" --modules name="RedisTimeSeries" args="RETENTION_POLICY 20" --modules name="RediSearch" \
--persistence aof-enabled=true aof-frequency="1s" --port 10000 --resource-group "rg1"
"""

helps['redisenterprise database update'] = """
    type: command
    short-summary: "Updates a database."
    parameters:
      - name: --persistence
        short-summary: "Persistence settings"
        long-summary: |
            Usage: --persistence aof-enabled=XX rdb-enabled=XX aof-frequency=XX rdb-frequency=XX

            aof-enabled: Sets whether AOF is enabled.
            rdb-enabled: Sets whether RDB is enabled.
            aof-frequency: Sets the frequency at which data is written to disk.
            rdb-frequency: Sets the frequency at which a snapshot of the database is created.
    examples:
      - name: RedisEnterpriseDatabasesUpdate
        text: |-
               az redisenterprise database update --cluster-name "cache1" --client-protocol "Encrypted" \
--eviction-policy "AllKeysLRU" --persistence rdb-enabled=true rdb-frequency="12h" --resource-group "rg1"
"""

helps['redisenterprise database delete'] = """
    type: command
    short-summary: "Deletes a single database."
    examples:
      - name: RedisEnterpriseDatabasesDelete
        text: |-
               az redisenterprise database delete --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise database export'] = """
    type: command
    short-summary: "Exports a database file from target database."
    examples:
      - name: RedisEnterpriseDatabasesExport
        text: |-
               az redisenterprise database export --cluster-name "cache1" --sas-uri "https://contosostorage.blob.core.w\
indow.net/urlToBlobContainer?sasKeyParameters" --resource-group "rg1"
"""

helps['redisenterprise database import'] = """
    type: command
    short-summary: "Imports a database file to target database."
    examples:
      - name: RedisEnterpriseDatabasesImport
        text: |-
               az redisenterprise database import --cluster-name "cache1" --sas-uri "https://contosostorage.blob.core.w\
indow.net/urltoBlobFile?sasKeyParameters" --resource-group "rg1"
"""

helps['redisenterprise database list-keys'] = """
    type: command
    short-summary: "Retrieves the access keys for the RedisEnterprise database."
    examples:
      - name: RedisEnterpriseDatabasesListKeys
        text: |-
               az redisenterprise database list-keys --cluster-name "cache1" --resource-group "rg1"
"""

helps['redisenterprise database regenerate-key'] = """
    type: command
    short-summary: "Regenerates the RedisEnterprise database's access keys."
    examples:
      - name: RedisEnterpriseDatabasesRegenerateKey
        text: |-
               az redisenterprise database regenerate-key --cluster-name "cache1" --key-type "Primary" \
--resource-group "rg1"
"""

helps['redisenterprise database wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the redisenterprise database is met.
    examples:
      - name: Pause executing next line of CLI script until the redisenterprise database is successfully created.
        text: |-
               az redisenterprise database wait --cluster-name "cache1" --resource-group "rg1" --created
      - name: Pause executing next line of CLI script until the redisenterprise database is successfully updated.
        text: |-
               az redisenterprise database wait --cluster-name "cache1" --resource-group "rg1" --updated
      - name: Pause executing next line of CLI script until the redisenterprise database is successfully deleted.
        text: |-
               az redisenterprise database wait --cluster-name "cache1" --resource-group "rg1" --deleted
"""
