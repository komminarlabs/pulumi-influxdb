# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

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
from ._inputs import *

__all__ = ['AuthorizationArgs', 'Authorization']

@pulumi.input_type
class AuthorizationArgs:
    def __init__(__self__, *,
                 org_id: pulumi.Input[str],
                 permissions: pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Authorization resource.
        :param pulumi.Input[str] org_id: An organization ID. Specifies the organization that owns the authorization.
        :param pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]] permissions: A list of permissions for an authorization.
        :param pulumi.Input[str] description: A description of the token.
        :param pulumi.Input[str] status: Status of the token. Valid values are `active` or `inactive`.
        :param pulumi.Input[str] user: A user name. Specifies the user that the authorization is scoped to.
        :param pulumi.Input[str] user_id: A user ID. Specifies the user that the authorization is scoped to.
        """
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "permissions", permissions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if user is not None:
            pulumi.set(__self__, "user", user)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        An organization ID. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]]:
        """
        A list of permissions for an authorization.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the token.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the token. Valid values are `active` or `inactive`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        A user name. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        A user ID. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _AuthorizationState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Authorization resources.
        :param pulumi.Input[str] created_at: Authorization creation date.
        :param pulumi.Input[str] description: A description of the token.
        :param pulumi.Input[str] org: Organization name. Specifies the organization that owns the authorization.
        :param pulumi.Input[str] org_id: An organization ID. Specifies the organization that owns the authorization.
        :param pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]] permissions: A list of permissions for an authorization.
        :param pulumi.Input[str] status: Status of the token. Valid values are `active` or `inactive`.
        :param pulumi.Input[str] token: The API token.
        :param pulumi.Input[str] updated_at: Last Authorization update date.
        :param pulumi.Input[str] user: A user name. Specifies the user that the authorization is scoped to.
        :param pulumi.Input[str] user_id: A user ID. Specifies the user that the authorization is scoped to.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if org is not None:
            pulumi.set(__self__, "org", org)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if user is not None:
            pulumi.set(__self__, "user", user)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization creation date.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the token.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        Organization name. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        An organization ID. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]]]:
        """
        A list of permissions for an authorization.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AuthorizationPermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the token. Valid values are `active` or `inactive`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The API token.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Last Authorization update date.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        A user name. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        A user ID. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class Authorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AuthorizationPermissionArgs', 'AuthorizationPermissionArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages an authorization and returns the authorization with the generated API token. Use this resource to create/manage an authorization, which generates an API token with permissions to read or write to a specific resource or type of resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the token.
        :param pulumi.Input[str] org_id: An organization ID. Specifies the organization that owns the authorization.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AuthorizationPermissionArgs', 'AuthorizationPermissionArgsDict']]]] permissions: A list of permissions for an authorization.
        :param pulumi.Input[str] status: Status of the token. Valid values are `active` or `inactive`.
        :param pulumi.Input[str] user: A user name. Specifies the user that the authorization is scoped to.
        :param pulumi.Input[str] user_id: A user ID. Specifies the user that the authorization is scoped to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages an authorization and returns the authorization with the generated API token. Use this resource to create/manage an authorization, which generates an API token with permissions to read or write to a specific resource or type of resource.

        :param str resource_name: The name of the resource.
        :param AuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AuthorizationPermissionArgs', 'AuthorizationPermissionArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizationArgs.__new__(AuthorizationArgs)

            __props__.__dict__["description"] = description
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["status"] = status
            __props__.__dict__["user"] = user
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["org"] = None
            __props__.__dict__["token"] = None
            __props__.__dict__["updated_at"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Authorization, __self__).__init__(
            'influxdb:index/authorization:Authorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            org: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AuthorizationPermissionArgs', 'AuthorizationPermissionArgsDict']]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'Authorization':
        """
        Get an existing Authorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: Authorization creation date.
        :param pulumi.Input[str] description: A description of the token.
        :param pulumi.Input[str] org: Organization name. Specifies the organization that owns the authorization.
        :param pulumi.Input[str] org_id: An organization ID. Specifies the organization that owns the authorization.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AuthorizationPermissionArgs', 'AuthorizationPermissionArgsDict']]]] permissions: A list of permissions for an authorization.
        :param pulumi.Input[str] status: Status of the token. Valid values are `active` or `inactive`.
        :param pulumi.Input[str] token: The API token.
        :param pulumi.Input[str] updated_at: Last Authorization update date.
        :param pulumi.Input[str] user: A user name. Specifies the user that the authorization is scoped to.
        :param pulumi.Input[str] user_id: A user ID. Specifies the user that the authorization is scoped to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AuthorizationState.__new__(_AuthorizationState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["org"] = org
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["status"] = status
        __props__.__dict__["token"] = token
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["user"] = user
        __props__.__dict__["user_id"] = user_id
        return Authorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Authorization creation date.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description of the token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def org(self) -> pulumi.Output[str]:
        """
        Organization name. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        An organization ID. Specifies the organization that owns the authorization.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence['outputs.AuthorizationPermission']]:
        """
        A list of permissions for an authorization.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the token. Valid values are `active` or `inactive`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The API token.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Last Authorization update date.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        A user name. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[Optional[str]]:
        """
        A user ID. Specifies the user that the authorization is scoped to.
        """
        return pulumi.get(self, "user_id")

