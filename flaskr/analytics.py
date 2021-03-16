# -*- coding: utf-8 -*-
import pandas as pd
from rake_nltk import Rake
from textblob import TextBlob
import profanity_check
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import sent_tokenize
import re

class Analytics(object):
    
    def __init__(self):
        pass
    
    def merge_numbers_intext(self, text):
        '''
        merge adjacent numbers occureence into the text which might got 
        splited coz of punctuations presence eg. 1,200,345 -> 1 200 345 
        '''
        word_list = text.split()
        new_word_list = []
        number = ""
        for word in word_list:
            if word.isnumeric():
                number+=word
            else:
                if len(number):
                    new_word_list.append(number)
                    number=""
                new_word_list.append(word)
        return " ".join(new_word_list)
    
    
    #def get_factual_info_0(text):
    #    labels=["numbers","data","death","recovery","count","discharged","cases","rising","droping"]
    #    words = stopwords.words("english")+["covid","corona","covid19","19"]
    #    stemmer = PorterStemmer()
    #    cleaning_lambda  = lambda x: " ".join([stemmer.stem(i) 
    #        for i in re.sub("[^a-zA-Z0-9]", " ", x.lower()).split()
    #        if i not in words])
    #    cleaned_text = cleaning_lambda(text)
    #    cleaned_text = merge_numbers_intext(cleaned_text)
    #    cleaned_labels = [cleaning_lambda(label) for label in labels]
    #    numb_exists = re.findall("\d+",cleaned_text)  # count all the numbers fro the text
    #    labels_exists = re.findall(r"({})".format("|".join(cleaned_labels)),cleaned_text)  # getting lables count which might indicate factual information
    #    numb_cnt = len(numb_exists)
    #    labels_cnt = len(labels_exists)
    #    word_cnt = len(cleaned_text.split())
    #    return (numb_cnt+labels_cnt)/word_cnt if word_cnt else 0
    
    def get_factual_info(self, text):
        labels=["numbers","data","death","recovery","count","discharged","cases","rising","droping"]
        words = stopwords.words("english")+["covid","corona","covid19","19"]
        sents = sent_tokenize(text)
        stemmer = PorterStemmer()
        cleaning_lambda  = lambda x: " ".join([stemmer.stem(i)
            for i in re.sub("[^a-zA-Z0-9]", " ", x.lower()).split()
            if i not in words])
        
        cleaned_labels = [stemmer.stem(label.lower()) for label in labels]
        factual_info = 0
        for sent in sents:
            cleaned_text = cleaning_lambda(sent)
            cleaned_text = self.merge_numbers_intext(cleaned_text)
            numb_exists = re.findall("\d+",cleaned_text)  # count all the numbers fro the text
            labels_exists = re.findall(r"({})".format("|".join(cleaned_labels)),cleaned_text)  # getting lables count which might indicate factual information
            if numb_exists or labels_exists:
                factual_info+=1
        return (factual_info/len(sents))
    
    # KeyWords
    def get_keywords(self, text):
        r = Rake(max_length = 1)
        r.extract_keywords_from_text(text)
        return r.get_ranked_phrases_with_scores()[:20]
    
    # KeyPhrases
    def get_keyphrases(self, text):
        r = Rake(min_length = 2, max_length = 10)
        r.extract_keywords_from_text(text)
        return r.get_ranked_phrases_with_scores()[:5]
        
    # Labeles
    def get_labels(self, text):
            labels_list = {
            "Vaccine":["vaccine"],
            "Lockdown":["lockdown"],
            "Safety measures": ["precaution", "social distancing", "washing hands", "safety measures", "ppe", "mask","quarantine"], 
            "Travel":["flight", "travel", "train", "transport", "visa","departure","arrival"],
            "Testing":["rt-pcr", "pcr", "antigen", "antibody test", "serology test", "diagnostic","rtpcr"],
            "Official announcements/Rules and regulations":["official", "rules", "regulation", "announced", "announcement", "government"]}
        
            stemmer = PorterStemmer()
            words = stopwords.words("english")
            cleaning_lambda  = lambda x: " ".join([stemmer.stem(i) 
                for i in re.sub("[^a-zA-Z]", " ", x.lower()).split() 
                if i not in words])
            cleaned_text = cleaning_lambda(text)
            cleaned_labels = {key:[cleaning_lambda(word) for word in values] 
                for key, values in labels_list.items()}       
            labels_count = {key:
                sum([cleaned_text.count(value) for value in values]) 
                for key, values in cleaned_labels.items()}
            
            return labels_count
    
    def get_info(self, df):
        new_df = df.copy()
        
        # Polarity
        new_df['polarity'] = new_df['content'].apply(lambda x : 
            TextBlob(str(x).lower().replace("positive","infected")).sentiment.polarity)
        print("Collected Polarity Information")
        
        # Subjectivity
        new_df['subjectivity'] = new_df['content'].apply(lambda x : 
            TextBlob(str(x).lower().replace("positive","infected")).sentiment.subjectivity)
        print("Collected Subjectivity information")
        
        # profanity
        new_df['profanity'] = new_df['content'].apply(lambda x : 
            round(profanity_check.predict_prob([str(x)])[0],2))
        print("Collected Profanity information")

        
        # KeyPhrases
        new_df['keywords'] = new_df['content'].apply(self.get_keywords)
        print("Collected Keywords")
        
        # KeyPhrases
        new_df['keyphrases'] = new_df['content'].apply(self.get_keyphrases)
        print("Colected KeyPhrases")
        
        # Factual Info
        new_df["factual_info"] = new_df['content'].apply(self.get_factual_info)
        print("Collected Numberic Info")
        
        # Labels information
        new_df["labels_info"] = new_df['content'].apply(self.get_labels)
        print("Collected content info")
        
        return new_df



