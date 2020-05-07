import time

import requests
import json

current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


# 数字专辑畅销榜


def get_album_comment(album_id):
    """
    数字专辑评论数
    :param album_id:专辑id
    :return: 评论总数
    """
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=2&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'.format(
        album_id)
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)
    commenttotal = data["comment"]["commenttotal"]
    return commenttotal



def get_album_details(album_id):
    """
    数字专辑详情信息 json里没有 流派 和语种 两个信息需要去html页面解析
    :param album_id:专辑id
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?cmd=get_album_buy_page&albumid={}&p=0.4434568940026893&g_tk_new_20200303=5381&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(album_id)
    res = requests.get(url,headers=headers)
    con = json.loads(res.text)
    data = con["data"]
    album_id = data["album_id"]
    album_mid = data["album_mid"]
    album_name = data["album_name"]
    buypage = data["buypage"]
    companyname = data["companyname"]
    desc = data["desc"]
    picurl = data["headpiclist"][0]["picurl"]
    publictime = data["publictime"]
    album_count = data["sale_info"]["album_count"]
    return (album_id,album_mid,album_name,buypage,companyname,desc,picurl,publictime,album_count)


def digital_album_day():
    """
    数字专辑日榜
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=day_sale_toplist&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584002531680'
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=5381&uin=     498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=day_sale_toplist&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584081749066'
    res = requests.get(url, headers=headers)
    return (res.text)


def digital_album_week(week):
    """
    数字专辑周榜
    :param week: 什么年份第几周 格式如：202012
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=5381&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=week_sale_toplist&week={}&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584081932774'.format(
        week)
    res = requests.get(url, headers=headers)
    return (res.text)


def digital_album_year(year):
    """
    数字专辑年榜
    :param year: 什么年份 格式如：2020
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=5381&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=year_sale_toplist&week=&year={}&weeklist=1&yearlist=1&sin=0&ein=19&_=1584082056201'.format(
        year)
    res = requests.get(url, headers=headers)
    return(res.text)


def digital_album_all():
    """
    数字专辑总榜
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=5381&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=sales_album&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584082181320'
    res = requests.get(url, headers=headers)
    return (res.text)


def parse_digital_album(data):
    """
    解析数字专辑信息
    :param data: data
    :return:
    """
    data = json.loads(data)
    list = data["data"]["list"]
    for item in list:
        album_id = item["album_id"]
        comment = get_album_comment(album_id)
        info = get_album_details(album_id)
        print(info,comment)


data = digital_album_week(202012)
parse_digital_album(data)
