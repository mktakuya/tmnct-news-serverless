import unittest

from crawler.models import News


class TestNews(unittest.TestCase):
    def test_short_url(self):
        news = News(
            title="サンプルニュース",
            wp_pid=19191,
            url="https://www.tomakomai-ct.ac.jp/news/19191.html",
            pub_date="Fri, 25 Nov 2022 00:02:46 +0000",
            category="news",
            content="サンプルニュースの内容",
            slug="d72d469eb3"
        )

        assert news.short_url() == "https://example.com/n/d72d469eb3"
