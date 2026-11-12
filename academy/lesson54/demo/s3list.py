import boto3
from moto import mock_aws

BUCKET = "devops-demo"

@mock_aws
def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=BUCKET)
    for k in ("app.log", "db.log", "notes.txt"):
        s3.put_object(Bucket=BUCKET, Key=k, Body=k.encode() * 50)
    r = s3.list_objects_v2(Bucket=BUCKET)
    for o in r["Contents"]:
        print(o["Key"], o["Size"])

main()
