// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace KomminarLabs.InfluxDB.Inputs
{

    public sealed class AuthorizationPermissionResourceGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A resource ID. Identifies a specific resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the resource. **Note:** not all resource types have a name property.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// An organization name. The organization that owns the resource.
        /// </summary>
        [Input("org")]
        public Input<string>? Org { get; set; }

        /// <summary>
        /// An organization ID. Identifies the organization that owns the resource.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// A resource type. Identifies the API resource's type (or kind).
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public AuthorizationPermissionResourceGetArgs()
        {
        }
        public static new AuthorizationPermissionResourceGetArgs Empty => new AuthorizationPermissionResourceGetArgs();
    }
}
