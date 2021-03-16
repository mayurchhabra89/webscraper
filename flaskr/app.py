# -*- coding: utf-8 -*-
import data_loader
from analytics import Analytics
from scraper import refresh_data
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def render_data():
    refresh = request.args.get("refresh", "false")
    if refresh.lower() == "true":
        refresh_data()
    who_stats = data_loader.load_who_stats()
    news_records = data_loader.load_news_data()
    news_stats = Analytics().get_info(news_records)

    return render_template("index.html",
          count_data = who_stats[["name","tot","dtot"]].values,
          news_records = news_stats[["head","source","polarity",
                                    "subjectivity","profanity",
                                                "keyphrases"]].values)
if __name__ == '__main__':
   app.run()
