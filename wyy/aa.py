import json
import random

import requests
from lxml import etree


def get_intro(id):
    """歌手简介"""
    url = 'https://music.163.com/artist/desc?id={}'.format(id)
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://music.163.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    proxies_list = json.loads(res.text)
    # proxies = (proxies_list['RESULT'])
    proxies = {'ip': '27.152.90.13', 'port': '29228'}
    print(proxies)
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=proxies)
    tree = etree.HTML(res.text)
    description = tree.xpath('//div[3]/div[1]/div/div/div[2]/div/p[1]/text()')
    return description

print(get_intro(1878))