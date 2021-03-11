# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
url = "https://edition.cnn.com/world/live-news/coronavirus-pandemic-vaccine-updates-03-09-21/index.html"
import requests

articles = soup.find_all("div", id="posts-and-button")
for a in articles:
#     print('HEADLINE******:', a.content)
#     print("\n")
    for h in a.find_all("article", class_="sc-bwzfXH sc-kIPQKe jjVnED"):
#         print("ARTICLE: ", h.text)
#         print("\n")
        for d in h.find_all("div", class_="sc-bdVaJa post-content-rendered render-stellar-contentstyles__Content-sc-9v7nwy-0 erzhuK"):
#             print("DIV:", d.text)
#             print("\n")
            for p in d.find_all("p", class_="sc-gZMcBi render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 dCwndB"):
                print('PARAGRAPH: ', p.text)
                print("\n")
#         print(h.h2.text)
#     print(a.header.h2.text)
#     print(a.div.p.text)