from crawler.domains import NewsSaver
from crawler.models import News

from crawler.utils import aws_s3


class S3NewsSaver(NewsSaver):
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def save(self, news: News) -> None:
        key = f"news/${news.wp_pid}.json"
        aws_s3.put_object(self.bucket_name, key, news.to_json())
