// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package influxdb

import (
	"context"
	"reflect"

	"github.com/komminarlabs/pulumi-influxdb/sdk/go/influxdb/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Lists all authorizations.
func GetAuthorizations(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetAuthorizationsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetAuthorizationsResult
	err := ctx.Invoke("influxdb:index/getAuthorizations:getAuthorizations", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getAuthorizations.
type GetAuthorizationsResult struct {
	Authorizations []GetAuthorizationsAuthorization `pulumi:"authorizations"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}

func GetAuthorizationsOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetAuthorizationsResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetAuthorizationsResultOutput, error) {
		options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
		return ctx.InvokeOutput("influxdb:index/getAuthorizations:getAuthorizations", nil, GetAuthorizationsResultOutput{}, options).(GetAuthorizationsResultOutput), nil
	}).(GetAuthorizationsResultOutput)
}

// A collection of values returned by getAuthorizations.
type GetAuthorizationsResultOutput struct{ *pulumi.OutputState }

func (GetAuthorizationsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAuthorizationsResult)(nil)).Elem()
}

func (o GetAuthorizationsResultOutput) ToGetAuthorizationsResultOutput() GetAuthorizationsResultOutput {
	return o
}

func (o GetAuthorizationsResultOutput) ToGetAuthorizationsResultOutputWithContext(ctx context.Context) GetAuthorizationsResultOutput {
	return o
}

func (o GetAuthorizationsResultOutput) Authorizations() GetAuthorizationsAuthorizationArrayOutput {
	return o.ApplyT(func(v GetAuthorizationsResult) []GetAuthorizationsAuthorization { return v.Authorizations }).(GetAuthorizationsAuthorizationArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAuthorizationsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAuthorizationsResult) string { return v.Id }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAuthorizationsResultOutput{})
}
