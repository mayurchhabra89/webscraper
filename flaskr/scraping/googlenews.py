# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests

URL = "https://www.google.com/search?q=covid+19&lr=lang_en&cr=countryIN&tbs=lr:lang_1en,ctr:countryIN&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjyv7Wxu6jvAhW5qksFHe1gAskQ_AUoAXoECFAQAw&biw=1792&bih=1041"

def scrap_data():
    html = requests.get(google_query_covid19).text
    soup = BeautifulSoup(html, 'lxml')
    
    articles = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
    for a in articles:
        if a.text.startswith("Popular on Twitter"):
            continue
        print('ARTICLE:')
        print("*"*10)
        for headline in a.find_all("div", class_="BNeawe vvjwJb AP7Wnd"):
            print("HEADLINE:", headline.text, "\n")
            
        
        
        unwanted = a.find('span')
        unwanted.extract()
        unwanted = a.find('span')
        unwanted.extract()
        
        for content in a.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
            print("Content:", content.text, "\n")
            break
            

    
    for i in a.find_all("a", href=True):
        print(i['href'].split("=")[1], "\n")
        break
    
    print("-"*100)
        
        
        

