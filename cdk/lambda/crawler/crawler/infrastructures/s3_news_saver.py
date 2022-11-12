from crawler.domains import NewsSaver
from crawler.models import News

from crawler.utils import aws_s3


def _key(news) -> str:
    key = f"news/${news.wp_pid}.json"


class S3NewsSaver(NewsSaver):
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    # TODO: このメソッドの実装場所は要検討。そもそもNewsFetcher / NewsSaverは別に切り出さなくても良かったかも。
    def is_exists(self, news: News) -> bool:
        key = _key(news)
        return aws_s3.is_exists(self.bucket_name, key)

    def save(self, news: News) -> None:
        key = _key(news)
        aws_s3.put_object(self.bucket_name, key, news.to_json())

