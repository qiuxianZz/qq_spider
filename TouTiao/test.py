import requests
import time
from datetime import datetime
import json
import execjs
import hashlib
import re
import csv
from zlib import crc32
from base64 import b64decode
import random
import urllib3
import os
import threading
from queue import Queue
from lxml import etree

# 查看js版本信息
# print(execjs.get().name)
# 屏蔽ssl验证警告
urllib3.disable_warnings()

"""
需要nodejs环境，需要修改subprocess.py文件内的class Popen(object)类中的__init__(..encode='utf-8)否则调用js文件时会报错
请求列表页时.py文件中的ua头要与js文件中一致，不然很难请求到数据，请求详情页时要用ua池否则会封浏览器/ip
会有一些空白表格，是因为该账号七天内为发表内容，或者该账号被封禁
输出结果在此文件所在根目录下/toutiao/
右键运行此py文件，newsign.js文件，toutiao.csv文件需在同一文件夹内
爬取的视频有时效性
"""


# 定义ua池
def headers():
    # 各种PC端
    user_agent_list = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


headers_a = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
}
# 代理ip
proxy = {
    'http': '183.57.44.62:808'
}
# cookies值
cookies = {'s_v_web_id': 'b68312370162a4754efb0510a0f6d394'}


# 获取_signature
def get_signature(user_id, max_behot_time):
    with open('newsign.js', 'r', encoding='utf-8') as f:
        jsData = f.read()
    execjs.get()
    ctx = execjs.compile(jsData).call('tac', str(user_id) + str(
        max_behot_time))  # 复原TAC.sign(userInfo.id + "" + i.param.max_behot_time)
    return ctx


# 获取as,cp
def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
    zz = {}
    now = round(time.time())
    # print(now)  # 获取当前计算机时间
    e = hex(int(now)).upper()[2:]  # hex()转换一个整数对象为16进制的字符串表示
    # print('e:', e)
    a = hashlib.md5()  # hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    # print('a:', a)
    a.update(str(int(now)).encode('utf-8'))
    i = a.hexdigest().upper()
    # print('i:', i)
    if len(e) != 8:
        zz = {'as': '479BB4B7254C150',
              'cp': '7E0AC8874BB0985'}
        return zz
    n = i[:5]
    a = i[-5:]
    r = ''
    s = ''
    for i in range(5):
        s = s + n[i] + e[i]
    for j in range(5):
        r = r + e[j + 3] + a[j]
    zz = {
        'as': 'A1' + s + e[-3:],
        'cp': e[0:3] + r + 'E1'
    }
    # print('zz:', zz)
    return zz


# 获取as,cp,_signature(弃用)
def get_js():
    f = open(r"juejin.js", 'r', encoding='UTF-8')  ##打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    ctx = execjs.compile(htmlstr)
    return ctx.call('get_as_cp_signature')


# print(json.loads(get_js())['as'])


# 文章数据
break_flag = []


def wenzhang(url=None, max_behot_time=0, n=0, csv_name=0):
    max_qingqiu = 50
    headers1 = ['发表时间', '标题', '来源', '所有图片', '文章内容']
    first_url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=%s&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s' % (
        url.split('/')[-2], max_behot_time, get_as_cp()['as'], get_as_cp()['cp'],
        get_signature(url.split('/')[-2], max_behot_time))
    while n < max_qingqiu and not break_flag:
        try:
            # print(url)
            r = requests.get(first_url, headers=headers_a, cookies=cookies)
            data = json.loads(r.text)
            # print(data)
            max_behot_time = data['next']['max_behot_time']
            if max_behot_time:
                article_list = data['data']
                for i in article_list:
                    try:
                        if i['article_genre'] == 'article':
                            res = requests.get('https://www.toutiao.com/i' + i['group_id'], headers=headers(),
                                               cookies=cookies)
                            # time.sleep(1)
                            article_title = re.findall("title: '(.*?)'", res.text)
                            article_content = re.findall("content: '(.*?)'", res.text, re.S)[0]
                            # pattern = re.compile(r"[(a-zA-Z~\-_!@#$%\^\+\*&\\\/\?\|:\.<>{}()';=)*|\d]")
                            # article_content = re.sub(pattern, '', article_content[0])
                            article_content = article_content.replace('&quot;', '').replace('u003C', '<').replace(
                                'u003E',
                                '>').replace(
                                '&#x3D;',
                                '=').replace(
                                'u002F', '/').replace('\\', '')
                            article_images = etree.HTML(article_content)
                            article_image = article_images.xpath('//img/@src')
                            article_time = re.findall("time: '(.*?)'", res.text)
                            article_source = re.findall("source: '(.*?)'", res.text, re.S)
                            result_time = []
                            [result_time.append(i) for i in
                             str(article_time[0]).split(' ')[0].replace('-', ',').split(',')]
                            # print(result_time)
                            cha = (datetime.now() - datetime(int(result_time[0]), int(result_time[1]),
                                                             int(result_time[2]))).days
                            # print(cha)
                            if 30 < cha <= 32:
                                # print('完成')
                                # break_flag.append(1)
                                # break
                                continue
                            if cha > 32:
                                print('完成')
                                break_flag.append(1)
                                break
                            row = {'发表时间': article_time[0], '标题': article_title[0].strip('&quot;'),
                                   '来源': article_source[0],'所有图片':article_image,
                                   '文章内容': article_content.strip()}
                            with open('/toutiao/' + str(csv_name) + '文章.csv', 'a', newline='', encoding='gb18030')as f:
                                f_csv = csv.DictWriter(f, headers1)
                                # f_csv.writeheader()
                                f_csv.writerow(row)
                            print('正在爬取文章:', article_title[0].strip('&quot;'), article_time[0],
                                  'https://www.toutiao.com/i' + i['group_id'])
                            time.sleep(1)
                        else:
                            pass
                    except Exception as e:
                        print(e, 'https://www.toutiao.com/i' + i['group_id'])
                wenzhang(url=url, max_behot_time=max_behot_time, csv_name=csv_name, n=n)
            else:
                pass
        except KeyError:
            n += 1
            print('第' + str(n) + '次请求', first_url)
            time.sleep(1)
            if n == max_qingqiu:
                print('请求超过最大次数')
                break_flag.append(1)
            else:
                pass
        except Exception as e:
            print(e)
    else:
        pass

        # print(max_behot_time)
        # print(data)


