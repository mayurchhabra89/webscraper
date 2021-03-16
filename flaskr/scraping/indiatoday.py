## -*- coding: utf-8 -*-
#import os
#from bs4 import BeautifulSoup
#from selenium import webdriver
#
#URL = "https://www.indiatoday.in/coronavirus-covid-19-outbreak"
#DRIVER_PATH = "C:/Users/91989/dspath/chromedriver"
#
#def cleanse_text(text):
#    paras = text.split("\n")
#    paras = [par for par in paras if not 
#            par.lower().startswith(("also read","advertisement"))]
#    return "\n".join(paras)
#    
#def scrap_data():
#    """ 
#    Scrap search results from google news along with website content 
#    """
#    driver = webdriver.Chrome(DRIVER_PATH)
#    driver.get(URL)
##    content_table = driver.find_element_by_class_name("view-content")
#    content_list = driver.find_elements_by_class_name("catagory-listing")
#    news = list()
#    
#    for content in content_list:
#        anchor = content.find_element_by_tag_name('a')
#        href = anchor.get_attribute("href")
#        head = anchor.text
#        sub_head = content.find_element_by_tag_name('p').text
#        news.append({"url":href, 
#                     "head":head, 
#                     "subhead":sub_head})
#    
#    for article in news:
#        driver.get(article["href"])  # go to linked page
#        content_tag = driver.find_element_by_xpath(
#                "//div[contains(@class,'description')]")
#        content = cleanse_text(content_tag.text)
#        article["content"]=content
#    
#    return news
#    
#    