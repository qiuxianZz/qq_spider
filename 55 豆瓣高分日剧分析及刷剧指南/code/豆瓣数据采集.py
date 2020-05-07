# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:00:08 2019

@author: Administrator
"""

from selenium import webdriver
import time
import random
import warnings
warnings.filterwarnings('ignore') 
import pandas as pd


def get_urls(url, current_page, page_n):
    lst = []
    error_lst = []
    browser.get(url)
    
    main_window = browser.window_handles[0]
    if current_page != 1:
        for i in range(current_page-1):
            sleeptime = random.randint(1,5)
            time.sleep(sleeptime)
            browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[4]/a').click()
   
    while current_page <= page_n:
        for p in range(20*(current_page-1)+1, 20*current_page+1):
            xpath = '//*[@id="content"]/div/div[1]/div/div[4]/div/a[{}]'.format(p)
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
        browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[4]/a').click()
        current_page += 1
    return lst, error_lst



if __name__ == "__main__":
   
    u = "https://movie.douban.com/tv/#!type=tv&tag=%E6%97%A5%E5%89%A7&sort=rank&page_limit=20&page_start=0"
    browser = webdriver.Chrome()
       
    current_page = 5
    page_n = 24
    lst, error_lst = get_urls(u, current_page=current_page, page_n=page_n)
    df = pd.DataFrame(lst, columns=["urls"])
    df_error = pd.DataFrame(error_lst, columns=["error_urls"])
    df.to_csv("urls.csv", mode="a", header=False)
    df_error.to_csv("error_xpath.csv")
    
    
    