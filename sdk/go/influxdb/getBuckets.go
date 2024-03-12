// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package influxdb

import (
	"context"
	"reflect"

	"github.com/komminarlabs/pulumi-influxdb/sdk/go/influxdb/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Lists buckets. InfluxDB retrieves buckets owned by the organization associated with the authorization (API token).
func GetBuckets(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetBucketsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetBucketsResult
	err := ctx.Invoke("influxdb:index/getBuckets:getBuckets", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getBuckets.
type GetBucketsResult struct {
	Buckets []GetBucketsBucket `pulumi:"buckets"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}

func GetBucketsOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetBucketsResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetBucketsResult, error) {
		r, err := GetBuckets(ctx, opts...)
		var s GetBucketsResult
		if r != nil {
			s = *r
		}
		return s, err
	}).(GetBucketsResultOutput)
}

// A collection of values returned by getBuckets.
type GetBucketsResultOutput struct{ *pulumi.OutputState }

func (GetBucketsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetBucketsResult)(nil)).Elem()
}

func (o GetBucketsResultOutput) ToGetBucketsResultOutput() GetBucketsResultOutput {
	return o
}

func (o GetBucketsResultOutput) ToGetBucketsResultOutputWithContext(ctx context.Context) GetBucketsResultOutput {
	return o
}

func (o GetBucketsResultOutput) Buckets() GetBucketsBucketArrayOutput {
	return o.ApplyT(func(v GetBucketsResult) []GetBucketsBucket { return v.Buckets }).(GetBucketsBucketArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetBucketsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetBucketsResult) string { return v.Id }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetBucketsResultOutput{})
}
