# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import os

URL = "https://covid19.who.int/table"
DRIVER_PATH = "C:/Users/91989/dspath/chromedriver"

options = webdriver.ChromeOptions() 
path = os.path.abspath(os.getcwd() + "\..\who_table_data")
prefs = {"download.default_directory": path}
options.add_experimental_option("prefs", prefs)

def download_data():
    #input_term = input("Enter a term to search:")
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    driver.get(URL)
    #time.sleep(10)
    
    #download_button = driver.find_element_by_class_name("sc-AxjAm sc-fzoyAV iiPwYT")
    download_button = driver.find_element_by_xpath("//a[@class='sc-AxjAm sc-fzoyAV iiPwYT']")
    download_button.click()