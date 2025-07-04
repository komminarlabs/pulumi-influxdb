// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package influxdb

import (
	"context"
	"reflect"

	"github.com/komminarlabs/pulumi-influxdb/sdk/go/influxdb/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves a bucket. Use this data source to retrieve information for a specific bucket.
func LookupBucket(ctx *pulumi.Context, args *LookupBucketArgs, opts ...pulumi.InvokeOption) (*LookupBucketResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBucketResult
	err := ctx.Invoke("influxdb:index/getBucket:getBucket", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBucket.
type LookupBucketArgs struct {
	// A Bucket name.
	Name string `pulumi:"name"`
}

// A collection of values returned by getBucket.
type LookupBucketResult struct {
	// Bucket creation date.
	CreatedAt string `pulumi:"createdAt"`
	// A description of the bucket.
	Description string `pulumi:"description"`
	// A Bucket ID.
	Id string `pulumi:"id"`
	// A Bucket name.
	Name string `pulumi:"name"`
	// An organization ID.
	OrgId string `pulumi:"orgId"`
	// The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
	RetentionPeriod int `pulumi:"retentionPeriod"`
	// The Bucket type.
	Type string `pulumi:"type"`
	// Last bucket update date.
	UpdatedAt string `pulumi:"updatedAt"`
}

func LookupBucketOutput(ctx *pulumi.Context, args LookupBucketOutputArgs, opts ...pulumi.InvokeOption) LookupBucketResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupBucketResultOutput, error) {
			args := v.(LookupBucketArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("influxdb:index/getBucket:getBucket", args, LookupBucketResultOutput{}, options).(LookupBucketResultOutput), nil
		}).(LookupBucketResultOutput)
}

// A collection of arguments for invoking getBucket.
type LookupBucketOutputArgs struct {
	// A Bucket name.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupBucketOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketArgs)(nil)).Elem()
}

// A collection of values returned by getBucket.
type LookupBucketResultOutput struct{ *pulumi.OutputState }

func (LookupBucketResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketResult)(nil)).Elem()
}

func (o LookupBucketResultOutput) ToLookupBucketResultOutput() LookupBucketResultOutput {
	return o
}

func (o LookupBucketResultOutput) ToLookupBucketResultOutputWithContext(ctx context.Context) LookupBucketResultOutput {
	return o
}

// Bucket creation date.
func (o LookupBucketResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// A description of the bucket.
func (o LookupBucketResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.Description }).(pulumi.StringOutput)
}

// A Bucket ID.
func (o LookupBucketResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.Id }).(pulumi.StringOutput)
}

// A Bucket name.
func (o LookupBucketResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.Name }).(pulumi.StringOutput)
}

// An organization ID.
func (o LookupBucketResultOutput) OrgId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.OrgId }).(pulumi.StringOutput)
}

// The duration in seconds for how long data will be kept in the database. `0` represents infinite retention.
func (o LookupBucketResultOutput) RetentionPeriod() pulumi.IntOutput {
	return o.ApplyT(func(v LookupBucketResult) int { return v.RetentionPeriod }).(pulumi.IntOutput)
}

// The Bucket type.
func (o LookupBucketResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.Type }).(pulumi.StringOutput)
}

// Last bucket update date.
func (o LookupBucketResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBucketResultOutput{})
}
