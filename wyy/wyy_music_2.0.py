import json
import queue
import random
import threading

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from wyy.save_wyy import save_result_user, save_result_song, save_result_album, formatData, save_result_user_to

from wyy.wyy_function import is_Chinese, list_dict


is_china = 0


def get_total(id):
    """ 获取评论数量 """
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(id)
    # print(url)
    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.baidu.com/link?url=kl7W_qmAYRwjM_DK6s0yN5kMZ_f8OWS-7CeGK36oYly&wd=&eqid=be9ba1b30001d70d000000065db2a1e4",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    proxies_list = json.loads(res.text)
    proxies = (proxies_list['RESULT'])
# print(random.choice(proxies))

    res = requests.get(url, headers=header, proxies=random.choice(proxies))

    # print(res.text)
    json_res = json.loads(res.text)
    return (json_res['total'])


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
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    tree = etree.HTML(res.text)
    description = tree.xpath('//div[3]/div[1]/div/div/div[2]/div/p[1]/text()')
    return description


def get_homepage(id):
    """主页信息"""
    url = 'https://music.163.com/user/home?id={}'.format(id)
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
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    tree = etree.HTML(res.text)
    global is_china
    tree = etree.HTML(res.text)
    head_img = tree.xpath('//*[@id="ava"]/img/@src')  # 歌手图片

    nickname = tree.xpath('//*[@id="j-name-wrap"]/span[1]/text()')  # 歌手名字

    if is_Chinese(nickname[0]) == 1:
        is_china = 1
        # print(is_china)
    else:
        is_china = 3
        # print(is_china)

    tags = tree.xpath('//*[@id="head-box"]/dd/div[1]')  # 歌手标签
    tag = ''
    for item in tags[0][1:]:
        tag += ((item.xpath('./text()')[1].strip()))

    gender = tree.xpath('//*[@id="j-name-wrap"]/i/@class')  # 歌手性别
    gender = (re.findall(r'\d+', gender[0]))

    dynamic_count = tree.xpath('//*[@id="event_count"]/text()')  # 歌手动态数

    follower_count = tree.xpath('//*[@id="follow_count"]/text()')  # 歌手关注数

    fans_count = tree.xpath('//*[@id="fan_count"]/text()')  # 歌手粉丝数

    region = tree.xpath('//*[@id="head-box"]/dd/div[3]/span/text()')  # 歌手所在区域
    if region == []:
        region = ''
    else:
        region = region[0][5::]

    introduce = tree.xpath('//*[@id="head-box"]/dd/div[2]/text()')  # 歌手个人介绍
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
                name: url
            }
            data_list.append(data)
        other_contact = list_dict(data_list)  # 歌手社交网络

    return head_img, tag, gender, dynamic_count, follower_count, fans_count, region, nickname, introduce, other_contact, is_china


def get_song(id, s_id):
    """歌曲and专辑信息"""

    url = 'https://music.163.com/album?id={}'.format(id)
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
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    tree = etree.HTML(res.text)

    album_id = id  # 专辑id
    tree = etree.HTML(res.text)
    artist_id = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/@href')  # 歌手id
    artist_id = re.findall('\d+', artist_id[0])

    album_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()')  # 专辑名

    head_img = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/img/@src')  # 专辑url

    singer = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/text()')  # 专辑所属歌手

    publish_time = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]/text()')  # 专辑发行时间

    publish_company = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]/text()')  # 发行公司
    if publish_company == []:
        publish_company = ''
    else:
        publish_company = publish_company[0].strip()

    share_count = tree.xpath('//*[@id="content-operation"]/a[4]/i/text()')  # 专辑转发数
    # print(share_count)
    share_count_ = tree.xpath('//*[@id="content-operation"]/a[3]/i/text()')
    # print(share_count_)

    if is_Chinese(share_count) == 1:
        share_count = 0

    elif share_count == ['下载']:
        share_count = re.findall('\d+', share_count_[0])
        share_count = share_count[0]
    else:
        share_count = re.findall('\d+', share_count[0])
        share_count = share_count[0]

    comment_count = tree.xpath('//*[@id="cnt_comment_count"]/text()')  # 专辑评论数
    if comment_count == ['评论']:
        comment_count = 0
    else:
        comment_count = comment_count[0]
    desc = tree.xpath('//*[@id="album-desc-more"]/p/text()')  # 专辑说明
    # print(desc)
    data = {
        'album_id': album_id,
        'artist_id': artist_id[0],
        'album_name': album_name[0],
        'head_img': head_img[0],
        'singer': singer[0],
        'publish_time': publish_time[0],
        'publish_company': publish_company,
        'share_count': share_count,
        'comment_count': comment_count,
        'desc': formatData(str(desc)[1:-1:])}

    print(data)
    save_result_album(data)

    soup = BeautifulSoup(res.text, 'lxml')
    textarea = (soup.find('textarea'))
    textarea = textarea.text
    if textarea.isspace() != True:
        json_res = json.loads(textarea)
        global is_china
        for item in json_res:
            if is_Chinese(item['name']) == True:
                is_china = 1

            song_data = {
                'artist_id': item['artists'][0]['id'],
                'music_id': item['privilege']['id'],
                'mvid': item['mvid'],
                'name': item['name'],
                'comment_thread_id': item['commentThreadId'],
                'comment_count': get_total(item['privilege']['id']),
                'copyright_id': item['copyrightId'],
                'duration': item['duration'],
                'music_status': item['status'],
                'no': item['no'],
                'score': item['score'],
                'album_id': item['album']['id'],
                'album_name': formatData(item['album']['name']),
                'album_pic_url': item['album']['picUrl']
            }
            save_result_song(song_data)
        print(is_china)


