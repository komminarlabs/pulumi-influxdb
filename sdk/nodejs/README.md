# InfluxDB Resource Provider

The InfluxDB Resource Provider lets you manage [InfluxDB](https://www.influxdata.com/) resources.

## Supported InfluxDB flavours

### v3

* [InfluxDB Cloud Serverless](https://www.influxdata.com/products/influxdb-cloud/serverless/)

### v2

* [InfluxDB Cloud TSM](https://docs.influxdata.com/influxdb/cloud/)
* [InfluxDB OSS](https://docs.influxdata.com/influxdb/v2/)

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @komminarlabs/influxdb
```

or `yarn`:

```bash
yarn add @komminarlabs/influxdb
```

### Python

To use from Python, install using `pip`:

```bash
pip install komminarlabs_influxdb
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/komminarlabs/pulumi-influxdb/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package KomminarLabs.InfluxDB
```

## Configuration

The following configuration points are available for the `influxdb` provider:

- `influxdb:password` (environment: `INFLUXDB_PASSWORD`) - The InfluxDB password
- `influxdb:token` (environment: `INFLUXDB_TOKEN`) - An InfluxDB token string
- `influxdb:url` (environment: `INFLUXDB_URL`) - The InfluxDB Cloud Dedicated server URL
- `influxdb:username` (environment: `INFLUXDB_USERNAME`) - The InfluxDB username

## Authentication

The InfluxDB provider supports two [authentication methods](https://docs.influxdata.com/influxdb/v2/api/v2/#tag/Authentication):

* Token-based authentication (recommended).
* Username and password authentication.

### Authentication Priority

When both authentication methods are provided, **token authentication takes priority**. This means:

- If both `token` and `username`/`password` are configured, the provider will use token authentication
- Token authentication is the recommended method for better security and simplicity
- Username/password authentication is used only when no token is provided

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/influxdb/api-docs/).
