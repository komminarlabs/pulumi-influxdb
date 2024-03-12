package shim

import (
	tfpf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/komminarlabs/terraform-provider-influxdb/internal/provider"
)

func NewProvider() tfpf.Provider {
	return provider.New("dev")()
}
