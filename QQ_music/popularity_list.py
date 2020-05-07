import json

import requests

from QQ_music.qq_music_info import getdetails

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

def getpopularity_day():
    """
    人气日榜
    :return:
    """
    url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=1&daystr=0&_=1584001744456'
    res = requests.get(url,headers=headers)
    print(res.text)


# getpopularity_day()

def getpopularity_week(year,num):
    """
    人气周榜
    :param year: 年份
    :param num: 第几周
    :return:
    """
    url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=2&weeklist=1&year={}&week={}&_=1584001693045'.format(year,num)
    res = requests.get(url,headers=headers)
    return res.text
# getpopularity_week(2020,10)

def getpopularity_year(year):
    """
    人气年榜
    :param year: 年份
    :return:
    """
    url= 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=3&year={}&_=1584001817866'.format(year)
    res = requests.get(url,headers=headers)
    return res.text
# getpopularity_year(2019)


def parse_popularity(data):
    """
    解析出榜单歌曲id mid
    :param data:
    :return:
    """
    data = json.loads(data)
    ranklist = data["data"]["ranklist"]
    for item in ranklist:
        songinfo = item["songinfo"]
        songmid = songinfo["songmid"]
        songid = songinfo["songid"]
        getdetails(songmid,songid)

def getpopularity_all(year,week):
    """
    人气总榜
    :param year: 年份
    :param week: 周数
    :return:
    """
    url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=0&weeklist=0&year={}&week={}&daystr=0&_=1584002135364'.format(year,week)
    res = requests.get(url,headers=headers)
    return res.text
data = getpopularity_all(2017,1)
parse_popularity(data)