def album(s_id, n):
    """专辑"""
    url = 'https://music.163.com/artist/album?id=%s&limit=12&offset=%d' % (s_id, n)
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
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    tree = etree.HTML(res.text)
    soup = BeautifulSoup(res.text, 'lxml')
    div = (soup.find_all(class_="m-cvrlst m-cvrlst-alb4 f-cb"))
    if div == []:
        return 'gg'
    div = (str(div[0]))
    soup = BeautifulSoup(div, 'lxml')
    li = soup.find_all('li')
    for item in li:
        href = item.a['href']
        id = re.findall('\d+', href)
        id = id[0]
        get_song(id, s_id)


def get_introduce_user(url):
    """user信息"""
    com_id = re.match(".*id=(\d+)", url)
    id = com_id.group(1)

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
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    tree = etree.HTML(res.text)
    # print(res.text)
    tree = etree.HTML(res.text)
    # print(tree)
    home_url = tree.xpath('//*[@id="artist-home"]/@href')

    artist_id = id  # artist id
    global user_id, is_china
    if home_url == [] or home_url == None:
        nickname = tree.xpath('//*[@id="artist-name"]/text()')  # user 名字
        if nickname == []:
            return '没有相关歌手'

        if is_Chinese(nickname[0]) == True:  # 是否中文名字
            is_china = 1
        else:
            is_china = 3

        description = get_intro(id)  # user 简介
        if description == []:
            description = ''
        else:
            description = description[0]

        page = 0
        while True:
            result = album(id, page)
            if result == 'gg':
                break
            page += 12

        data = {
            "artist_id": artist_id,
            "nickname": nickname[0],
            "description": description,
            "is_china": is_china
        }
        print(data)
        save_result_user_to(data)

    # 有个人主页模块
    else:
        user_id = re.findall('\d+', home_url[0])  # user id

        soup = BeautifulSoup(res.text, 'lxml')
        name = soup.find('title')
        # print(name.text)
        head_img, tag, gender, dynamic_count, follower_count, fans_count, region, nickname, introduce, other_contact, is_china = \
            get_homepage(user_id[0])

        description = get_intro(id)
        if description == []:
            description = ''
        else:
            description = description[0]

        page = 0
        while True:
            result = album(id, page)
            if result == 'gg':
                break
            page += 12

        data = {
            "artist_id": artist_id,
            "user_id": user_id[0],
            "nickname": nickname[0],
            "description": formatData(description),
            "home_url": home_url[0],
            "head_img": str(head_img[0]),
            "tag": str(tag),
            "gender": str(gender[0])[1],
            "dynamic_count": dynamic_count[0],
            "follower_count": follower_count[0],
            "fans_count": fans_count[0],
            "region": str(region),
            "other_contact": other_contact,
            "introduce": introduce,
            "is_china": is_china
        }

        print(data)
        save_result_user(data)


q = queue.Queue(maxsize=60)


def Producer():
    music_id = 1880
    while True:
        url = 'https://music.163.com/artist?id={}'.format(music_id)
        q.put(url)
        music_id += 1


def Consumer():
    '''消费者'''
    while True:
        i = q.get()  # 从队列中取数据
        get_introduce_user(i)
        # time.sleep(1)


def main():
    p = threading.Thread(target=Producer)
    threads = [threading.Thread(target=Consumer) for _ in range(30)]
    for thread in threads:
        thread.start()
    p.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
