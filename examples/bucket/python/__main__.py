"""A Python Pulumi program"""

import komminarlabs_influxdb as influxdb

org_id = influxdb.get_organization(name="default").id

bucket = influxdb.Bucket(
    "signals",
    org_id=org_id,
    name="signals",
    description="This is a bucket to store signals",
    retention_period=604800,
)
