import boto3

from crawler.settings import Settings


settings = Settings()


def get_sentry_dsn():
    ssm = boto3.client("ssm", region_name="ap-northeast-1")

    sentry_dsn = ssm.get_parameter(
        Name=f"{settings.CREDENTIALS_KEY_PREFIX}/sentry-dsn",
        WithDecryption=True
    )["Parameter"]["Value"]

    return sentry_dsn
