// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/komminarlabs/pulumi-influxdb/sdk/go/influxdb/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// An InfluxDB token string
func GetToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "influxdb:token")
}

// The InfluxDB Cloud Dedicated server URL
func GetUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "influxdb:url")
}
