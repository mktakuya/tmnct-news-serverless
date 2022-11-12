import os


class Settings(object):
    DEFAULT_NEWS_FEED_URL = "https://www.tomakomai-ct.ac.jp/feed"
    DEFAULT_S3_BUCKET_NAME = "tmnct-news-crawler-local"

    # Singleton
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # By environ
        self.NEWS_FEED_URL = os.getenv("NEWS_FEED_URL", self.DEFAULT_NEWS_FEED_URL)
        self.S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", self.DEFAULT_S3_BUCKET_NAME)
