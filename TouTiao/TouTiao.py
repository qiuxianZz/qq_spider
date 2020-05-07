import json
import random
import re
import time
import execjs
import requests



from nwerank.db_helper import get_conn, execute_sql, close_conn


def get_article():
    res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    proxies_list = json.loads(res.text)
    proxies = (proxies_list['RESULT'])
    # print(random.choice(proxies))

    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.toutiao.com/c/user/5954781019/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    dic = get_cpas()
    as1 = dic['as']
    cp = dic['cp']
    url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=={}&max_behot_time={}&count=20&as={}&cp={}'.format(
        53335521365, 0, as1, cp)
    res = requests.get(url, headers=header, proxies=random.choice(proxies))
    print(res.text)


def website_t(id):
    """网站账号内容"""

    url = 'https://www.toutiao.com/c/user/%s/' % id
    print(url)

    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.toutiao.com/c/user/5954781019/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    r = requests.get(url, headers=header)
    # print(r.text)

    patterns = re.compile('media_id:\'(.*?)\',', re.S)

    # id = patterns.findall(r.text)
    # print(id)
    patterns = re.compile('name:(.*?)avatarUrl:', re.S)
    # url = patterns.findall(json_data)
    name = patterns.findall(r.text)
    # print(name)

    patterns = re.compile('avatarUrl:(.*?)isPgc:', re.S)
    # url = patterns.findall(json_data)
    img = patterns.findall(r.text)
    # print(img)
    # for i in img:
    #     print(i)

    patterns = re.compile('guanzhu:(.*?)fensi:', re.S)
    guanzhu = patterns.findall(r.text)
    # print(guanzhu)

    patterns = re.compile('fensi:(.*?)base_url:', re.S)
    fensi = patterns.findall(r.text)
    # print(fensi)

    # patterns = re.compile('home_url:(.*?)right_knight_sign_status',re.S)
    # a = 'https://www.toutiao.com'
    # url  = patterns.findall(r.text)
    # print(url,11111)
    # url = a+ url[0]
    # print(url)
    data = {
        "name": (name[0].strip().strip('"",')).replace('"', ''),
        "img": (img[0].strip().strip('"",').replace('"', '')),
        "guanzhu": (guanzhu[0].strip().strip('"",').replace('"', '')),
        "fensi": (fensi[0].strip().strip('"",').replace('"', '')),
        "url": str(id)
    }
    # print(data)

    save_result(data=data)


def json_con(url):
    """文章内容"""
    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.toutiao.com/c/user/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    # res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    # proxies_list = json.loads(res.text)
    # proxies = (proxies_list['RESULT'])

    res = requests.get(url, headers=header)
    print("==========================")

    json_res = json.loads(res.text)
    print(json_res)
    if (json_res['data'] == None or len(json_res['data']) == 0):
        url = 'https://www.toutiao.com/c/user/article/?' \
              'page_type={}&user_id={}&max_behot_time=0&count=20'
        return url.format(1,uid)

    max_behot_time = json_res["next"]['max_behot_time']

    for item in json_res['data']:
        if item["behot_time"] <= max_time:
            return 'GG'

        # print(item)
        if item['single_mode'] == None:
            item['image_url'] = None
            save_result(item)
            # print('成功存入数据')
        else:
            save_result(item)
    print('成功存入数据')

    url = 'https://www.toutiao.com/c/user/article/?' \
          'page_type=0&user_id=%s&max_behot_time=%s&count=20' % (
              uid, max_behot_time)
    return max_behot_time


def transfer_time(t):
    """时间戳转换成格式时间"""

    timestamp = int(t)
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2017-09-16 11:28:54)
    dtime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    return dtime


def save_result(data):
    """存储数据"""
    try:
        conn = get_conn()
        sql = "INSERT IGNORE INTO TouTiao " \
              "(img,titles,pageview,comments,time,url)" \
              "values ('%s','%s','%s'," \
              "'%s','%s','%s')" % (data["image_url"], data["title"], data["go_detail_count"], data["comments_count"],
                                   transfer_time(data["behot_time"]), data["source_url"][6:-1:])
        print(sql)
        # execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def get_cpas():
    """cp as"""
    with open('ascp.js', 'r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a')


def get_sign(id, t):
    """_signature"""
    with open('sign.js', 'r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a', id, t)


