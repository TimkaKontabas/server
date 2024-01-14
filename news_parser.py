from collections import namedtuple
from functools import lru_cache
import requests
import bs4
from random import sample
import datetime


News = namedtuple('News', 'title text link')


site = "https://www.pochta.ru"
url = "https://www.pochta.ru/news"
class_ = "GridBox-sc-a3sce5-0 bIiyaZ"

@lru_cache(maxsize=10)
def parse_news(date:str, hour:int, ten_min:int):
    response = requests.get(url)
    bs = bs4.BeautifulSoup(response.text, "html.parser")
    news_container = bs.find("div", class_=class_)
    news_tags = news_container.find_all("div", class_="Newsstyled__PostItem-sc-1gokvzo-0")

    NEWS = []

    for news_tag in news_tags:
        title = news_tag.find("h2").text
        link = site + news_tag.find("a").get("href")
        text = news_tag.find("div", class_="Paragraph-sc-10hckd4-0 guIMBs").text
        NEWS.append(News(
            title=title,
            text=text,
            link=link
        ))
    return NEWS

def get_news(count_news=None):
    try:
        now = datetime.datetime.now()
        NEWS = parse_news(date=now.strftime("%d.%m.%Y"), hour=now.hour, ten_min=now.minute // 10)
        if count_news is None:
            count_news = len(NEWS) 
        return sample(NEWS, count_news)
    except:
        return []