# -*- coding: utf-8 -*-
import config
import pandas as pd
from scraping import googlenews, indiatoday, cnn, who

def refresh_data():
    who.download_data() # Download data.csv file from who website
    googlenews_df = pd.DataFrame(googlenews.scrap_data())
    googlenews_df.to_csv("../data/googlenews.csv", 
                         date_format=config.DATE_FORMAT, sep=config.CSV_DELIMITER)
    print("Data refreshed Successful.")