# 文章详情页数据(已合并到文章数据)
def get_wenzhang_detail(url, csv_name=0):
    headers1 = ['发表时间', '标题', '来源', '文章内容']
    res = requests.get(url, headers=headers_a, cookies=cookies)
    # time.sleep(1)
    article_title = re.findall("title: '(.*?)'", res.text)
    article_content = re.findall("content: '(.*?)'", res.text, re.S)
    pattern = re.compile(r"[(a-zA-Z~\-_!@#$%\^\+\*&\\\/\?\|:\.<>{}()';=)*|\d]")
    article_content = re.sub(pattern, '', article_content[0])
    article_time = re.findall("time: '(.*?)'", res.text)
    article_source = re.findall("source: '(.*?)'", res.text, re.S)
    result_time = []
    [result_time.append(i) for i in str(article_time[0]).split(' ')[0].replace('-', ',').split(',')]
    # print(result_time)
    cha = (datetime.now() - datetime(int(result_time[0]), int(result_time[1]), int(result_time[2]))).days
    # print(cha)
    if cha > 8:
        return None

    row = {'发表时间': article_time[0], '标题': article_title[0].strip('&quot;'), '来源': article_source[0],
           '文章内容': article_content.strip()}
    with open('/toutiao/' + str(csv_name) + '文章.csv', 'a', newline='')as f:
        f_csv = csv.DictWriter(f, headers1)
        # f_csv.writeheader()
        f_csv.writerow(row)
    print('正在爬取文章:', article_title[0].strip('&quot;'), article_time[0], url)
    time.sleep(0.5)
    return 'ok'


# 视频数据
break_flag_video = []


def shipin(url, max_behot_time=0, csv_name=0, n=0):
    max_qingqiu = 20
    headers2 = ['视频发表时间', '标题', '来源', '视频链接']
    first_url = 'https://www.toutiao.com/c/user/article/?page_type=0&user_id=%s&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s' % (
        url.split('/')[-2], max_behot_time, get_as_cp()['as'], get_as_cp()['cp'],
        get_signature(url.split('/')[-2], max_behot_time))
    while n < max_qingqiu and not break_flag_video:
        try:
            res = requests.get(first_url, headers=headers_a, cookies=cookies)
            data = json.loads(res.text)
            # print(data)
            max_behot_time = data['next']['max_behot_time']
            if max_behot_time:
                video_list = data['data']
                for i in video_list:
                    try:
                        start_time = i['behot_time']
                        video_title = i['title']
                        video_source = i['source']
                        detail_url = 'https://www.ixigua.com/i' + i['item_id']

                        resp = requests.get(detail_url, headers=headers())
                        r = str(random.random())[2:]
                        url_part = "/video/urls/v/1/toutiao/mp4/{}?r={}".format(
                            re.findall('"video_id":"(.*?)"', resp.text)[0], r)
                        s = crc32(url_part.encode())
                        api_url = "https://ib.365yg.com{}&s={}".format(url_part, s)
                        resp = requests.get(api_url, headers=headers())
                        j_resp = resp.json()
                        video_url = j_resp['data']['video_list']['video_1']['main_url']
                        video_url = b64decode(video_url.encode()).decode()
                        # print((int(str(time.time()).split('.')[0])-start_time)/86400)
                        if 30 < (int(str(time.time()).split('.')[0]) - start_time) / 86400 <= 32:
                            # print('完成')
                            # break_flag_video.append(1)
                            continue
                        if (int(str(time.time()).split('.')[0]) - start_time) / 86400 > 32:
                            print('完成')
                            break_flag_video.append(1)
                            break
                        row = {'视频发表时间': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)),
                               '标题': video_title, '来源': video_source,
                               '视频链接': video_url}
                        with open('/toutiao/' + str(csv_name) + '视频.csv', 'a', newline='', encoding='gb18030')as f:
                            f_csv = csv.DictWriter(f, headers2)
                            # f_csv.writeheader()
                            f_csv.writerow(row)
                        print('正在爬取视频：', video_title, detail_url, video_url)
                        time.sleep(3)
                    except Exception as e:
                        print(e, 'https://www.ixigua.com/i' + i['item_id'])
                shipin(url=url, max_behot_time=max_behot_time, csv_name=csv_name, n=n)
        except KeyError:
            n += 1
            print('第' + str(n) + '次请求', first_url)
            time.sleep(3)
            if n == max_qingqiu:
                print('请求超过最大次数')
                break_flag_video.append(1)
        except Exception as e:
            print(e)
    else:
        pass


