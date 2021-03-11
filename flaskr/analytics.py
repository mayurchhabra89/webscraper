# -*- coding: utf-8 -*-

import pandas as pd
from rake_nltk import Rake
from textblob import TextBlob
import profanity_check


def get_data():
    df = pd.DataFrame([['The vaccine for covid-19 will be announced on 1st August.'],
                       ['Do you know how much expectation the world population is having from this research?'],
                       ['This risk of virus will end on 31st July.']])
    df.columns = ['text']
    
    # Polarity
    df['polarity'] = df['text'].apply(lambda x : 
        TextBlob(str(x)).sentiment.polarity)
    
    # Subjectivity
    df['subjectivity'] = df['text'].apply(lambda x : 
        TextBlob(str(x)).sentiment.subjectivity)
    
    # profanity
    df['profanity'] = df['text'].apply(lambda x : 
        round(profanity_check.predict_prob([str(x)])[0],2))
    
    # KeyPhrases
    def get_phrases(text):
        r = Rake()
        r.extract_keywords_from_text(str(text))
        return r.get_ranked_phrases_with_scores()
    
    
    df['keyphrases'] = df['text'].apply(get_phrases)
    
    return df