def timeStamp_(Y, m, d, H, M, S):
    tss = '%s-%s-%s %s:%s:%s' % (Y, m, d, H, M, S)
    timeArray = time.strptime(tss, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def main():
    # get_article()

    global uid, max_time
    max_time = timeStamp_(2019, 10, 10, 00, 00, 00)

    user_id = [95858796570, 4931329242, 5443257860, 5856631223, 2053497172272163, 52270200701, 15628441699, 92759961612,
               100118439201, 6989512897, 20353903130, 5263800450, 61749076352, 61746455612,
               61746388948, 67627004851, 61749473542, 61748360588, 61749472947, 61747696266, 61745883201, 60067064925,
               61748538913, 61748261798, 5910115546, 61747700995, 97082579926, 50226404364, 70318658273751670122517774]
    # user_id = [5954781019]
    # user_id = website_t(url='https://www.toutiao.com/c/user/relation/5954781019/?tab=following#mid=5954781019')
    for uid in user_id:
        print(uid)
        print("__________________________________________________")
        # website_t(item)
        url = 'https://www.toutiao.com/c/user/article/?' \
              'page_type={}&user_id={}&max_behot_time=0&count=20'
        while True:
            url = json_con(url.format(0, uid))
            print(url)
            if url == 'GG':
                break
        time.sleep(5)


if __name__ == '__main__':
    main()

#
# url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=6186597332&max_behot_time=0&count=20&as=A1B5EDCB9244A64&cp=5DB224CAC6E48E1&_signature=6.sbdhAVtlRB1Fv2uawH9uv7G2'

#
# while True:
#     try:
#         url  = json_con(url=url)
#     except KeyError:
#         continue
# a = '/item/6751549814921495043/'
# print(a[6:-1:])
'https://www.toutiao.com/c/user/article/?page_type=0&user_id=95858796570&max_behot_time=0&count=20'
'https://www.toutiao.com/c/user/article/?page_type=1&user_id=95858796570&max_behot_time=0&count=20'


def get_cpas():
    """cp as"""
    with open('ascp.js', 'r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a')



def timeStamp_(Y, m, d, H, M, S):
    tss = '%s-%s-%s %s:%s:%s' % (Y, m, d, H, M, S)
    timeArray = time.strptime(tss, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def TouTiao(url):
    """文章内容"""

    # time.sleep(5)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Referer": "https://www.toutiao.com/c/user/",
    }
    res = requests.get(url, headers=header)
    print(url)
    print(res.text)
    json_res = json.loads(res.text)
    try:
        max_behot_time = json_res['next']
    except:
        time.sleep(10)
        return url
    max_behot_time = json_res['next']['max_behot_time']
    data = json_res['data']
    if (data == None or len(data) == 0):
        return 'GG'

    for item in data:
        # print(item)
        if item["behot_time"] <= max_time:
            return 'GG'
    ascp = get_cpas()
    url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id={}&max_behot_time={}&count=20&as={}&cp={}'.format(uid, max_behot_time,ascp['as'],ascp['cp'])
    return url


def get_content(uid):
    global max_time
    max_time = timeStamp_(2019, 12, 12, 00, 00, 00)
    ascp = get_cpas()

    max_behot_time = 0
    url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id={}&max_behot_time={}&count=20&as={}&cp={}'.format(uid, max_behot_time,ascp['as'],ascp['cp'])
    while True:
        url = TouTiao(url)
        if url =='GG':
            break


def main():
    global uid
    # user_id = [95858796570, 4931329242, 5443257860, 5856631223, 2053497172272163, 52270200701, 15628441699, 92759961612,
    #            100118439201, 6989512897, 20353903130, 5263800450, 61749076352, 61746455612,
    #            61746388948, 67627004851, 61749473542, 61748360588, 61749472947, 61747696266, 61745883201, 60067064925,
    #            61748538913, 61748261798, 5910115546, 61747700995, 97082579926, 50226404364, 70318658273,751670122517774]
    user_id = [3200725091]
    for uid in user_id:
        get_content(uid)


if __name__ == '__main__':
    main()
#
'https://www.toutiao.com/c/user/article/?page_type=0&user_id=70318658273&max_behot_time=0&count=20'
'https://www.toutiao.com/c/user/article/?page_type=0&user_id=70318658273&max_behot_time=0&count=20&as=A1256E6173E056D&cp=5E1350C5762DDE1'
# https://www.toutiao.com/c/user/article/?page_type=1&user_id=70318658273&max_behot_time=0&count=20&as=A105DE51F3E05FF&cp=5E1380351FCFFE1
# https://www.toutiao.com/c/user/article/?page_type=0&user_id=70318658273&max_behot_time=0&count=20&as=A1754E1173105FC&cp=5E1380352F6CAE1
