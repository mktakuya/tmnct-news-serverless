import tweepy

from crawler.settings import Settings
from crawler.twitter_credentials import get_twitter_credentials

settings = Settings()


class TwitterClient:
    def __init__(self):
        credentials = get_twitter_credentials()

        auth = tweepy.OAuthHandler(credentials["TWITTER_CONSUMER_KEY"], credentials["TWITTER_CONSUMER_SECRET"])
        auth.set_access_token(credentials["TWITTER_ACCESS_TOKEN"], credentials["TWITTER_ACCESS_TOKEN_SECRET"])

        self.api = tweepy.API(auth)

    def tweet(self, body: str):
        self.api.update_status(body)
