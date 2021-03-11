# -*- coding: utf-8 -*-
import reader
import analytics
from scraper import refresh_data
from flask import Flask, render_template,request 

app = Flask(__name__)
    
@app.route('/')
def render_data():
   refresh = request.args.get("refresh", "false")
   if refresh.lower() == "true":
       refresh_data()
   who_stats = reader.read_who_stat()
   return render_template("index.html", 
                          count_data = who_stats[["name","tot","dtot"]].values,
                          news_records=analytics.get_data().values)
if __name__ == '__main__':
#   who_scrap.scrap_data()
   app.run()

