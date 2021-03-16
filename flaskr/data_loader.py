# -*- coding: utf-8 -*-
import os
import glob
import config
import pandas as pd


def load_news_data():
    news = pd.read_csv("../data/googlenews.csv",sep=config.CSV_DELIMITER)
    news["content"]=news["content"].apply(
            lambda x: x.replace(config.CUSTOM_NEW_LINE,"\n"))
    print("loaded news data")
    return news

def load_who_stats():
    path = os.path.abspath(os.getcwd()+"\..\data\who\*")
    list_of_files = glob.glob(path) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    df = pd.read_csv(latest_file)
    df.colums=["name","region","tot","totpm","new7","new7pm","new24","dtot",
               "dthpm","dth7","dth7pm","d24","class"]
    df.set_axis(["name","region","tot","totpm","new7","new7pm","new24","dtot",
                 "dthpm","dth7","dth7pm","d24","class"], axis=1, inplace=True)
    print("loaded who data")
    return df