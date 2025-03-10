package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"
	p "github.com/komminarlabs/terraform-provider-influxdb/internal/provider"
)

func NewProvider(version string) provider.Provider {
	return p.New(version)()
}
