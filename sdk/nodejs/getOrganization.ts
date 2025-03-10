// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Retrieves an organization. Use this data source to retrieve information for a specific organization.
 */
export function getOrganization(args: GetOrganizationArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("influxdb:index/getOrganization:getOrganization", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationArgs {
    /**
     * The name of the organization.
     */
    name: string;
}

/**
 * A collection of values returned by getOrganization.
 */
export interface GetOrganizationResult {
    /**
     * Organization creation date.
     */
    readonly createdAt: string;
    /**
     * The description of the organization.
     */
    readonly description: string;
    /**
     * An organization ID.
     */
    readonly id: string;
    /**
     * The name of the organization.
     */
    readonly name: string;
    /**
     * Last Organization update date.
     */
    readonly updatedAt: string;
}
/**
 * Retrieves an organization. Use this data source to retrieve information for a specific organization.
 */
export function getOrganizationOutput(args: GetOrganizationOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetOrganizationResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("influxdb:index/getOrganization:getOrganization", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getOrganization.
 */
export interface GetOrganizationOutputArgs {
    /**
     * The name of the organization.
     */
    name: pulumi.Input<string>;
}
