import tweepy

from crawler.settings import Settings
from crawler.credentials import get_twitter_credentials

settings = Settings()


class TwitterClient:
    def __init__(self):
        credentials = get_twitter_credentials()

        auth = tweepy.OAuthHandler(credentials["TWITTER_CONSUMER_KEY"], credentials["TWITTER_CONSUMER_SECRET"])
        auth.set_access_token(credentials["TWITTER_ACCESS_TOKEN"], credentials["TWITTER_ACCESS_TOKEN_SECRET"])

        self.api = tweepy.API(auth)

    def tweet(self, body: str, image_paths: list[str] = []):
        if len(image_paths) >= 1:
            media_ids = []

            for image_path in image_paths:
                media = self.api.simple_upload(image_path)
                media_ids.append(media.media_id)

            self.api.update_status(status=body, media_ids=media_ids)
        else:
            self.api.update_status(body)
