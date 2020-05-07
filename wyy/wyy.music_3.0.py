import json
import queue
import random
import threading

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from qq.proxies_s import verify_ip
from wyy.save_wyy import save_result_user, save_result_song, save_result_user_to

from wyy.wyy_function import is_Chinese, get_intro, formatData, get_total, get_homepage
# from fake_useragent import UserAgent

from wyy.wyy_parameter import get_json


def get_introduce_user(id):
    """user信息"""
    url = 'https://music.163.com/artist?id={}'.format(id)
    ua = UserAgent()
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        'User-Agent': ua.random,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://music.163.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    global user_id
    is_china = 3

    ip = verify_ip()
    proxy = {
        'http': 'http://' + ip["ip"] + ':' + ip["port"],
    }

    res = requests.get(url, headers=headers, proxies=proxy)

    tree = etree.HTML(res.text)
    hot_50 = tree.xpath('//*[@id="artist-top50"]')
    if hot_50 != []:
        #  热门歌曲
        soup = BeautifulSoup(res.text, 'lxml')
        textarea = (soup.find('textarea'))
        textarea = textarea.text
        if textarea.isspace() != True:
            json_res = json.loads(textarea)
            for item in json_res:
                if is_Chinese(item['name']) == True:
                    is_china = 1
                song_data = {
                    'artist_id': item['artists'][0]['id'],
                    'music_id': item['privilege']['id'],
                    'mvid': item['mvid'],
                    'name': item['name'],
                    'comment_thread_id': item['commentThreadId'],
                    'comment_count': get_json(item['privilege']['id']),
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
                print(song_data)

    nickname = tree.xpath('//*[@id="artist-name"]/text()')  # user 名字
    if nickname == []:
        print('没有相关歌手', id)
        return '没有相关歌手'

    home_url = tree.xpath('//*[@id="artist-home"]/@href')
    artist_id = id  # artist id

    if home_url == []:
        if is_china != 1:
            if is_Chinese(nickname[0]) == True:  # 是否中文名字
                is_china = 1
        description = get_intro(id)  # user 简介
        if description == []:
            description = ''
        else:
            description = description[0]
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
        head_img, tag, gender, dynamic_count, follower_count, fans_count, region, nickname, introduce, other_contact, is_chinas = \
            get_homepage(user_id[0])
        if is_china == 1 and is_chinas == 3:
            is_china = 1
        description = get_intro(id)
        if description == []:
            description = ''
        else:
            description = description[0]
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

gLock = threading.Lock()


def Producer():
    music_id = 195971
    while True:
        # gLock.acquire()
        id = music_id
        q.put(id)

        music_id += 1
        # gLock.release()


def Consumer():
    '''消费者'''
    while True:
        gLock.acquire()
        i = q.get()  # 从队列中取数据
        gLock.release()

        get_introduce_user(i)
        # time.sleep(1)


def main():
    p = threading.Thread(target=Producer)
    p.start()
    threads = [threading.Thread(target=Consumer) for _ in range(30)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


#
if __name__ == '__main__':
    main()
# get_introduce_user(1885)
