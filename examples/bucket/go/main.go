package main

import (
	"github.com/komminarlabs/pulumi-influxdb/sdk/go/influxdb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		org, err := influxdb.LookupOrganization(ctx, &influxdb.LookupOrganizationArgs{Name: "default"})
		if err != nil {
			return err
		}

		signals, err := influxdb.NewBucket(ctx, "signals", &influxdb.BucketArgs{
			OrgId:           pulumi.String(org.Id),
			Name:            pulumi.String("signals"),
			Description:     pulumi.String("Bucket for storing signal data"),
			RetentionPeriod: pulumi.Int(604800),
		})
		if err != nil {
			return err
		}

		ctx.Export("bucketId", signals.ID())
		return nil
	})
}
