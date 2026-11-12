import boto3
from botocore.exceptions import ClientError
from moto import mock_aws

@mock_aws
def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    try:
        s3.list_objects_v2(Bucket="no-such-bucket")
    except ClientError as e:
        print("caught:", e.response["Error"]["Code"])

main()
