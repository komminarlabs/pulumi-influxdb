// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface AuthorizationPermission {
    /**
     * Permission action. Valid values are `read` or `write`.
     */
    action: string;
    resource: outputs.AuthorizationPermissionResource;
}

export interface AuthorizationPermissionResource {
    /**
     * A resource ID. Identifies a specific resource.
     */
    id: string;
    /**
     * The name of the resource. **Note:** not all resource types have a name property.
     */
    name: string;
    /**
     * An organization name. The organization that owns the resource.
     */
    org: string;
    /**
     * An organization ID. Identifies the organization that owns the resource.
     */
    orgId: string;
    /**
     * A resource type. Identifies the API resource's type (or kind).
     */
    type: string;
}

export interface GetAuthorizationPermission {
    /**
     * Permission action.
     */
    action: string;
    resource: outputs.GetAuthorizationPermissionResource;
}

export interface GetAuthorizationPermissionResource {
    /**
     * A resource ID. Identifies a specific resource.
     */
    id: string;
    /**
     * The name of the resource. Note: not all resource types have a name property.
     */
    name: string;
    /**
     * An organization name. The organization that owns the resource.
     */
    org: string;
    /**
     * An organization ID. Identifies the organization that owns the resource.
     */
    orgId: string;
    /**
     * A resource type. Identifies the API resource's type (or kind).
     */
    type: string;
}

export interface GetAuthorizationsAuthorization {
    /**
     * Authorizations creation date.
     */
    createdAt: string;
    /**
     * A description of the token.
     */
    description: string;
    /**
     * The authorization ID.
     */
    id: string;
    /**
     * An Organization name. Specifies the organization that owns the authorization.
     */
    org: string;
    /**
     * An organization ID. Specifies the organization that owns the authorization.
     */
    orgId: string;
    /**
     * A list of permissions for an authorization.
     */
    permissions: outputs.GetAuthorizationsAuthorizationPermission[];
    /**
     * Status of the token.
     */
    status: string;
    /**
     * The API token.
     */
    token: string;
    /**
     * Last Authorizations update date.
     */
    updatedAt: string;
    /**
     * A user name. Specifies the user that the authorization is scoped to.
     */
    user: string;
    /**
     * A user ID. Specifies the user that the authorization is scoped to.
     */
    userId: string;
}

export interface GetAuthorizationsAuthorizationPermission {
    /**
     * Permission action.
     */
    action: string;
    resource: outputs.GetAuthorizationsAuthorizationPermissionResource;
}

export interface GetAuthorizationsAuthorizationPermissionResource {
    /**
     * The authorization ID.
     */
    id: string;
    /**
     * The name of the resource. Note: not all resource types have a name property.
     */
    name: string;
    /**
     * An Organization name. Specifies the organization that owns the authorization.
     */
    org: string;
    /**
     * An organization ID. Specifies the organization that owns the authorization.
     */
    orgId: string;
    /**
     * A resource type. Identifies the API resource's type (or kind).
     */
    type: string;
}

export interface GetBucketsBucket {
    /**
     * Bucket creation date.
     */
    createdAt: string;
    /**
     * A description of the bucket.
     */
    description: string;
    /**
     * A Bucket ID.
     */
    id: string;
    /**
     * A Bucket name.
     */
    name: string;
    /**
     * An organization ID.
     */
    orgId: string;
    /**
     * The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
     */
    retentionPeriod: number;
    /**
     * The Bucket type.
     */
    type: string;
    /**
     * Last bucket update date.
     */
    updatedAt: string;
}

export interface GetOrganizationsOrganization {
    /**
     * Organization creation date.
     */
    createdAt: string;
    /**
     * The description of the organization.
     */
    description: string;
    /**
     * An organization ID.
     */
    id: string;
    /**
     * The name of the organization.
     */
    name: string;
    /**
     * Last Organization update date.
     */
    updatedAt: string;
}

