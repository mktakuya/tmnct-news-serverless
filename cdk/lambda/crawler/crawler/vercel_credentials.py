import boto3

from crawler.settings import Settings


settings = Settings()


def get_vercel_webhook_url():
    if settings.VERCEL_CREDENTIALS_KEY_PREFIX == "":
        return {
            "VERCEL_WEBHOOK_URL": "",
        }

    ssm = boto3.client("ssm", region_name="ap-northeast-1")

    vercel_webhook_url = ssm.get_parameter(
        Name=f"{settings.VERCEL_CREDENTIALS_KEY_PREFIX}/vercel-webhook-url",
        WithDecryption=True
    )["Parameter"]["Value"]

    return {
        "VERCEL_WEBHOOK_URL": vercel_webhook_url,
    }
