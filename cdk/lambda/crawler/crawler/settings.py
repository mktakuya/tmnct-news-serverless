import os


class Settings(object):
    DEFAULT_NEWS_FEED_URL = "https://www.tomakomai-ct.ac.jp/feed"

    # Singleton
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # By environ
        self.NEWS_FEED_URL = os.getenv("NEWS_FEED_URL", self.DEFAULT_NEWS_FEED_URL)
