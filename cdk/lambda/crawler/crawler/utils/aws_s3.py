import boto3


def is_exists(bucket_name: str, key: str) -> bool:
    s3_client = boto3.Session().client("s3")
    contents = s3_client.list_objects(Prefix=key, Bucket=bucket_name).get("Contents")
    if contents:
        for content in contents:
            if content.get("Key") == key:
                return True
    return False


def put_object(bucket_name: str, key: str, body: str):
    s3 = boto3.resource("s3")
    s3.Object(bucket_name, key).put(Body=body)

