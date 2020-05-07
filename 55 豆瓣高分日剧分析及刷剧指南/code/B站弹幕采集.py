# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:43:02 2019

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
import pymongo
import re
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")

def get_links(n):
    links = []
    for i in range(n):
        links.append("https://search.bilibili.com/all?keyword=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3&page=" + str(i+1))
    return links
#https://search.bilibili.com/all?keyword=%E6%9C%A8%E6%9D%91%E6%8B%93%E5%93%89&page=
#https://search.bilibili.com/all?keyword=%E5%A4%A9%E6%B5%B7%E4%BD%91%E5%B8%8C&page=

def get_urls(url, headers, cookies):
    lst = []
    print(url)
    data = requests.get(url=url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(data.text, "lxml")
    lis = soup.find("ul", class_="video-list clearfix").find_all("li")
    for l in lis:
        lst.append("https:" + l.a["href"])
    print(lst)
    return lst


def get_data(url, headers, cookies, table):
    r1 = requests.get(url, headers=headers, cookies=cookies)
    soup1 = BeautifulSoup(r1.text, "lxml")
    name = soup1.h1["title"]
    date = re.search(r"(20\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})",soup1.find('div',class_ = 'video-data').text).group(1)
    cid = re.search(r'"cid":(\d*)', r1.text).group(1)
    u2 = 'https://comment.bilibili.com/{}.xml'.format(cid)
    r2 = requests.get(u2, headers=headers, cookies=cookies)
    r2.encoding = r2.apparent_encoding
    comment_list = re.findall(r'">(.*?)</d>', r2.text)
    n = 0    
    for c in comment_list:
        dic = {}
        dic["视频标题"] = name
        dic["视频发布时间"] = date
        dic["弹幕内容"] = c
        table.insert_one(dic)
        n += 1
    return n 
    
num = 10
links = get_links(num)
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
cookies_str = "_uuid=1C1F803A-930C-50D6-73D4-4B719782A60916235infoc; buvid3=5F8D60FA-2AF9-4BD3-A0B8-4F0C0E010C12155826infoc; arrange=matrix; LIVE_BUVID=AUTO4115744157165591"
cookies = {}
cookies_str = cookies_str.split("; ")
for i in cookies_str:
    cookies[i.split("=")[0]] = i.split("=")[1]

start = time.time()
video_list = []
video_error = []
for link in links:
    try:
        video_list.extend(get_urls(link, headers=headers, cookies=cookies))
        #print("视频网址获取成功，共获取{}个视频网址".format(len(video_list)))
    except:
        video_error.append(link)
        #print("视频网址获取失败，失败网址为：", link)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["bilibili"]
datatable = db["gakki"]


comment_error = []
count = 0

for v in video_list:
    try:
        count += get_data(v, headers=headers, cookies=cookies, table=datatable)
        #print("弹幕内容获取成功，共获取{}条弹幕".format(count))
    except:
        comment_error.append(v)
        #print("弹幕内容获取失败，失败链接为：", v)
end = time.time()
print("\n")
print("采集完成！")
print("共采集{}个视频的{}条弹幕信息".format(len(video_list), count))
print("总共用时{:.2f}秒".format(end - start))

        
