import re

import pymysql
import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


def get_conn():
    # 建立链接
    conn = pymysql.Connection(
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


def close_conn(conn):
    conn.commit()
    # 关闭连接
    conn.close()


def get_all_url():
    # url = 'http://bj.lieju.com/'
    url = 'http://aq.lieju.com/'
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    data = tree.xpath("/html/body/div[4]/div[1]")
    url_list = []
    for item in data[0]:
        # print(item)
        for i in item:
            res = i.xpath('./div[2]')
            for j in res[0]:
                url_list.append(j.xpath('./a//@href')[0])

    return url_list


# a = get_all_url()
# print(a)
# a = get_href()
# print(a)


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def formatData(data):
    """处理sql字符串引号"""
    if (data == None or data == ''):
        return ""
    data = data.replace("'", "\\\'")
    return data.replace('"', '\\\"')


def get_info(url, tel):
    info = {}
    # url = 'http://aq.lieju.com/jiazheng/43369320.htm'
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    title = tree.xpath('//*[@id="show_title"]/h1/text()')
    info["url"] = url
    info["title"] = title[0]
    type_add = []
    info["tel"] = tel
    a = tree.xpath('//*[@id="mainbox_l"]/div[3]/text()')
    for i in a:
        a = (is_Chinese(i))
        if a:
            type_add.append(i)
    if len(type_add) < 2:
        info["type"] = type_add[0]
        info["location"] = ''
    info["type"] = type_add[0]
    info["location"] = type_add[1]

    name = tree.xpath('//*[@id="mainbox_l"]/div[4]/div[1]/a/b/text()')
    info["contacts"] = name[0]

    c = tree.xpath('//*[@id="mainbox_l"]/div[4]/div[3]/a[1]/@href')
    qq = re.findall('uin=1(.*?)&site', c[0], re.S)
    if qq != []:
        info["qq"] = qq[0]
    info["qq"] = ''
    d = tree.xpath('//*[@id="box"]/text()')
    n = ''
    for i in d:
        n += i
    info["brief"] = formatData(n)

    imgs = tree.xpath('//*[@id="mainbox_l"]/div[7]')
    imgs_list = []
    for i in imgs[0]:
        # print(i)
        img = i.xpath('./@src')
        if img != []:
            imgs_list.append(img[0])

    info["img"] = imgs_list

    return info


def get_href(type, page):
    url = 'http://bj.lieju.com/{}-page-{}/'
    res = requests.get(url.format(type, page), headers=headers)
    tree = etree.HTML(res.text)
    list_left = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]')
    list_href = []
    for item in list_left:
        for i in item:
            href = (i.xpath('./div[1]/a/@href'))
            tel = (i.xpath('./div[3]/a/div/@data-phone'))
            if tel != []:
                tel = (tel[0][:-5:])
            if href != [] and tel != []:
                data = (get_info(href[0], tel))
                save_data(data)
                list_href.append(href[0])

    return list_href


def start(type):
    page = 1
    while True:
        href = get_href(type, page)
        if href == []:
            return
        page += 1


def run():
    serve_list = get_all_url()
    for item in serve_list:
        start(item[20:-1])


def save_data(data):
    print(data["qq"])
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = f'insert ignore into  ljw ' \
              f'(url,title,tel,type,location,contacts,qq,brief,img)' \
              f'values ("{data["url"]}", "{data["title"]}","{data["tel"]}","{data["type"]}", "{data["location"]}", ' \
              f'"{data["contacts"]}", "{data["qq"]}", "{data["brief"]}", "{data["img"]}")'

        print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
