# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd

def read_who_data():
    pass
def read_news_data():
    pass

def read_who_stats():
    path = os.path.abspath(os.getcwd()+"\..\data\who\*")
    list_of_files = glob.glob(path) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    df = pd.read_csv(latest_file)
    df.head()
    df.colums=["name","region","tot","totpm","new7","new7pm","new24","dtot",
               "dthpm","dth7","dth7pm","d24","class"]
    df.shape
    df.set_axis(["name","region","tot","totpm","new7","new7pm","new24","dtot",
                 "dthpm","dth7","dth7pm","d24","class"], axis=1, inplace=True)
    return df
#df[["name","tot","dtot"]]