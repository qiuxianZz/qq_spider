# -*- coding: UTF-8 -*-
import datetime
import re
import threading
import time
from threading import Thread

import pymysql
import requests
from lxml import etree
from requests.adapters import HTTPAdapter

s = requests.session()

s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))


def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        # host='101.133.130.11',
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='qx_data'
    )
    return conn


def execute_sql(sql, conn):
    # 获取游标
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def close_conn(conn):
    conn.commit()
    # 关闭连接
    conn.close()


def formatData(data):
    """处理sql字符串引号"""
    if (data == None or data == ''):
        return ""
    data = data.replace("'", "\\\'")
    return data.replace('"', '\\\"')


def save_con(con):
    try:
        conn = get_conn()
        select_sql = 'select phone from ddztb_data where phone = \'{}\''.format(con["phone"])
        cursor = conn.cursor()
        cursor.execute(select_sql)
        res = cursor.fetchall()
        if res == ():
            sql = 'INSERT INTO ddztb_data (company,auth,tag,`name`,phone,tel,`add`,`code`) VALUES' \
                  f'("{con["company"]}","{con["auth"]}", "{con["tag"]}", "{con["name"]}", "{con["phone"]}"' \
                  f',"{con["tel"]}","{con["add"]}","{con["code"]}") '
            print(sql)
            execute_sql(sql, conn)
        close_conn(conn)

    except Exception as e:
        print(e)


def getcon(id):
    print(id)
    url = 'http://www.ddztb.com/qiye/{}/contact.html'.format(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',

    }

    res = s.get(url, headers=headers)
    tree = etree.HTML(res.text)

    n = tree.xpath('/html/body/div[1]/div/div[1]/h1/text()')
    if n == []:
        return
    data = {}
    a = tree.xpath('/html/body/div[3]/div[1]/div[1]/div[2]')
    con = a[0].xpath('string(.)').strip()
    auth = re.findall('公司认证：(.*?)主营产品', con, re.S)
    if auth == []:
        data['auth'] = ''
    else:
        data['auth'] = auth[0]

    tag = re.findall('主营产品：(.*?)公司地址', con, re.S)
    if tag == []:
        data['tag'] = ''
    else:
        data['tag'] = tag[0]
    aa = tree.xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/ul')
    con = aa[0].xpath('string(.)').strip()



    name = re.findall('联系人：(.*?)手机', con, re.S)
    if name != []:
        data['name'] = name[0]
    else:
        data['name'] = ''
    company = re.findall('公司名称：(.*?)公司电话', con, re.S)
    if company == []:
        data['company'] = ''
    else:
        data['company'] = company[0]
    phone = re.findall('手机：(.*?)公司名称', con, re.S)
    if phone != []:
        data['phone'] = phone[0]
    else:
        data['phone'] = ''

    tel = re.findall('公司电话：(.*?)传真', con, re.S)
    if tel == []:
        tel = re.findall('公司电话：(.*?)地址', con, re.S)
        if tel == []:
            data['tel'] = ''
        else:
            data['tel']= tel[0]
    else:
        data['tel'] = tel[0]

    tel = re.findall('公司电话：(.*?)地址', con, re.S)
    if tel == []:
        data['tel'] = ''
    else:
        data['tel'] = tel[0]

    add = re.findall('地址：(.*?)邮编', con, re.S)
    if add == []:
        data['add'] = ''
    else:
        data['add'] = add[0]
    code = re.findall('邮编：(.*?)公司主页', con, re.S)
    if code == []:
        data['code'] = ''
    else:
        data['code'] = code[0]
    print(data)
    return data


# # getcon(1100148)
# id = 1100000
# while True:
#     con = getcon(id)
#     save_con(con)
#     id += 1


# q = queue.Queue()

#
# def Producer():
#     while True:
#         uid = counter()
#         q.put(uid)
#         uid += 1
#


def async_call(func):
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
#
@async_call
def Consumer():
    '''消费者'''
    while True:
        # uid = q.get()
        uid = counter()
        # if uid > 1000000:
        #     print("+++++++++++++++++++++++++++++")
        #     return
        con = getcon(uid)
        if con != None:
            save_con(con)


def run():
    # p = threading.Thread(target=Producer)
    # p.start()
    threads = [threading.Thread(target=Consumer) for _ in range(1)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def increase():  # 定义一个还有自然数算法的生成器,企图使用next来完成不断调用的递增
    # n = 1198852
    n = 706278
    # n = 0
    while True:
        n = n + 1
        yield n




def counter():  # 再定义一内函数
    return next(it)  # 调用生成器的值,每次调用均自增（
    # 注意：it不要加()括号调用会出错的


if __name__ == '__main__':
    # start = datetime.datetime.now()
    it = increase()  # 一定要将生成器转给一个(生成器)对象,才可以完成,笔者第一次做,这里一直出问题,
    run()
    # print("=================================")
    # end = datetime.datetime.now()
    # print("时间:  " + str((end - start).seconds))



# sql = 'CREATE TABLE `ddztb_data` (`id` int(11) NOT NULL AUTO_INCREMENT,`auth` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,`tag` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,`name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,`phone` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,`tel` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,`add` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,`code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,`insert_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,`update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=3578 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;'

    # uid = 1000000
    # while True:
    #     data = getcon(uid)
    #     if data != None:
    #         save_con(data)
    #     uid += 1
