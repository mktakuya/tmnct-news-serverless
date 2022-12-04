import unittest
from unittest.mock import MagicMock

from crawler.models import News
from crawler.infrastructures.services import TweetNewsService
from crawler.utils.twitter import TwitterClient

news = News(
    title="タイトル",
    wp_pid=1,
    url="https://example.com",
    pub_date="2020-01-01",
    category="news",
    content="内容",
    slug="slug",
)


class MockedTwitterClient(TwitterClient):
    def __init__(self):
        pass

    def tweet(self, body: str):
        pass


class TestTweetNewsService(unittest.TestCase):
    def test_notify(self):
        twitter_client = MockedTwitterClient()
        twitter_client.tweet = MagicMock()

        service = TweetNewsService(news=news, twitter_client=twitter_client)

        expected_body = "タイトル\nhttps://tmnct-news.m6a.jp/n/slug #苫小牧高専"

        service.notify()

        twitter_client.tweet.assert_called_once_with(expected_body, [])
