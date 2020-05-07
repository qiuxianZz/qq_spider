import queue
import threading

import pymysql
import requests

import json

# address = ''
# url= 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
# response = requests.get(url)
# answer = response.json()
# lon = float(answer['result']['location']['lng'])
# lat = float(answer['result']['location']['lat'])
# print(lon)
# print(lat)

# provinces = {
#     '吉林省': [125.326800, 43.896160], '黑龙江省': [126.662850, 45.742080],
#     '辽宁省': [123.429250, 41.835710], '内蒙古自治区': [111.765220, 40.817330],
#     '新疆维吾尔自治区': [87.627100, 43.793430], '青海省': [101.780110, 36.620870],
#     '北京市': [116.407170, 39.904690], '天津市': [117.199370, 39.085100],
#     '上海市': [121.473700, 31.230370], '重庆市': [106.550730, 29.564710],
#     '河北省': [114.469790, 38.035990], '河南省': [113.753220, 34.765710],
#     '陕西省': [108.954240, 34.264860], '江苏省': [118.762950, 32.060710],
#     '山东省': [117.020760, 36.668260], '山西省': [112.562720, 37.873430],
#     '甘肃省': [103.826340, 36.059420], '宁夏回族自治区': [106.258670, 38.471170],
#     '四川省': [104.075720, 30.650890], '西藏自治区': [91.117480, 29.647250],
#     '安徽省': [117.285650, 31.861570], '浙江省': [120.153600, 30.265550],
#     '湖北省': [114.342340, 30.545390], '湖南省': [112.983400, 28.112660],
#     '福建省': [119.296590, 26.099820], '江西省': [115.910040, 28.674170],
#     '贵州省': [106.707220, 26.598200], '云南省': [102.709730, 25.045300],
#     '广东省': [113.266270, 23.131710], '广西壮族自治区': [108.327540, 22.815210],
#     '香港': [114.165460, 22.275340], '澳门': [113.549130, 22.198750],
#     '海南省': [110.348630, 20.019970], '台湾省': [121.520076, 25.030724],
# }


#
# for key,value in provinces.items():
#     print(key,value)


def get_data(page):
    # url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiQueryTelList&state=we7sid-ae09d1ce99367ecdab3a69440fb7df8d&sign=4f157a76f7ae6f7b030efe9ea335eb35&type=1&lat=20.019970&lng=110.348630&m=amouse_tel114&pageIndex={}'.format(page)
    url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiQueryTelList&state=we7sid-76d696100681f9a539366d8fd1d93257&sign=09f5b2c28596d9953bac6c6d9ddeaa99&type=1&lat=20.019970&lng=110.348630&m=amouse_tel114&pageIndex={}'.format(
        page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    res = requests.get(url, headers=headers)
    # print(res.text)
    data = json.loads(res.text)
    lists = data["data"]["list"]
    data = {}
    for item in lists:
        data["id"] = (item["id"])
        data["openid"] = item["openid"]
        data["title"] = item["title"]
        data["contact_name"] = item["contact_name"]
        data["info"] = item["info"]
        data["weixin"] = item["weixin"]
        data["logo"] = item["logo"]
        data["mobile"] = item["mobile"]
        data["place"] = item["place"]
        print(data)


# get_data(1)

# for item in range(100):
#     get_data(item)
# 11897
# 131873
# 131802
# 14507
headers = {
    "Host": "cn.bykszb.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/x-www-form-urlencoded",
    "Referer": "https://servicewechat.com/wxa54043f6082835a1/48/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",

    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
}


def get_info(id):
    con = {}
    # url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiGetTelInfo&state=we7sid-76d696100681f9a539366d8fd1d93257&sign=4a4ea61bef88e338a797a0aef02e0803&m=amouse_tel114&id={}'.format(
    #     id)
    url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiGetTelInfo&state=we7sid-bf42856f4bcd80270266b3f7aa701250&sign=43f725eafdc0d0805972c5b7b60881e5&m=amouse_tel114&id={}'.format(id)

    res = requests.get(url, headers=headers)
    data = json.loads(res.text)
    data = data["data"]
    view = data["view"]
    if view == 1:
        return
    con["id"] = (data["id"])
    con["openid"] = data["openid"]
    con["title"] = data["title"]
    con["contact_name"] = data["contact_name"]
    con["info"] = data["info"]
    con["weixin"] = data["weixin"]
    con["logo"] = data["logo"]
    con["mobile"] = data["mobile"]
    con["place"] = data["place"]
    con["cate_title"] = data["cate_title"]
    print(con)
    # save_result_album(data)




def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        host='192.168.2.215',
        port=3306,
        user='test1',
        password='test1',
        database='others'
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
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return  data.replace('"','\\\"')



def save_result_album(data):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = f'insert ignore into  acq_kszb ' \
              f'(uid,open_id,title,contact_name,info,weixin,logo,mobile,place,cate_title)' \
              f'values ("{data["id"]}", "{data["openid"]}","{data["title"]}", "{data["contact_name"]}", ' \
              f'"{data["info"]}", "{data["weixin"]}", "{data["logo"]}", "{data["mobile"]}","{data["cate_title"]}",' \
              f' "{data["place"]}")'
        # print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)
        print(sql)


# if __name__ == '__main__':
#     page = 11895
#     while True:
#         data = get_info(page)
#         if data != None:
#             save_result_album(data)
#         page+=1
#         print(page)
#

q = queue.Queue(maxsize=60)


def Producer():
    music_id = 4454
    while True:
        q.put(music_id)
        music_id += 1


def Consumer():
    '''消费者'''
    while True:
        i = q.get()  # 从队列中取数据
        print(i)
        get_info(i)
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
    # page = 1
    # while True:
    #     get_info(page)
    #     print(page)
    #     page+=1