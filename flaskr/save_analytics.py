# -*- coding: utf-8 -*-
import data_loader
import csv
import pandas as pd
from analytics import Analytics

def write_stats():
    news_stats[["head","polarity","subjectivity","profanity",
            "factual_info"]].to_csv("../data/analytics.csv",sep="#")
    print("Stored Sentiment and profanity data into keywords.csv")

def write_keyphrases():
    file_header = ["head","phrase","score"] 
    data = [[head,phrase[1],phrase[0]] 
        for head,keyphrases in news_stats[["head","keyphrases"]].values
        for phrase in keyphrases]
    with open('../data/keyphrases.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(file_header)
        writer.writerows(data)  
    print("Stored Keyphrases data into keyphrases.csv")
        
def write_keywords():
    file_header = ["head","keyword","score"] 
    data = [[head,phrase[1],phrase[0]] 
        for head,keyphrases in news_stats[["head","keywords"]].values
        for phrase in keyphrases]
    with open('../data/keywords.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(file_header)
        writer.writerows(data)  
    print("Stored Keywords data into keywords.csv")
          
def write_labels_info():          
    labels_info_dict = {head:labels_info 
                        for head, labels_info in 
                        news_stats[["head","labels_info"]].values}
    df = pd.DataFrame.from_dict(labels_info_dict,orient="index")
    df.to_csv("../data/labels_info.csv",sep="#")
    print("Stored content type data into keywords.csv")

news_records = data_loader.load_news_data()
news_stats = Analytics().get_info(news_records)        
write_stats()
write_keyphrases()
write_keywords()
write_labels_info()
