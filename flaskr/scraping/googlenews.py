# -*- coding: utf-8 -*-
import requests
import config
from bs4 import BeautifulSoup
from newspaper import Article
from tld import get_tld

QUERY = "covid-19"
#URL for Google News Tab
QUERY_URL ="https://www.google.com/search?q={}&lr=lang_en&cr=countryIN&tbs=lr:lang_1en,ctr:countryIN&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjyv7Wxu6jvAhW5qksFHe1gAskQ_AUoAXoECFAQAw&biw=1792&bih=1041"

def scrap_data():
    search_url = QUERY_URL.format(QUERY)
    html = requests.get(search_url).text
    soup = BeautifulSoup(html, 'lxml')
    
    news = list()
    articles = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
    for a in articles:
        if a.text.startswith("Popular on Twitter"):
            continue
        head = a.find("div", class_="BNeawe vvjwJb AP7Wnd")
        subhead = a.find("div", class_="BNeawe s3v9rd AP7Wnd")
        
        url = a.find("a", href=True)
        url = url['href'].lstrip("/url?q=")
        url = url.split("&")[0]
        
        article = Article(url)
        article.download()
        article.parse()
        news.append({"head" : head.text,
                             "subhead" : subhead.text,
                             "url" : url,
                             "source":get_tld(url, as_object=True).fld,
                             "publish_date": article.publish_date,
                             "content" : article.text.replace("\n",config.CUSTOM_NEW_LINE)})
    print("Google News results scrapped successfully")
    return news