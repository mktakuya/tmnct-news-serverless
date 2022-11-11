import logging

DUMMY_CONTENT = """<p>　令和４年１０月１日（土）～１０月２９日（土）の期間中、苫小牧、札幌及び千歳に会場を設け、中学校３年生及び保護者等を対象に「令和５年度入学試験に関する説明会」を開催いたしました。<br />
　当日は全体で、苫小牧会場にはWeb参加を含めて219名，札幌会場には52名そして千歳会場には32名の方にご参加いただきました。<br />
説明会では、学校概要及び入学試験に関する説明を行い、苫小牧会場においては、校内施設を見学いただくキャンパスツアーも実施しました。<br />
　各会場とも参加者から多くの質問が寄せられ、本校及び入学試験の手続きに関する理解を深めていただく機会となりました。<br />
　多くの中学生・保護者等の方にご参加いただき、改めて教職員一同感謝申し上げます。</p>
<p><img loading="lazy" src="https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11011.jpg" alt="" width="300" height="200" class="alignleft size-full wp-image-19120" /><img loading="lazy" src="https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11012.jpg" alt="" width="300" height="200" class="alignright size-full wp-image-19121" /><br />
<img loading="lazy" src="https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11013.jpg" alt="" width="300" height="200" class="alignleft size-full wp-image-19122" /><img loading="lazy" src="https://www.tomakomai-ct.ac.jp/wp01/wp-content/uploads/2022/11/11014.jpg" alt="" width="300" height="200" class="alignright size-full wp-image-19123" /></p>
"""


def fetch_news_handler(event, context):
    logging.info('Started lambda function as fetchNews with event: %s', event)

    return {
        "updated": True,
        "news": {
            "title": "令和５年度入学試験に関する説明会を実施しました",
            "wp_pid": 19119,
            "url": "https://www.tomakomai-ct.ac.jp/news/19119.html",
            "pub_date": "2022-11-01 04:29:17",
            "category": "news",
            "content": DUMMY_CONTENT,
            "slug": "ab296fe875",
        }
    }


def tweet_news_handler(event, context):
    logging.info('Started lambda function as tweetNews with event: %s', event)

    news = event['news']

    return news


def save_news_handler(event, context):
    logging.info('Started lambda function as saveNews with event: %s', event)

    return {
        "status": "OK"
    }


