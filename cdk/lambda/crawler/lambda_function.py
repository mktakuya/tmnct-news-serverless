import logging


def tweet_news_handler(event, context):
    logging.info('Started lambda function as tweetNews with event: %s', event)

    news = event['news']

    return news


def save_news_handler(event, context):
    logging.info('Started lambda function as saveNews with event: %s', event)

    return {
        "status": "OK"
    }


