import logging

from crawler.usecases import fetch_and_save_news_usecase
from crawler.infrastructures import NewsRepositoryImpl
from crawler.infrastructures import RssNewsFetcher
from crawler.infrastructures import S3NewsSaver
from crawler.settings import Settings


def handler(event, context):
    logging.info("Started lambda function as fetchNews with event: %s", event)

    settings = Settings()

    fetcher = RssNewsFetcher(feed_url=settings.NEWS_FEED_URL)
    saver = S3NewsSaver(bucket_name=settings.S3_BUCKET_NAME)

    news_repository = NewsRepositoryImpl(fetcher=fetcher, saver=saver)
    result = fetch_and_save_news_usecase.fetch_and_save_news(news_repository=news_repository)

    return result.to_dict()


if __name__ == "__main__":
    handler({}, {})
