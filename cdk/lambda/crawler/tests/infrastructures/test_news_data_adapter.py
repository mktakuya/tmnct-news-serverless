from datetime import datetime
import unittest

from crawler.models import News
from crawler.infrastructures.adapters import NewsDataAdapter


def data():
    return {
        "title": "サンプルニュース", "wp_pid": 19191, "url": "https://www.tomakomai-ct.ac.jp/news/19191.html",
        "pub_date": "Fri, 25 Nov 2022 00:02:46 +0000",
        "category": "news",
        "content": "サンプルニュースの内容",
        "slug": "d72d469eb3"
    }


class TestNewsDataAdapter(unittest.TestCase):
    def test_transform(self):
        adapter = NewsDataAdapter()
        result = adapter.transform(data=data())

        assert isinstance(result, News)

        assert result.title == "サンプルニュース"
        assert result.wp_pid == 19191
        assert result.url == "https://www.tomakomai-ct.ac.jp/news/19191.html"
        assert result.pub_date == datetime(2022, 11, 25).date()
        assert result.category == "news"
        assert result.content == "サンプルニュースの内容"
        assert result.slug == "d72d469eb3"
