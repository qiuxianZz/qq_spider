import queue
import random
import re

import threading

import requests
from bs4 import BeautifulSoup
from lxml import etree

from qq.proxies_s import getProxy, verifyProxy
from wyy.save_wyy import save_result_album
from wyy.wyy_function import formatData
from fake_useragent import UserAgent

import logging  # 引入logging模块



# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.ERROR)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件

#

# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# log_path = os.path.dirname(os.getcwd()) + './qq'
# log_name = log_path + rq + '.log'
# logfile = log_name
# fh = logging.FileHandler(logfile, mode='w')

fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] -%(thread)d- %(funcName)s - %(levelname)s: %(message)s")
#创建TimedRotatingFileHandler对象
# log_file_handler = TimedRotatingFileHandler(filename="ds_update", when="D", interval=2, backupCount=2)
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)



IndexError_list = []
def get_song(id):
    """专辑信息"""
    url = 'https://music.163.com/album?id={}'.format(id)
    ua = UserAgent()
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://music.163.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        'User-Agent':ua.random,
    }
    print(headers)
    # while True:
    #     ip = getProxy()
    #     if verifyProxy(ip) == 200:
    #         proxies =  {'https': ip}
    #         # print(proxies)
    #         break
    # res = requests.get(url=url, headers=headers, proxies=proxies)
    # proxies = {'http':"http://117.94.183.226:47312"}
    #     {'http':"http://183.7.171.16:45754"},{'http':"http://115.151.176.73:44622"},,{'http':"http://115.223.125.187:29324"},
    #     {'http':"http://182.98.37.30:27432"},{'http':"http://117.169.78.54.178:17947"},
    #     {'http':"http://117.169.78.54:14961"},{'http':"http://117.169.78.54.119:10822"},
    #     {'http':"http://117.169.78.54:17127"}, {'http':"http://117.169.78.54:18230"}]
    proxie = {'http':"http://49.77.210.113:32513"}



    res = requests.get(url,headers=headers,proxies=proxie)
    tree = etree.HTML(res.text)

    album_id = id  # 专辑id
    # tree = etree.HTML(res.text)
    soup = BeautifulSoup(res.text, 'lxml')

    album_name_ = soup.find("h2")

    album_name = tree.xpath('//div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()')
    if album_name == [] and album_name_ == None:
        # q.task_done()
        logger.error("id的值为：%s",id)
        print('没有此专辑',id)
        return
    try:
        artist_id = tree.xpath('//div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/@href')  # 歌手id
        artist_id = re.findall('\d+', artist_id[0])
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
        a = str(share_count)+str(share_count_)
        share_count = re.findall('\d+', a)
        if share_count == []:
            share_count = 0
        else:
            share_count = share_count[0]
        comment_count = tree.xpath('//*[@id="cnt_comment_count"]/text()')  # 专辑评论数
        if comment_count == ['评论'] or comment_count == []:
            comment_count = 0
        else:
            comment_count = comment_count[0]
        desc = tree.xpath('//*[@id="album-desc-more"]/p/text()')  # 专辑说明
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
    except IndexError:
        IndexError_list.append(id)
    # q.task_done()
    # logger.error("id的值为:%d"%id)

# get_song(9204)

q = queue.Queue(maxsize=500)

gLock = threading.Lock()

def Producer():
    music_id = 7000
    while True:
        id = music_id
        q.put(id)
        music_id += 1


def Consumer():
    '''消费者'''
    while True:
        gLock.acquire()
        i = q.get()  # 从队列中取数据
        gLock.release()
        get_song(i)




def main():
    p = threading.Thread(target=Producer)
    p.start()
    threads = [threading.Thread(target=Consumer)for _ in range(50)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

#
# if __name__ == '__main__':
#     main()

get_song(8206)