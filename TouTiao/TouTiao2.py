import re
import threading

import requests

from nwerank.db_helper import get_conn, execute_sql, close_conn
from qq.qq_function import formatData


def save_result(data):
    """存储账号数据"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        sql = "INSERT IGNORE INTO Users_post " \
              "(`name`,img,guanzhu,fensi,url)" \
              "values ('%s','%s','%s','%s'," \
              "'%s')" % (formatData(data["name"]), formatData(data["img"]),formatData(data["guanzhu"]),formatData(data["fensi"]),formatData(data["url"]))

        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def website_t(id):
    """网站账号内容"""

    url = 'https://www.toutiao.com/c/user/%s/'%id
    print(url)


    header = {
        "Connection":"keep-alive",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"https://www.toutiao.com/c/user/5954781019/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }
    r = requests.get(url,headers=header)
    # print(r.text)

    patterns = re.compile('media_id:\'(.*?)\',',re.S)

    # id = patterns.findall(r.text)
    # print(id)
    patterns = re.compile('name:(.*?)avatarUrl:',re.S)
    # url = patterns.findall(json_data)
    name = patterns.findall(r.text)
    # print(name)


    patterns = re.compile('avatarUrl:(.*?)isPgc:',re.S)
    # url = patterns.findall(json_data)
    img = patterns.findall(r.text)
    # print(img)
    # for i in img:
    #     print(i)

    patterns = re.compile('guanzhu:(.*?)fensi:',re.S)
    guanzhu = patterns.findall(r.text)
    # print(guanzhu)

    patterns = re.compile('fensi:(.*?)base_url:',re.S)
    fensi = patterns.findall(r.text)
    # print(fensi)

    # patterns = re.compile('home_url:(.*?)right_knight_sign_status',re.S)
    # a = 'https://www.toutiao.com'
    # url  = patterns.findall(r.text)
    # print(url,11111)
    # url = a+ url[0]
    # print(url)
    data = {
        "name":(name[0].strip().strip('"",')).replace('"', ''),
        "img":(img[0].strip().strip('"",').replace('"', '')),
        "guanzhu":(guanzhu[0].strip().strip('"",').replace('"', '')),
        "fensi":(fensi[0].strip().strip('"",').replace('"', '')),
        "url":str(id)
    }
    # print(data)

    save_result(data=data)

    # return id[0]




# n = 108000
# a = ''
# def f():
#     while True:
#         global n,a
#
#         url ='https://www.toutiao.com/c/user/%d/#mid=%d'% (n,n)
#         print(url)
#         data = website_t(url)
#         if data['name'] != ''and data['name'] != a:
#             save_result(data)
#         a = data['name']
#         print(n)
#         n += 1


# def main():
#
#     threads = [threading.Thread(target=f) for _ in range(50) ]
#     for thread in threads:
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#
# if __name__ == '__main__':
#     main()
#
