# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:31:46 2019

@author: Administrator
"""

import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
from bokeh.io import output_file
from bokeh.plotting import figure,show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import brewer
from bokeh.models.annotations import Label
import bokeh.palettes as bp
import warnings
warnings.filterwarnings('ignore') 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['豆瓣']
datatable = db['高分日剧']
df = pd.DataFrame(list(datatable.find()))

del df["_id"]
df["year"] = df["year"].astype(int)
df["grade"] = df["grade"].astype(float)

df_genre = df["genre"].str.split("/",expand=True)
df_genre.columns = ["genre"+str(i) for i in range(len(df_genre.columns))]
df_actor = df["actors"].str.split("/",expand=True)
df_actor.columns = ["actor"+str(i) for i in range(len(df_actor.columns))]
df = df.join(df_genre)
df = df.join(df_actor)
del df["genre"]
del df["actors"]
#初步清洗整理数据

genre_analysis = pd.DataFrame([])
for g in df_genre.columns:
    temp = df[["grade", g]]
    temp2 = temp.groupby(g).agg(["sum", "count"])
    genre_analysis = pd.concat([genre_analysis, temp2])
genre_analysis = genre_analysis.groupby(genre_analysis.index).sum()
genre_analysis.columns = ["sum", "count"]
genre_analysis["average"] = genre_analysis["sum"] / genre_analysis["count"]
genre_analysis["proportion"] = genre_analysis["sum"] / genre_analysis["sum"].sum()
genre_analysis.sort_values(by="proportion", inplace=True, ascending=False)
#分析类型
bokeh_pie = genre_analysis.iloc[:8][["proportion"]]
bokeh_pie.loc["其他"] = 1 - bokeh_pie["proportion"].sum()
color = brewer["YlGn"][9]
plt.axis("equal")
plt.pie(bokeh_pie["proportion"], labels=bokeh_pie.index, autopct="%.2f%%",
       pctdistance=0.8, labeldistance=1.1, startangle=90, radius=1.5,
       counterclock=False, colors=brewer["Set3"][9])
plt.savefig("genere_pie.png", dpi=300)
#绘制各类型占比饼图

genre_grade = pd.merge(df[["grade"]], df_genre, left_index=True, right_index=True)
box_dic = {}
for i in ['剧情', '喜剧', '爱情', '悬疑', '犯罪', '动作', '科幻', '家庭']:
    box_dic[i] = pd.Series([])
for i in ['剧情', '喜剧', '爱情', '悬疑', '犯罪', '动作', '科幻', '家庭']:
    for j in ['genre0', 'genre1', 'genre2', 'genre3', 'genre4', 'genre5',
       'genre6']:
        box_dic[i] = pd.concat([box_dic[i], genre_grade[genre_grade[j] == i]["grade"]]) 
color2 = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
bokeh_box = pd.DataFrame(box_dic)
box_fig = bokeh_box.plot.box(vert=False, grid = True, positions=[8,7,6,5,4,3,2,1], color = color2, figsize=(8, 12))
box_fig.get_figure().savefig("genre_box.png", dpi=300)
#绘制箱型图

df_year = df[["year", "title", "grade"]]
df_year = df_year.groupby("year").agg(["count", "mean"])
df_year = df_year[df_year.index >=1990]
df_year.columns = ["count", "mean"]
df_year["size"] = df_year["count"] * 1.5
year = df_year.index.astype(str).tolist()
output_file("year_bubble.html")
source = ColumnDataSource(df_year)
hover = HoverTool(tooltips=[("数量", "@count"),
                            ("平均分", "@mean")])
p = figure(plot_width=900, plot_height=350,
           title="不同年份日剧数量及平均分",
           tools = [hover,"box_select, reset, wheel_zoom,pan,crosshair"])
p.circle(x="year", y="mean", size="size", source=source,line_color="black", line_dash=[6,4], fill_color="blue", fill_alpha=0.6)
show(p)        
#不同年份日剧数量及平均分气泡图    

df_total_rank = df[df["year"] >=1990][["grade","title"]]
df_total_rank.sort_values(by="grade", ascending=False, inplace=True)
df_total_rank = df_total_rank.iloc[:10]  
df_total_rank.sort_values(by="grade", inplace=True)
title_c = ["白色巨塔", "假面骑士空我", "绅士刑警2", "假面骑士555", "东京爱情故事", "孤独的美食家第八季", "奈克瑟斯奥特曼", "胜者即是正义", "非自然死亡", "冷暖人间"]
title_c.reverse()
grade = df_total_rank["grade"].tolist()
fig,ax=plt.subplots(figsize=(3, 9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
b=ax.barh(range(len(title_c)),grade,color='#8dd3c7',hatch='X')
for rect in b:
    w=rect.get_width() 
    ax.text(w,rect.get_y()+rect.get_height()/2,'%.1f'%w,ha='left',va='center',fontsize=15, color='gray')
ax.set_yticks(range(len(title_c)))
ax.set_yticklabels(title_c)
ax.set_xlim([8,10])
ax.set_xticks([])
fig.savefig("total_rank.jpeg", dpi=300, bbox_inches = 'tight')
#1990年之后的日剧总排行


actor_analysis = pd.DataFrame([])
for a in df_actor.columns:
    temp = df[["grade", a]]
    temp2 = temp.groupby(a).agg(["sum", "count"])
    actor_analysis = pd.concat([actor_analysis, temp2])
actor_analysis = actor_analysis.groupby(actor_analysis.index).sum()
actor_analysis.columns = ["sum", "count"]
actor_analysis["average"] = actor_analysis["sum"] / actor_analysis["count"]

actor_count = actor_analysis.sort_values(by="count", ascending=False)
actor_count[["count"]].to_csv("actor_count.csv")


actor_rank = actor_analysis[actor_analysis["count"] >= 5]
actor_rank.sort_values(by="average", inplace=True, ascending=False)
actor_rank = actor_rank.iloc[:33]
actor_rank["gender"] = ['f','f','m','m','m','m','f','f','m','m','m','f','m','f','m','f','m','m','m','m','f','f','m','m','m','m','m','m','m','m','m','m','f']
actors = actor_rank[actor_rank["gender"] == "m"]
actors = actors.iloc[:10]
actresses= actor_rank[actor_rank["gender"] == "f"]


actors.index.name = "name"
actors_s = ColumnDataSource(actors)
output_file("actorsTOP10.html")
actors_fig = figure(plot_width=800, plot_height=250, title="男演员豆瓣高分TOP10", x_range=actors.index.tolist(),
           tools=['box_select,reset,xwheel_zoom,pan,crosshair'])
actors_fig.vbar(x="name", top="average", source=actors_s, width=0.7, alpha=0.5, color="#c6dbef")
for i in range(10):
    label = Label(x=i, y=7,       
                  x_offset=26,    
                  text=str(actors["average"].tolist()[i])[:3],      
                  text_font_size="15pt",    
                  text_color = "#084594")
    actors_fig.add_layout(label)
show(actors_fig)

actresses.index.name = "name"
actresses_s = ColumnDataSource(actresses)
output_file("actressesTOP10.html")
actresses_fig = figure(plot_width=800, plot_height=250, title="女演员豆瓣高分TOP10", x_range=actresses.index.tolist(),
           tools=['box_select,reset,xwheel_zoom,pan,crosshair'])
actresses_fig.vbar(x="name", top="average", source=actresses_s, width=0.7, alpha=0.5, color="#9c9ede")
for i in range(10):
    label = Label(x=i, y=7,       
                  x_offset=26,    
                  text=str(actors["average"].tolist()[i])[:3],      
                  text_font_size="15pt",    
                  text_color = "#393b79")
    actresses_fig.add_layout(label)
show(actresses_fig)


gephi_data = pd.DataFrame([],columns=["name","actor1","actor2"])
col_names = ["actor"+str(i) for i in range(89)]
for ac1 in col_names[0:]:
    for ac2 in col_names[1:]:
        data = df_actor[["title", ac1, ac2]].dropna()
        data.columns = ["name","actor1","actor2"]
        gephi_data = pd.concat([gephi_data, data])
gephi_data = gephi_data[gephi_data["actor1"] != gephi_data["actor2"]]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['豆瓣']
datatable = db['演员合作']
data_lst = gephi_data.to_dict(orient="records")
datatable.insert_many(data_lst)

weight_cal = gephi_data.groupby(["actor1", "actor2"]).count().reset_index()
weight_cal.sort_values(by="name", ascending=False, inplace=True)
weight_cal = weight_cal[weight_cal["name"] > 1]
weight_cal.to_csv("gephi_weight.csv")






