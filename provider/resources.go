package influxdb

import (
	"fmt"
	"path"

	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"

	influxdbshim "github.com/komminarlabs/terraform-provider-influxdb/shim"

	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"

	// Import custom shim
	"github.com/komminarlabs/pulumi-influxdb/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "influxdb"
	// modules:
	mainMod = "index" // the influxdb module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(resource.PropertyMap, shim.ResourceConfig) error {
	return nil
}

//go:embed cmd/pulumi-resource-influxdb/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	prov := tfbridge.ProviderInfo{
		// Instantiate the Terraform provider
		P:                    pf.ShimProvider(influxdbshim.NewProvider()),
		Name:                 "influxdb",
		DisplayName:          "InfluxDB",
		Publisher:            "komminarlabs",
		Version:              version.Version,
		LogoURL:              "https://avatars.githubusercontent.com/u/5713248?s=200&v=4",
		PluginDownloadURL:    "github://api.github.com/komminarlabs",
		Description:          "A Pulumi package for creating and managing InfluxDB resources.",
		Keywords:             []string{"pulumi", "influxdb", "category/database"},
		License:              "Apache-2.0",
		Homepage:             "https://www.influxdata.com",
		Repository:           "https://github.com/komminarlabs/pulumi-influxdb",
		GitHubOrg:            "komminarlabs",
		MetadataInfo:         tfbridge.NewProviderMetadata(metadata),
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"influxdb_authorization": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Authorization")},
			"influxdb_bucket":        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Bucket")},
			"influxdb_organization":  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Organization")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"influxdb_authorization":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAuthorization")},
			"influxdb_authorizations": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAuthorizations")},
			"influxdb_bucket":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getBucket")},
			"influxdb_buckets":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getBuckets")},
			"influxdb_organization":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getOrganization")},
			"influxdb_organizations":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getOrganizations")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@komminarlabs/influxdb",
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0",
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "komminarlabs_influxdb",
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				fmt.Sprintf("github.com/komminarlabs/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "KomminarLabs",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: map[string]string{
				"influxdb": "InfluxDB",
			},
		},
	}

	prov.MustComputeTokens(tokens.SingleModule("influxdb_", mainMod,
		tokens.MakeStandard(mainPkg)))
	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}