# 微头条
break_flag_weitoutiao = []


def weitoutiao(url, max_behot_time=0, n=0, csv_name=0):
    max_qingqiu = 20
    headers3 = ['微头条发表时间', '来源', '标题', '文章内图片', '微头条内容']
    while n < max_qingqiu and not break_flag_weitoutiao:
        try:

            first_url = 'https://www.toutiao.com/api/pc/feed/?category=pc_profile_ugc&utm_source=toutiao&visit_user_id=%s&max_behot_time=%s' % (
                url.split('/')[-2], max_behot_time)
            # print(first_url)
            res = requests.get(first_url, headers=headers_a, cookies=cookies)
            data = json.loads(res.text)
            # print(data)
            max_behot_time = data['next']['max_behot_time']
            weitoutiao_list = data['data']
            for i in weitoutiao_list:
                try:
                    detail_url = 'https://www.toutiao.com/a' + str(i['concern_talk_cell']['id'])
                    # print(detail_url)
                    resp = requests.get(detail_url, headers=headers(), cookies=cookies)
                    start_time = re.findall("time: '(.*?)'", resp.text, re.S)
                    weitoutiao_name = re.findall("name: '(.*?)'", resp.text, re.S)
                    weitoutiao_title = re.findall("title: '(.*?)'", resp.text, re.S)
                    weitoutiao_images = re.findall('images: \["(.*?)"\]',resp.text,re.S)
                    # print(weitoutiao_images)
                    if weitoutiao_images:
                        weitoutiao_image = 'http:' + weitoutiao_images[0].replace('u002F','/').replace('\\','')
                        # print(weitoutiao_image)
                    else:
                        weitoutiao_image = '此头条内无附件图片'
                    weitoutiao_content = re.findall("content: '(.*?)'", resp.text, re.S)
                    result_time = []
                    [result_time.append(i) for i in str(start_time[0]).split(' ')[0].replace('-', ',').split(',')]
                    # print(result_time)
                    cha = (
                            datetime.now() - datetime(int(result_time[0]), int(result_time[1]), int(result_time[2]))).days
                    # print(cha)
                    if cha > 30:
                        break_flag_weitoutiao.append(1)
                        print('完成')
                        break
                    row = {'微头条发表时间': start_time[0], '来源': weitoutiao_name[0],
                           '标题': weitoutiao_title[0].strip('&quot;'),'文章内图片': weitoutiao_image,
                           '微头条内容': weitoutiao_content[0].strip('&quot;')}
                    with open('/toutiao/' + str(csv_name) + '微头条.csv', 'a', newline='', encoding='gb18030')as f:
                        f_csv = csv.DictWriter(f, headers3)
                        # f_csv.writeheader()
                        f_csv.writerow(row)
                    time.sleep(1)
                    print('正在爬取微头条', weitoutiao_name[0], start_time[0], detail_url)
                except Exception as e:
                    print(e, 'https://www.toutiao.com/a' + str(i['concern_talk_cell']['id']))
            weitoutiao(url=url, max_behot_time=max_behot_time, csv_name=csv_name, n=n)
        except KeyError:
            n += 1
            print('第' + str(n) + '次请求')
            time.sleep(2)
            if n == max_qingqiu:
                print('请求超过最大次数')
                break_flag_weitoutiao.append(1)
            else:
                pass
        except Exception as e:
            print(e)
    else:
        pass


