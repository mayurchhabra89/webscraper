# -*- coding: utf-8 -*-
import os
import glob
import time
from bs4 import BeautifulSoup
from selenium import webdriver

WHO_URL="https://covid19.who.int/table"
CHROME_DRIVER_PATH="C://Users/91989/dspath/chromedriver"

# Configuring Download folder for chorme web driver
options = webdriver.ChromeOptions() 
path = os.path.abspath(os.getcwd() + "\..\..\data\who")
prefs = {"download.default_directory": path}
options.add_experimental_option("prefs", prefs)

def download_data():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
    driver.get(WHO_URL)
    download_button = driver.find_element_by_xpath("//a[@class='sc-AxjAm sc-fzoyAV iiPwYT']")
    download_button.click()
    time.sleep(2)
    print("WHO datafile downloaded");

def manage_downloaded_files():
    path = os.path.abspath(os.getcwd()+"\..\..\data\who")
    list_of_files = glob.glob(path+"\*") # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.remove(latest_file)
    for file in list_of_files:
        os.remove(file)
    os.rename(latest_file,path+"\\"+"who.csv")
    print("Renamed recently WHO datafile to who.csv")
