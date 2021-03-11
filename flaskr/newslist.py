## -*- coding: utf-8 -*-
#import requests
#from bs4 import BeautifulSoup
#
##input_term = input("Enter a term to search:")
#url = "https://news.google.com/search?q={}"
#url = url.format("corona virus")
#source = requests.get(url).text
#source
#soup = BeautifulSoup(source, 'html.parser')
## here divires contains an ol which contains the results.
#news_divs = results = soup.find("div", {"class": "xrnccd"})
#news_titles = []
#for div in news_divs:
##    print(div)
#    title = div.find("h3").find("a").text
#    print(title)
#    news_titles.append(title)
#    break
## Loop over each item to obtain the title and link (anchor tag text and link)
##print(heading_results)
#from flask import Flask, render_template
#app = Flask(__name__)
#
#@app.route('/')
#def send_news(news_titles):
#   return render_template('newslist.html', news = news_titles)
#
#if __name__ == '__main__':
#   app.run()