# 获取需要爬取的网站数据
def csv_read(path):
    data = []
    with open(path, 'r', encoding='gb18030') as f:
        reader = csv.reader(f, dialect='excel')
        for row in reader:
            data.append(row)
    return data


# 启动函数
def main():
    for j, i in enumerate(csv_read('toutiao-suoyou.csv')):
        # data_url = data.get_nowait()
        if '文章' in i[3]:
            # 启动抓取文章函数
            print('当前正在抓取文章第', j, i[2])
            headers1 = ['发表时间', '标题', '来源', '所有图片', '文章内容']
            with open('/toutiao/' + i[0] + '文章.csv', 'a', newline='')as f:
                f_csv = csv.DictWriter(f, headers1)
                f_csv.writeheader()
            break_flag.clear()
            wenzhang(url=i[2], csv_name=i[0])

        if '视频' in i[3]:
            # 启动爬取视频的函数
            print('当前正在抓取视频第', j, i[2])
            headers2 = ['视频发表时间', '标题', '来源', '视频链接']
            with open('/toutiao/' + i[0] + '视频.csv', 'a', newline='')as f:
                f_csv = csv.DictWriter(f, headers2)
                f_csv.writeheader()
            break_flag_video.clear()
            shipin(url=i[2], csv_name=i[0])

        if '微头条' in i[3]:
            # 启动获取微头条的函数
            headers3 = ['微头条发表时间', '来源', '标题', '文章内图片', '微头条内容']
            print('当前正在抓取微头条第', j, i[2])
            with open('/toutiao/' + i[0] + '微头条.csv', 'a', newline='')as f:
                f_csv = csv.DictWriter(f, headers3)
                f_csv.writeheader()
            break_flag_weitoutiao.clear()
            weitoutiao(url=i[2], csv_name=i[0])


# 多线程启用
def get_all(urlQueue):
    while True:
        try:
            # 不阻塞的读取队列数据
            data_url = urlQueue.get_nowait()
            # i = urlQueue.qsize()
        except Exception as e:
            break
        # print(data_url)
        # if '文章' in data_url[3]:
        #     # 启动抓取文章函数
        #     print('当前正在抓取文章', data_url[2])
        #     headers1 = ['发表时间', '标题', '来源', '所有图片', '文章内容']
        #     with open('/toutiao/' + data_url[0] + '文章.csv', 'a', newline='')as f:
        #         f_csv = csv.DictWriter(f, headers1)
        #         f_csv.writeheader()
        #     break_flag.clear()
        #     wenzhang(url=data_url[2], csv_name=data_url[0])

        if '视频' in data_url[3]:
            # 启动爬取视频的函数
            print('当前正在抓取视频', data_url[2])
            headers2 = ['视频发表时间', '标题', '来源', '视频链接']
            with open('/toutiao/' + data_url[0] + '视频.csv', 'a', newline='')as f:
                f_csv = csv.DictWriter(f, headers2)
                f_csv.writeheader()
            break_flag_video.clear()
            shipin(url=data_url[2], csv_name=data_url[0])
            #
        # if '微头条' in data_url[3]:
        #     # 启动获取微头条的函数
        #     headers3 = ['微头条发表时间', '来源', '标题','文章内图片', '微头条内容']
        #     print('当前正在抓取微头条', data_url[2])
        #     with open('/toutiao/' + data_url[0] + '微头条.csv', 'a', newline='')as f:
        #         f_csv = csv.DictWriter(f, headers3)
        #         f_csv.writeheader()
        #     break_flag_weitoutiao.clear()
        #     weitoutiao(url=data_url[2], csv_name=data_url[0])


if __name__ == '__main__':
    # 创建存储目录
    path = '/toutiao/'
    if not os.path.exists(path):
        os.mkdir(path)

    """单一脚本使用main函数，开启多线程按照下面方法控制线程数，开启多线程会请求过于频繁，导致头条反爬封ip等，需要设置代理ip"""
    # main()


    urlQueue = Queue()
    for j, i in enumerate(csv_read('toutiao-suoyou.csv')):
        urlQueue.put(i)
    # print(urlQueue.get_nowait())
    # print(urlQueue.qsize())
    threads = []
    # 可以调节线程数， 进而控制抓取速度
    threadNum = 4
    for i in range(0, threadNum):
        t = threading.Thread(target=get_all, args=(urlQueue,))
        threads.append(t)

    for t in threads:
        # 设置为守护线程,当守护线程退出时,由它启动的其它子线程将同时退出,
        # t.setDaemon(True)
        t.start()
    for t in threads:
        # 多线程多join的情况下，依次执行各线程的join方法, 这样可以确保主线程最后退出， 且各个线程间没有阻塞
        t.join()

        # pass