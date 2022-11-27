from crawler.models import News
from crawler.domains.services import NotifyNewsService
from crawler.utils.twitter import TwitterClient


class TweetNewsService(NotifyNewsService):
    def __init__(self, news: News, twitter_client: TwitterClient):
        super().__init__(news)
        self.twitter_client = twitter_client

    def notify(self) -> None:
        tweet_body = self.__build_tweet_body()
        # TODO: 画像も対応する
        self.twitter_client.tweet(tweet_body)

    def __build_tweet_body(self):
        return (
                f"{self.news.title}\n" +
                f"{self.news.short_url()} #苫小牧高専"
        )
