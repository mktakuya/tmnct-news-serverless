import boto3

from crawler.settings import Settings


settings = Settings()


def get_twitter_credentials():
    ssm = boto3.client("ssm", region_name="ap-northeast-1")

    twitter_consumer_key = ssm.get_parameter(
        Name=f"{settings.TWITTER_CREDENTIALS_KEY_PREFIX}/twitter-consumer-key",
        WithDecryption=True
    )["Parameter"]["Value"]

    twitter_consumer_secret = ssm.get_parameter(
        Name=f"{settings.TWITTER_CREDENTIALS_KEY_PREFIX}/twitter-consumer-secret",
        WithDecryption=True
    )["Parameter"]["Value"]

    twitter_access_token = ssm.get_parameter(
        Name=f"{settings.TWITTER_CREDENTIALS_KEY_PREFIX}/twitter-access-token",
        WithDecryption=True
    )["Parameter"]["Value"]

    twitter_access_token_secret = ssm.get_parameter(
        Name=f"{settings.TWITTER_CREDENTIALS_KEY_PREFIX}/twitter-access-token-secret",
        WithDecryption=True
    )["Parameter"]["Value"]

    return {
        "TWITTER_CONSUMER_KEY": twitter_consumer_key,
        "TWITTER_CONSUMER_SECRET": twitter_consumer_secret,
        "TWITTER_ACCESS_TOKEN": twitter_access_token,
        "TWITTER_ACCESS_TOKEN_SECRET": twitter_access_token_secret,
    }
