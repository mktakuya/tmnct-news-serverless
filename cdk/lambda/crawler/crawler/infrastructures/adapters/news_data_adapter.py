from dateutil import parser

from crawler.domains.adapters import InputDataAdapter
from crawler.models import News


class NewsDataAdapter(InputDataAdapter):
    def transform(self, data: dict) -> News:
        return News(
            title=data["title"],
            wp_pid=data["wp_pid"],
            url=data["url"],
            pub_date=parser.parse(data["pub_date"]).date(),
            category=data["category"],
            content=data["content"],
            slug=data["slug"],
        )
