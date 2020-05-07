# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:15:12 2019

@author: Administrator
"""

import pymongo
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
import warnings
warnings.filterwarnings('ignore') 

def get_data(url, headers, cookies, table):
    r = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, "lxml")
    dic = {}
    dic["title"] = soup.h1.find("span",property="v:itemreviewed").text
    dic["year"] = soup.h1.find("span",class_="year").text.replace("(","").replace(")","")
    dic["grade"] = soup.find("strong", class_="ll rating_num").text
    
    if  soup.find("span", class_="actor").find_all("a"):
        dic["actors"] = soup.find("span", class_="actor").find_all("a")[0].text
        if len(soup.find("span", class_="actor").find_all("a")) > 1:
            for actor in soup.find("span", class_="actor").find_all("a")[1:]:
                dic["actors"] += "/" + actor.text
    
    if soup.find_all("span", property="v:genre"):      
        dic["genre"] = soup.find_all("span", property="v:genre")[0].text
        if len(soup.find_all("span", property="v:genre")) > 1:
            for g in soup.find_all("span", property="v:genre")[1:]:
                dic["genre"] += "/" + g.text
                
    if soup.find_all("span", class_="short"):
        dic["comment"] = soup.find_all("span", class_="short")[0].text
        if len(soup.find_all("span", class_="short")) > 1:
            for c in soup.find_all("span", class_="short")[1:]:
                dic["comment"] += "/" + c.text
    table.insert_one(dic)
    



if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    cookies_str = 'bid=waBzrcPm3WI; douban-fav-remind=1; __gads=ID=9ff765aeef719291:T=1571033320:S=ALNI_MYgrTo53o5WzczzQDsAzE4ktW3X1w; __utmz=30149280.1571033333.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ll="118173"; __utma=30149280.2057584399.1571033333.1571033333.1574139989.2; __utmc=30149280'
    cookies = {}
    cookies_str = cookies_str.split("; ")
    for i in cookies_str:
        cookies[i.split("=")[0]] = i.split("=")[1]
    
    urls = pd.read_csv("urls.csv", index_col=0)
    urls.reset_index(drop=True, inplace=True)    
        
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient['豆瓣']
    datatable = db['高分日剧']
    

    count = 0
    error_list = []
    for u in urls["urls"]:
        try:
            get_data(u, headers=headers, cookies=cookies, table=datatable)
            count += 1
            print("成功获取{}部日剧信息".format(count))
            #sleeptime = random.randint(1,3)
            #time.sleep(sleeptime)
        except:
            error_list.append(u)
            print("获取信息失败，失败链接为: ", u)
            
"""
error_list = ['https://movie.douban.com/subject/26381232/?tag=%E6%97%A5%E5%89%A7&from=gaia_video',
 'https://movie.douban.com/subject/2136731/?tag=%E6%97%A5%E5%89%A7&from=gaia']
"""