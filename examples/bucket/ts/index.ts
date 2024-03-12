import * as influxdb from "@komminarlabs/influxdb";

export const orgId = influxdb.getOrganizationOutput({ name: "default" }).id;

export const bucket = new influxdb.Bucket("signals", {
    orgId: orgId,
    name: "signals",
    description: "This is a bucket to store signals",
    retentionPeriod: 604800,
});

export const bucketId = bucket.id;

console.log(`Bucket ID: {bucketId}`);
