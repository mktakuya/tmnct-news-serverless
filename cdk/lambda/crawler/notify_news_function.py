import logging

# from crawler.settings import Settings
from crawler.usecases import notify_news_usecase
from crawler.infrastructures.adapters import NewsDataAdapter
from crawler.infrastructures.services import TweetNewsService, EmailNewsService


logger = logging.getLogger()
logger.setLevel(logging.INFO)


adapter = NewsDataAdapter()


def tweet_news_handler(event, _context):
    logger.info("Started lambda function as tweetNewsLambda with event: %s", event)

    # settings = Settings()

    service = TweetNewsService()

    news = adapter.transform(event)

    notify_news_usecase.notify_news(news=news, notifier=service)


def email_news_handler(event, _context):
    logger.info("Started lambda function as emailNewsLambda with event: %s", event)

    # settings = Settings()

    service = EmailNewsService()

    news = adapter.transform(event)

    notify_news_usecase.notify_news(news=news, notifier=service)
