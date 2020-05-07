import pymysql
import requests
from lxml import etree

#
# url = 'https://www.vvic.com/gz/rank/index?&currentPage=1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

}


# res = requests.get(url,headers = headers)
#
# tree = etree.HTML(res.text)
#
# # a = tree.xpath("/html/body/div[7]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div/p[1]/a[1]//@href")
# tbody = tree.xpath("/html/body/div[7]/div[2]/div/div[2]/table/tbody")
# # for item in tbody[0]:
# #     print(item.xpath("./td[2]/div/p[1]/a[1]//@href"))
#
#
#
#
#
# url = 'https://www.vvic.com/shop/44304'
#
# res = requests.get(url,headers)
# tree = etree.HTML(res.text)
# a = tree.xpath("/html/body/div[7]/div[1]/div/ul/li[2]/div[2]/span/text()")
# b = tree.xpath("/html/body/div[7]/div[1]/div/ul/li[4]/div[2]/p/span[13]/text()")
# c = tree.xpath("/html/body/div[7]/div[1]/div/ul/li[4]/div[2]")
# for item in c[0]:
#     print(item.xpath("./span[13]/text()"))


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


def formatData(data):
    """处理sql字符串引号"""
    if (data == None or data == ''):
        return ""
    data = data.replace("'", "\\\'")
    return data.replace('"', '\\\"')


def save_result_album(uid):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = 'INSERT INTO vvic_user (uid) SELECT {} FROM DUAL WHERE NOT EXISTS (SELECT * FROM vvic_user where uid = {})'.format(uid,uid)
        # print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


# url = 'https://www.vvic.com/gz/shops/19'
# res = requests.get(url,headers=headers)
# tree = etree.HTML(res.text)
# # ul = tree.xpath("/html/body/div[6]/div[3]/div[1]/dl/dd/ul")
# ul = tree.xpath("/html/body/div[6]/div[3]/div[2]/dl[13]/dd/ul")
# for item in ul[0]:
#     data = (item.xpath("./a/@href")[0])[6::]
#     print(item.xpath("./a/@href")[0])
#     save_result_album(data)


def run(id, dl):
    print(id)
    url = 'https://www.vvic.com/gz/shops/{}'.format(id)
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    # ul = tree.xpath("/html/body/div[6]/div[3]/div[1]/dl/dd/ul")
    dl = '/html/body/div[6]/div[3]/div[2]/dl[{}]/dd/ul'.format(dl)
    ul = tree.xpath(dl)
    print(dl)
    try:
        for item in ul[0]:
            data = (item.xpath("./a/@href")[0])[6::]
            print(item.xpath("./a/@href")[0])
            save_result_album(data)
    except IndexError:
        return "end"

a = [12,19,49,55,10,13, 14, 15, 56, 31, 11, 17, 52, 18, 34, 20, 16, 48, 23, 25, 51, 47, 53, 50, 54, 36, 43, 39, 45, 28,
     26, 35, 42, 38, 55]

# for item in a:
#     dl = 1
#     while True:
#         end = run(10, dl)
#         if end =="end":
#             break
#         dl += 1

# url = 'https://www.vvic.com/shop/51634'
# res = requests.get(url,headers=headers)
# print(res.text)
# for i in range(1,32):
#     print(i)
#     # url ='https://www.vvic.com/pn/markets.html?currentPage={}'.format(52)
#     # url ='https://www.vvic.com/hznz/markets.html?currentPage={}'.format(i)
#     # url ='https://www.vvic.com/jfn/markets.html?currentPage={}'.format(i)
#     # url ='https://www.vvic.com/xt/markets.html?currentPage={}'.format(i)
#     url ='https://www.vvic.com/hz/markets.html?currentPage={}'.format(i)
#     res = requests.get(url,headers=headers)
#     tree = etree.HTML(res.text)
#     ul = tree.xpath('//*[@id="shopsListContainer"]')
#     for item in ul[0]:
#         data = item.xpath('./div[2]/div[1]/a/@href')
#         save_result_album(data[0][6::])

for i in range(1,101):

    # url = 'https://www.vvic.com/gz/rank/10000?&tjtime=month&t=top&currentPage={}'.format(i)
    url = 'https://www.vvic.com/gz/rank/10001?&tjtime=month&t=top&currentPage={}'.format(i)
    # url = 'https://www.vvic.com/gz/rank/1?&tjtime=month&t=top&currentPage={}'.format(i)
    print(url)
    res = requests.get(url,headers=headers)
    tree = etree.HTML(res.text)
    tb = tree.xpath('/html/body/div[7]/div[2]/div/div[2]/table/tbody')
    for item in tb[0]:
        data =(item.xpath('./td[2]/div/p[1]/a[1]/@href'))
        print(data[0][6::])
        save_result_album(data[0][6::])
