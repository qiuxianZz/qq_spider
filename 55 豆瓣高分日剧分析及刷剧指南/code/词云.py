# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:07:23 2019

@author: Administrator
"""

import pymongo
import pandas as pd
import numpy as np
import wordcloud
import jieba
import warnings
warnings.filterwarnings('ignore') 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['bilibili']
#datatable = db['kimura']
datatable = db['gakki']
df = pd.DataFrame(list(datatable.find()))
df["弹幕内容"].to_csv("弹幕.txt", index=False)
stop_list = pd.read_csv("stop_words.csv",encoding='gbk', engine='python', names=["sw"])["sw"].tolist()

def txt_cut(f):
   return [w for w in jieba.cut(f) if w not in stop_list and len(w)>1]

f = open("弹幕.txt", encoding="utf-8").read()
txtcut = txt_cut(f)
words = pd.Series(txtcut)
TOP20 = words.value_counts().sort_values(ascending=False)[0:20]

w = wordcloud.WordCloud(background_color="white")
w.generate(" ".join(txtcut))
w.to_file("g.png")

w2 = wordcloud.WordCloud(background_color="white", min_font_size=10, max_font_size=100, font_step=2)
w2.generate(" ".join(TOP20.index.tolist()))
w2.to_file("g2.png")