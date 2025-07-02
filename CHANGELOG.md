# Changelog

All notable changes to this project will automatically be documented in this file.

The format is based on vKeep a Changelog(https://keepachangelog.com/en/1.0.0/),
and this project adheres to vSemantic Versioning(https://semver.org/spec/v2.0.0.html).

## v1.5.0 - 2025-07-02

### What's Changed

* feat: add label, user, and task resources and datasources by @thulasirajkomminar in https://github.com/komminarlabs/pulumi-influxdb/pull/57

**Full Changelog**: https://github.com/komminarlabs/pulumi-influxdb/compare/v1.4.0...v1.5.0

## v1.4.0 - 2025-06-19

### What's Changed

* Files Sync From komminarlabs/github-workflows by @komminarlabs-bot in https://github.com/komminarlabs/pulumi-influxdb/pull/53
* feat: add dual authentication support with improved validation by @thulasirajkomminar in https://github.com/komminarlabs/pulumi-influxdb/pull/56

**Full Changelog**: https://github.com/komminarlabs/pulumi-influxdb/compare/v1.3.0...v1.4.0

## v1.2.2 - 2024-09-12

## Updated:

* Updated docs to include supported influxdb flavours.

## v1.2.1 - 2024-08-23

## Fixed:

* fixed overwriting the token value during read in `influxdb_authorization` resource.

## v1.2.0 - 2024-04-17

#### Updates

* Updated `influxdb_authorization` resource and made the `id` & `org_id` as optional in `permissions.resource` inline with Influx api.
* Updated `influxdb_authorization` resource and made the `name` as read-only in `permissions.resource`. This is due to how Influx api returns the response. This will be modified in the future versions.

## v1.0.2 - 2024-04-03

#### Changes

- Fixed broken docs link

#### Updates

- Bumped few go modules

## v1.0.1 - 2024-03-13

Initial release of the provider

#### New resources:

- `index/authorization.Authorization`
- `index/bucket.Bucket`
- `index/organization.Organization`

#### New functions:

- `index/getAuthorization.getAuthorization`
- `index/getAuthorizations.getAuthorizations`
- `index/getBucket.getBucket`
- `index/getBuckets.getBuckets`
- `index/getOrganization.getOrganization`
- `index/getOrganizations.getOrganizations`
