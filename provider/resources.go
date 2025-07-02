package influxdb

import (
	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"
	"fmt"
	"path"

	// Import custom shim
	"github.com/komminarlabs/pulumi-influxdb/provider/pkg/version"
	influxdbshim "github.com/komminarlabs/terraform-provider-influxdb/shim"

	pfbridge "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "influxdb"
	// modules:
	mainMod = "index" // the influxdb module
)

//go:embed cmd/pulumi-resource-influxdb/bridge-metadata.json
var bridgeMetadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	info := tfbridge.ProviderInfo{
		// Instantiate the Terraform provider
		P:                 pfbridge.ShimProvider(influxdbshim.NewProvider(version.Version)),
		Name:              "influxdb",
		DisplayName:       "InfluxDB",
		Publisher:         "komminarlabs",
		Version:           version.Version,
		LogoURL:           "https://avatars.githubusercontent.com/u/5713248?s=200&v=4",
		PluginDownloadURL: "github://api.github.com/komminarlabs",
		Description:       "A Pulumi package for creating and managing InfluxDB resources.",
		Keywords:          []string{"pulumi", "influxdb", "category/database"},
		License:           "Apache-2.0",
		Homepage:          "https://www.influxdata.com",
		Repository:        "https://github.com/komminarlabs/pulumi-influxdb",
		GitHubOrg:         "komminarlabs",
		MetadataInfo:      tfbridge.NewProviderMetadata(bridgeMetadata),
		Resources: map[string]*tfbridge.ResourceInfo{
			"influxdb_authorization": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Authorization")},
			"influxdb_bucket":        {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Bucket")},
			"influxdb_label":         {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Label")},
			"influxdb_organization":  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Organization")},
			"influxdb_task":          {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Task")},
			"influxdb_user":          {Tok: tfbridge.MakeResource(mainPkg, mainMod, "User")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"influxdb_authorization":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAuthorization")},
			"influxdb_authorizations": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAuthorizations")},
			"influxdb_bucket":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getBucket")},
			"influxdb_buckets":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getBuckets")},
			"influxdb_label":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getLabel")},
			"influxdb_labels":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getLabels")},
			"influxdb_organization":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getOrganization")},
			"influxdb_task":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTask")},
			"influxdb_tasks":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTasks")},
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

	info.MustComputeTokens(tokens.SingleModule("influxdb_", mainMod,
		tokens.MakeStandard(mainPkg)))
	info.MustApplyAutoAliases()
	info.SetAutonaming(255, "-")

	return info
}
