import logging

from crawler.usecases import fetch_and_save_news_usecase
from crawler.infrastructures import NewsRepositoryImpl
from crawler.infrastructures import RssNewsFetcher
from crawler.infrastructures import S3NewsSaver
from crawler.settings import Settings


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


def handler(event, context):
    logging.info("Started lambda function as fetchNews with event: %s", event)

    fetcher = RssNewsFetcher(feed_url=settings.NEWS_FEED_URL)
    saver = S3NewsSaver(bucket_name=settings.S3_BUCKET_NAME)

    news_repository = NewsRepositoryImpl(fetcher=fetcher, saver=saver)
    result = fetch_and_save_news_usecase.fetch_and_save_news(news_repository=news_repository)

    return result.to_dict()


if __name__ == "__main__":
    handler({}, {})
