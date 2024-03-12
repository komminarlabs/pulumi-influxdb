package main

import (
	"github.com/pulumi/pulumi-terraform-bridge/pf/tfgen"

	influxdb "github.com/komminarlabs/pulumi-influxdb/provider"
)

func main() {
	tfgen.Main("influxdb", influxdb.Provider())
}
