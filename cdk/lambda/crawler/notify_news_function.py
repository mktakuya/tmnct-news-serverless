import logging
import requests

from crawler.usecases import notify_news_usecase
from crawler.infrastructures.adapters import NewsDataAdapter
from crawler.infrastructures.services import TweetNewsService, EmailNewsService
from crawler.utils.twitter import TwitterClient
from crawler.settings import Settings

from crawler.credentials import get_vercel_webhook_url

logger = logging.getLogger()
logger.setLevel(logging.INFO)

adapter = NewsDataAdapter()


settings = Settings()

if settings.CREDENTIALS_KEY_PREFIX != "":
    import sentry_sdk
    from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

    from crawler.credentials import get_sentry_dsn

    sentry_sdk.init(
        dsn=get_sentry_dsn(),
        integrations=[AwsLambdaIntegration(timeout_warning=True)],
        environment=settings.ENV,
        traces_sample_rate=1.0,
    )


def tweet_news_handler(event, _context):
    logger.info("Started lambda function as tweetNewsLambda with event: %s", event)

    news = adapter.transform(event)
    service = TweetNewsService(news=news, twitter_client=TwitterClient())

    notify_news_usecase.notify_news(notifier=service)


def email_news_handler(event, _context):
    logger.info("Started lambda function as emailNewsLambda with event: %s", event)

    news = adapter.transform(event)
    service = EmailNewsService(news)

    notify_news_usecase.notify_news(notifier=service)


# TODO: あとでちゃんと実装する
def ping_to_vercel_handler(event, _context):
    logger.info("Started lambda function as pingToVercelLambda with event: %s", event)

    result = get_vercel_webhook_url()
    webhook_url = result["VERCEL_WEBHOOK_URL"]

    if webhook_url != "":
        requests.post(webhook_url)
