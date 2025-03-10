//go:generate go run ./generate.go

package main

import (
	"context"
	_ "embed"

	influxdb "github.com/komminarlabs/pulumi-influxdb/provider"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
)

//go:embed schema.json
var pulumiSchema []byte

func main() {
	tfbridge.Main(context.Background(), "influxdb", influxdb.Provider(),
		tfbridge.ProviderMetadata{PackageSchema: pulumiSchema})
}
