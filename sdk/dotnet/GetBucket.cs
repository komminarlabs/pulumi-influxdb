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
    public static class GetBucket
    {
        /// <summary>
        /// Retrieves a bucket. Use this data source to retrieve information for a specific bucket.
        /// </summary>
        public static Task<GetBucketResult> InvokeAsync(GetBucketArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBucketResult>("influxdb:index/getBucket:getBucket", args ?? new GetBucketArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves a bucket. Use this data source to retrieve information for a specific bucket.
        /// </summary>
        public static Output<GetBucketResult> Invoke(GetBucketInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBucketResult>("influxdb:index/getBucket:getBucket", args ?? new GetBucketInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBucketArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A Bucket name.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetBucketArgs()
        {
        }
        public static new GetBucketArgs Empty => new GetBucketArgs();
    }

    public sealed class GetBucketInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A Bucket name.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetBucketInvokeArgs()
        {
        }
        public static new GetBucketInvokeArgs Empty => new GetBucketInvokeArgs();
    }


    [OutputType]
    public sealed class GetBucketResult
    {
        /// <summary>
        /// Bucket creation date.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// A description of the bucket.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// A Bucket ID.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A Bucket name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// An organization ID.
        /// </summary>
        public readonly string OrgId;
        /// <summary>
        /// The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
        /// </summary>
        public readonly int RetentionPeriod;
        /// <summary>
        /// The Bucket type.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// Last bucket update date.
        /// </summary>
        public readonly string UpdatedAt;

        [OutputConstructor]
        private GetBucketResult(
            string createdAt,

            string description,

            string id,

            string name,

            string orgId,

            int retentionPeriod,

            string type,

            string updatedAt)
        {
            CreatedAt = createdAt;
            Description = description;
            Id = id;
            Name = name;
            OrgId = orgId;
            RetentionPeriod = retentionPeriod;
            Type = type;
            UpdatedAt = updatedAt;
        }
    }
}
