import logging

from crawler.usecases import notify_news_usecase
from crawler.infrastructures.adapters import NewsDataAdapter
from crawler.infrastructures.services import TweetNewsService, EmailNewsService

logger = logging.getLogger()
logger.setLevel(logging.INFO)

adapter = NewsDataAdapter()


def tweet_news_handler(event, _context):
    logger.info("Started lambda function as tweetNewsLambda with event: %s", event)

    news = adapter.transform(event)
    service = TweetNewsService(news)

    notify_news_usecase.notify_news(notifier=service)


def email_news_handler(event, _context):
    logger.info("Started lambda function as emailNewsLambda with event: %s", event)

    news = adapter.transform(event)
    service = EmailNewsService(news)

    notify_news_usecase.notify_news(notifier=service)
