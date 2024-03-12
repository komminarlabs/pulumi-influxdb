// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace KomminarLabs.InfluxDB
{
    public static class GetOrganization
    {
        /// <summary>
        /// Retrieves an organization. Use this data source to retrieve information for a specific organization.
        /// </summary>
        public static Task<GetOrganizationResult> InvokeAsync(GetOrganizationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationResult>("influxdb:index/getOrganization:getOrganization", args ?? new GetOrganizationArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves an organization. Use this data source to retrieve information for a specific organization.
        /// </summary>
        public static Output<GetOrganizationResult> Invoke(GetOrganizationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationResult>("influxdb:index/getOrganization:getOrganization", args ?? new GetOrganizationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrganizationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the organization.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOrganizationArgs()
        {
        }
        public static new GetOrganizationArgs Empty => new GetOrganizationArgs();
    }

    public sealed class GetOrganizationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the organization.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOrganizationInvokeArgs()
        {
        }
        public static new GetOrganizationInvokeArgs Empty => new GetOrganizationInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrganizationResult
    {
        /// <summary>
        /// Organization creation date.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The description of the organization.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// An organization ID.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the organization.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Last Organization update date.
        /// </summary>
        public readonly string UpdatedAt;

        [OutputConstructor]
        private GetOrganizationResult(
            string createdAt,

            string description,

            string id,

            string name,

            string updatedAt)
        {
            CreatedAt = createdAt;
            Description = description;
            Id = id;
            Name = name;
            UpdatedAt = updatedAt;
        }
    }
}
