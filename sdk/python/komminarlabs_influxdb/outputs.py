# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
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
                 action: str,
                 resource: 'outputs.AuthorizationPermissionResource'):
        """
        :param str action: Permission action. Valid values are `read` or `write`.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
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
                 id: str,
                 org_id: str,
                 type: str,
                 name: Optional[str] = None,
                 org: Optional[str] = None):
        """
        :param str id: A resource ID. Identifies a specific resource.
        :param str org_id: An organization ID. Identifies the organization that owns the resource.
        :param str type: A resource type. Identifies the API resource's type (or kind).
        :param str name: The name of the resource. **Note:** not all resource types have a name property.
        :param str org: An organization name. The organization that owns the resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        A resource ID. Identifies a specific resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        An organization ID. Identifies the organization that owns the resource.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource. **Note:** not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> Optional[str]:
        """
        An organization name. The organization that owns the resource.
        """
        return pulumi.get(self, "org")


@pulumi.output_type
class GetAuthorizationPermissionResult(dict):
    def __init__(__self__, *,
                 action: str,
                 resource: 'outputs.GetAuthorizationPermissionResourceResult'):
        """
        :param str action: Permission action.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
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
                 id: str,
                 name: str,
                 org: str,
                 org_id: str,
                 type: str):
        """
        :param str id: A resource ID. Identifies a specific resource.
        :param str name: The name of the resource. Note: not all resource types have a name property.
        :param str org: An organization name. The organization that owns the resource.
        :param str org_id: An organization ID. Identifies the organization that owns the resource.
        :param str type: A resource type. Identifies the API resource's type (or kind).
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "org", org)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        A resource ID. Identifies a specific resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource. Note: not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> str:
        """
        An organization name. The organization that owns the resource.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        An organization ID. Identifies the organization that owns the resource.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetAuthorizationsAuthorizationResult(dict):
    def __init__(__self__, *,
                 created_at: str,
                 description: str,
                 id: str,
                 org: str,
                 org_id: str,
                 permissions: Sequence['outputs.GetAuthorizationsAuthorizationPermissionResult'],
                 status: str,
                 token: str,
                 updated_at: str,
                 user: str,
                 user_id: str):
        """
        :param str created_at: Authorizations creation date.
        :param str description: A description of the token.
        :param str id: The authorization ID.
        :param str org: An Organization name. Specifies the organization that owns the authorization.
        :param str org_id: An organization ID. Specifies the organization that owns the authorization.
        :param Sequence['GetAuthorizationsAuthorizationPermissionArgs'] permissions: A list of permissions for an authorization.
        :param str status: Status of the token.
        :param str token: The API token.
        :param str updated_at: Last Authorizations update date.
        :param str user: A user name. Specifies the user that the authorization is scoped to.
        :param str user_id: A user ID. Specifies the user that the authorization is scoped to.
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
    def created_at(self) -> str:
        """
        Authorizations creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The authorization ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def org(self) -> str:
        """
        An Organization name. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
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
    def status(self) -> str:
        """
        Status of the token.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        The API token.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Last Authorizations update date.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def user(self) -> str:
        """
        A user name. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        A user ID. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user_id")


@pulumi.output_type
class GetAuthorizationsAuthorizationPermissionResult(dict):
    def __init__(__self__, *,
                 action: str,
                 resource: 'outputs.GetAuthorizationsAuthorizationPermissionResourceResult'):
        """
        :param str action: Permission action.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
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
                 id: str,
                 name: str,
                 org: str,
                 org_id: str,
                 type: str):
        """
        :param str id: The authorization ID.
        :param str name: The name of the resource. Note: not all resource types have a name property.
        :param str org: An Organization name. Specifies the organization that owns the authorization.
        :param str org_id: An organization ID. Specifies the organization that owns the authorization.
        :param str type: A resource type. Identifies the API resource's type (or kind).
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "org", org)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The authorization ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource. Note: not all resource types have a name property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> str:
        """
        An Organization name. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        An organization ID. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        A resource type. Identifies the API resource's type (or kind).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetBucketsBucketResult(dict):
    def __init__(__self__, *,
                 created_at: str,
                 description: str,
                 id: str,
                 name: str,
                 org_id: str,
                 retention_period: int,
                 type: str,
                 updated_at: str):
        """
        :param str created_at: Bucket creation date.
        :param str description: A description of the bucket.
        :param str id: A Bucket ID.
        :param str name: A Bucket name.
        :param str org_id: An organization ID.
        :param int retention_period: The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
        :param str type: The Bucket type.
        :param str updated_at: Last bucket update date.
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
    def created_at(self) -> str:
        """
        Bucket creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of the bucket.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        A Bucket ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A Bucket name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        An organization ID.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> int:
        """
        The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
        """
        return pulumi.get(self, "retention_period")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Bucket type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Last bucket update date.
        """
        return pulumi.get(self, "updated_at")


@pulumi.output_type
class GetOrganizationsOrganizationResult(dict):
    def __init__(__self__, *,
                 created_at: str,
                 description: str,
                 id: str,
                 name: str,
                 updated_at: str):
        """
        :param str created_at: Organization creation date.
        :param str description: The description of the organization.
        :param str id: An organization ID.
        :param str name: The name of the organization.
        :param str updated_at: Last Organization update date.
        """
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        Organization creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the organization.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An organization ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the organization.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        Last Organization update date.
        """
        return pulumi.get(self, "updated_at")


