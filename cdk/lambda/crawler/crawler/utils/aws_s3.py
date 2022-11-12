import boto3
import botocore


s3 = boto3.resource("s3")


def is_exists(bucket_name: str, key: str) -> bool:
    try:
        s3.Object(bucket_name, key).load()

        return True
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False
        else:
            raise e


def put_object(bucket_name: str, key: str, body: str):
    s3.Object(bucket_name, key).put(Body=body)

