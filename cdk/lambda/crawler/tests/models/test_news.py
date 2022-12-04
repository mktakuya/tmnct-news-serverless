import unittest
from copy import copy

from crawler.models import News

CONTENT = """
<p>
    令和４年１１月８日（火）、９日（水）に３年ぶりとなる第４学年総合研修旅行を実施しました。
    学生たちは、旅行の目的である国内外の産業構造の変化や現代の科学・技術の多様な進展について理解するとともに、
    文化財等を訪ねることで幅広い視野・教養を養うことができました。
</p>
<p>
    <img src=\"https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11251.jpg\" width=\"300\" />
    <img src=\"https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11252.jpg\" width=\"300\" />
</p>
"""
news = News(
    title="サンプルニュース",
    wp_pid=19191,
    url="https://www.tomakomai-ct.ac.jp/news/19191.html",
    pub_date="Fri, 25 Nov 2022 00:02:46 +0000",
    category="news",
    content=CONTENT,
    slug="d72d469eb3"
)


class TestNews(unittest.TestCase):
    def test_short_url(self):
        assert news.short_url() == "https://tmnct-news.m6a.jp/n/d72d469eb3"

    def test_image_urls_with_news_has_images(self):
        expected = [
            "https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11251.jpg",
            "https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11252.jpg"
        ]
        actual = news.image_urls()
        assert actual == expected

    def test_image_urls_with_news_does_not_have_any_images(self):
        non_image_news = copy(news)
        non_image_news.content = "画像が含まれていないニュース"

        expected = []
        actual = non_image_news.image_urls()
        assert actual == expected
