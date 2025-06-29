# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'AuthorizationPermission',
    'AuthorizationPermissionResource',
    'GetAuthorizationPermissionResult',
    'GetAuthorizationPermissionResourceResult',
    'GetAuthorizationsAuthorizationResult',
    'GetAuthorizationsAuthorizationPermissionResult',
    'GetAuthorizationsAuthorizationPermissionResourceResult',
    'GetBucketsBucketResult',
    'GetOrganizationsOrganizationResult',
]

@pulumi.output_type
class AuthorizationPermission(dict):
    def __init__(__self__, *,
                 action: builtins.str,
                 resource: 'outputs.AuthorizationPermissionResource'):
        """
        :param builtins.str action: Permission action. Valid values are `read` or `write`.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> builtins.str:
        """
        Permission action. Valid values are `read` or `write`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> 'outputs.AuthorizationPermissionResource':
        return pulumi.get(self, "resource")


@pulumi.output_type
class AuthorizationPermissionResource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "orgId":
            suggest = "org_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthorizationPermissionResource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthorizationPermissionResource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthorizationPermissionResource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: builtins.str,
                 id: Optional[builtins.str] = None,
                 name: Optional[builtins.str] = None,
                 org: Optional[builtins.str] = None,
                 org_id: Optional[builtins.str] = None):
        """
        :param builtins.str type: A resource type. Identifies the API resource's type (or kind).
        :param builtins.str id: A resource ID. Identifies a specific resource.
        :param builtins.str name: The name of the resource. **Note:** not all resource types have a name property.
        :param builtins.str org: An organization name. The organization that owns the resource.
        :param builtins.str org_id: An organization ID. Identifies the organization that owns the resource.
        """
        pulumi.set(__self__, "type", type)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def id(self) -> Optional[builtins.str]:
        """
        A resource ID. Identifies a specific resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        """
        The name of the resource. **Note:** not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> Optional[builtins.str]:
        """
        An organization name. The organization that owns the resource.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[builtins.str]:
        """
        An organization ID. Identifies the organization that owns the resource.
        """
        return pulumi.get(self, "org_id")


@pulumi.output_type
class GetAuthorizationPermissionResult(dict):
    def __init__(__self__, *,
                 action: builtins.str,
                 resource: 'outputs.GetAuthorizationPermissionResourceResult'):
        """
        :param builtins.str action: Permission action.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> builtins.str:
        """
        Permission action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> 'outputs.GetAuthorizationPermissionResourceResult':
        return pulumi.get(self, "resource")


@pulumi.output_type
class GetAuthorizationPermissionResourceResult(dict):
    def __init__(__self__, *,
                 id: builtins.str,
                 name: builtins.str,
                 org: builtins.str,
                 org_id: builtins.str,
                 type: builtins.str):
        """
        :param builtins.str id: A resource ID. Identifies a specific resource.
        :param builtins.str name: The name of the resource. **Note:** not all resource types have a name property.
        :param builtins.str org: An organization name. The organization that owns the resource.
        :param builtins.str org_id: An organization ID. Identifies the organization that owns the resource.
        :param builtins.str type: A resource type. Identifies the API resource's type (or kind).
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "org", org)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        A resource ID. Identifies a specific resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource. **Note:** not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> builtins.str:
        """
        An organization name. The organization that owns the resource.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> builtins.str:
        """
        An organization ID. Identifies the organization that owns the resource.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetAuthorizationsAuthorizationResult(dict):
    def __init__(__self__, *,
                 created_at: builtins.str,
                 description: builtins.str,
                 id: builtins.str,
                 org: builtins.str,
                 org_id: builtins.str,
                 permissions: Sequence['outputs.GetAuthorizationsAuthorizationPermissionResult'],
                 status: builtins.str,
                 token: builtins.str,
                 updated_at: builtins.str,
                 user: builtins.str,
                 user_id: builtins.str):
        """
        :param builtins.str created_at: Authorizations creation date.
        :param builtins.str description: A description of the token.
        :param builtins.str id: The authorization ID.
        :param builtins.str org: An Organization name. Specifies the organization that owns the authorization.
        :param builtins.str org_id: An organization ID. Specifies the organization that owns the authorization.
        :param Sequence['GetAuthorizationsAuthorizationPermissionArgs'] permissions: A list of permissions for an authorization.
        :param builtins.str status: Status of the token.
        :param builtins.str token: The API token.
        :param builtins.str updated_at: Last Authorizations update date.
        :param builtins.str user: A user name. Specifies the user that the authorization is scoped to.
        :param builtins.str user_id: A user ID. Specifies the user that the authorization is scoped to.
        """
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "org", org)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "token", token)
        pulumi.set(__self__, "updated_at", updated_at)
        pulumi.set(__self__, "user", user)
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> builtins.str:
        """
        Authorizations creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        A description of the token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        The authorization ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def org(self) -> builtins.str:
        """
        An Organization name. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> builtins.str:
        """
        An organization ID. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetAuthorizationsAuthorizationPermissionResult']:
        """
        A list of permissions for an authorization.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def status(self) -> builtins.str:
        """
        Status of the token.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def token(self) -> builtins.str:
        """
        The API token.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> builtins.str:
        """
        Last Authorizations update date.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def user(self) -> builtins.str:
        """
        A user name. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> builtins.str:
        """
        A user ID. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user_id")


@pulumi.output_type
class GetAuthorizationsAuthorizationPermissionResult(dict):
    def __init__(__self__, *,
                 action: builtins.str,
                 resource: 'outputs.GetAuthorizationsAuthorizationPermissionResourceResult'):
        """
        :param builtins.str action: Permission action.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> builtins.str:
        """
        Permission action.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> 'outputs.GetAuthorizationsAuthorizationPermissionResourceResult':
        return pulumi.get(self, "resource")


@pulumi.output_type
class GetAuthorizationsAuthorizationPermissionResourceResult(dict):
    def __init__(__self__, *,
                 id: builtins.str,
                 name: builtins.str,
                 org: builtins.str,
                 org_id: builtins.str,
                 type: builtins.str):
        """
        :param builtins.str id: A resource ID. Identifies a specific resource.
        :param builtins.str name: The name of the resource. **Note:** not all resource types have a name property.
        :param builtins.str org: An organization name. The organization that owns the resource.
        :param builtins.str org_id: An organization ID. Identifies the organization that owns the resource.
        :param builtins.str type: A resource type. Identifies the API resource's type (or kind).
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "org", org)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        A resource ID. Identifies a specific resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the resource. **Note:** not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> builtins.str:
        """
        An organization name. The organization that owns the resource.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> builtins.str:
        """
        An organization ID. Identifies the organization that owns the resource.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetBucketsBucketResult(dict):
    def __init__(__self__, *,
                 created_at: builtins.str,
                 description: builtins.str,
                 id: builtins.str,
                 name: builtins.str,
                 org_id: builtins.str,
                 retention_period: builtins.int,
                 type: builtins.str,
                 updated_at: builtins.str):
        """
        :param builtins.str created_at: Bucket creation date.
        :param builtins.str description: A description of the bucket.
        :param builtins.str id: A Bucket ID.
        :param builtins.str name: A Bucket name.
        :param builtins.str org_id: An organization ID.
        :param builtins.int retention_period: The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
        :param builtins.str type: The Bucket type.
        :param builtins.str updated_at: Last bucket update date.
        """
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "retention_period", retention_period)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> builtins.str:
        """
        Bucket creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        A description of the bucket.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        A Bucket ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        A Bucket name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> builtins.str:
        """
        An organization ID.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> builtins.int:
        """
        The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
        """
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def type(self) -> builtins.str:
        """
        The Bucket type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> builtins.str:
        """
        Last bucket update date.
        """
        return pulumi.get(self, "updated_at")


@pulumi.output_type
class GetOrganizationsOrganizationResult(dict):
    def __init__(__self__, *,
                 created_at: builtins.str,
                 description: builtins.str,
                 id: builtins.str,
                 name: builtins.str,
                 updated_at: builtins.str):
        """
        :param builtins.str created_at: Organization creation date.
        :param builtins.str description: The description of the organization.
        :param builtins.str id: An organization ID.
        :param builtins.str name: The name of the organization.
        :param builtins.str updated_at: Last Organization update date.
        """
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> builtins.str:
        """
        Organization creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> builtins.str:
        """
        The description of the organization.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> builtins.str:
        """
        An organization ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> builtins.str:
        """
        The name of the organization.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> builtins.str:
        """
        Last Organization update date.
        """
        return pulumi.get(self, "updated_at")


