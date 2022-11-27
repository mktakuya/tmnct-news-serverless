import os
import requests

from crawler.models import News
from crawler.domains.services import NotifyNewsService
from crawler.utils.twitter import TwitterClient


class TweetNewsService(NotifyNewsService):
    def __init__(self, news: News, twitter_client: TwitterClient):
        super().__init__(news)
        self.twitter_client = twitter_client

    def notify(self) -> None:
        tweet_body = self.__build_tweet_body()
        image_paths = self.__download_images()
        self.twitter_client.tweet(tweet_body, image_paths)

    def __build_tweet_body(self):
        return (
                f"{self.news.title}\n" +
                f"{self.news.short_url()} #苫小牧高専"
        )

    def __download_images(self) -> list[str]:
        image_paths = []

        for i, url in enumerate(self.news.image_urls()):
            response = requests.get(url)
            if response.status_code != 200:
                continue

            image_data = response.content

            image_dir = f"/tmp/{self.news.slug}"
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            image_path = f"{image_dir}/{i}.jpg"
            with open(image_path, "wb") as f:
                f.write(image_data)

            image_paths.append(image_path)

        return image_paths
