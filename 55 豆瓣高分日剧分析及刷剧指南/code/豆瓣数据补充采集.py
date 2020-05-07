# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:00:00 2019

@author: Administrator
"""

from selenium import webdriver
import time
import random
import warnings
warnings.filterwarnings('ignore') 
import pandas as pd

u = "https://movie.douban.com/tv/#!type=tv&tag=%E6%97%A5%E5%89%A7&sort=rank&page_limit=20&page_start=0"
browser = webdriver.Chrome()

lst = []
error_lst = []
browser.get(u)
main_window = browser.window_handles[0]
for i in range(16):
    sleeptime = random.randint(1,5)
    time.sleep(sleeptime)
    browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[4]/a').click()



xpaths = pd.read_csv("error_temp.csv", header=None)
for xpath in xpaths[0]:    
    try:
        browser.find_element_by_xpath(xpath).click()
        new_window = browser.window_handles[1]               
    except:
        error_lst.append(xpath)
        continue
    browser.switch_to_window(new_window)
    lst.append(browser.current_url)
    browser.close()
    browser.switch_to_window(main_window)
    sleeptime = random.randint(1,5)
    time.sleep(sleeptime)
    
df = pd.DataFrame(lst, columns=["urls"])
df_error = pd.DataFrame(error_lst, columns=["error_urls"])
df.to_csv("urls.csv", mode="a", header=False)
df_error.to_csv("error_update.csv")

