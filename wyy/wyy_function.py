import json
import random
import re

import requests
# from fake_useragent import UserAgent
from lxml import etree
from fake_useragent import UserAgent


def get_total(id):
    """ 获取评论数量 """
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(id)
    # print(url)
    ua = UserAgent()
    header = {
        "Host": "music.163.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"

    }
    # while True:
    #     ip = getProxy()
    #     if verifyProxy(ip) == 200:
    #         proxies =  {'https': ip}
    #     # print(proxies)
    #         break
    res = requests.get(url, headers=header)
    print(res.text)
    json_res = json.loads(res.text)
    print(id,json_res)
    return (json_res['total'])


def get_intro(id):
    """歌手简介"""
    url = 'https://music.163.com/artist/desc?id={}'.format(id)
    ua = UserAgent()
    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent":ua.random,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer":"https://music.163.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    # while True:
    #     ip = getProxy()
    #     if verifyProxy(ip) == 200:
    #         proxies =  {'https': ip}
    #         # print(proxies)
    #         break
    res = requests.get(url, headers=header)
    tree = etree.HTML(res.text)
    description = tree.xpath('//div[3]/div[1]/div/div/div[2]/div/p[1]/text()')
    return description

# print(get_intro(1049023))


def get_homepage(id):
    """主页信息"""
    url = 'https://music.163.com/user/home?id={}'.format(id)
    headers = {
        "Connection":"keep-alive",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"https://music.163.com/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }
    proxies = [
        {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
        {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
        {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"},
        {'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
        {'http':"http://183.166.86.209:32342"}]
    res = requests.get(url,headers=headers,proxies=random.choice(proxies))
    global is_china
    tree = etree.HTML(res.text)
    head_img = tree.xpath('//*[@id="ava"]/img/@src')  # 歌手图片

    nickname = tree.xpath('//*[@id="j-name-wrap"]/span[1]/text()') # 歌手名字
    print(nickname)
    is_china = 3
    if is_Chinese(nickname[0]) == 1:
        is_china = 1
        print(is_china)

    tags = tree.xpath('//*[@id="head-box"]/dd/div[1]')  # 歌手标签
    tag = ''
    for item in tags[0][1:]:
        tag += ((item.xpath('./text()')[1].strip()))

    gender = tree.xpath('//*[@id="j-name-wrap"]/i/@class') # 歌手性别
    gender = (re.findall(r'\d+',gender[0]))

    dynamic_count = tree.xpath('//*[@id="event_count"]/text()') # 歌手动态数


    follower_count = tree.xpath('//*[@id="follow_count"]/text()') # 歌手关注数


    fans_count = tree.xpath('//*[@id="fan_count"]/text()') # 歌手粉丝数


    region = tree.xpath('//*[@id="head-box"]/dd/div[3]/span/text()') # 歌手所在区域
    if region == []:
        region = ''
    else:
        region = region[0][5::]

    introduce = tree.xpath('//*[@id="head-box"]/dd/div[2]/text()') # 歌手个人介绍
    introduce = introduce[0][5::]

    ul = tree.xpath('//*[@id="head-box"]/dd/div[4]/ul')
    if ul == []:
        other_contact = ''
    else:
        data_list = []
        for item in ul[0]:
            url = (item.xpath('./a/@href')[0])
            name = (item.xpath('./a/@title')[0])
            data = {
                name:url
            }
            data_list.append(data)
        other_contact = list_dict(data_list)  # 歌手社交网络

    return head_img,tag,gender,dynamic_count,follower_count,fans_count,region,nickname,introduce,other_contact,is_china




















def formatData(data):
    """处理sql字符串引号"""
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return  data.replace('"','\\\"')







def is_Chinese(word):
    """判断是否包含中文"""
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False



def isnull(data):
    """判断列表是否空值"""
    if data == [] or data == None:
        data = ''
    else:data = data[0]
    return data



def list_dict(list_data):
    """列表中的字典合并"""
    dict_data = {}
    for i in list_data:
        key, = i
        value, = i.values()
        dict_data[key] = value
    return dict_data

