import json

import pymysql
import requests

# url = "https://paipianbang.com/api/v3/homepages/search?token=8be3ee559aaf08c6de44&page=1&per_page=20"
url = "https://paipianbang.com/api/v3/homepages/search?token=8be3ee559aaf08c6de44&page=2&per_page=20 "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
}
# res = requests.get(url,headers=headers)
# print(res.text)

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

        sql = f'insert ignore into  muxy_data ' \
              f'(uid,`name`,avatar_url,signature,intro,city,grouped_films_count_description,business_name,career_years,has_freetime)' \
              f'values ("{data["id"]}", "{data["nonblank_name"]}","{data["avatar_url"]}", "{data["signature"]}", ' \
              f'"{data["intro"]}", "{data["city"]}", "{data["grouped_films_count_description"]}", "{data["business_name"]}",' \
              f' "{data["career_years"]}", "{data["has_freetime"]}")'
        # print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)
        print(sql)



# for item in range(1,500):
#     url = "https://paipianbang.com/api/v3/homepages/search?token=8be3ee559aaf08c6de44&page={}&per_page=20".format(item)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
#     }
#     res = requests.get(url,headers=headers)
#     if res.status_code == 500:
#         print(res.status_code)
#         continue
#     con = json.loads(res.text)
#     members = con["members"]
#     data = {}
#     for item in members:
#         # print(item)
#         id = item["id"]
#         data["id"] = id
#         nonblank_name = item["nonblank_name"]
#         data["nonblank_name"] =nonblank_name
#         avatar_url = item["avatar_url"]
#         data["avatar_url"] = avatar_url
#         signature = item["signature"]
#         data["signature"] = signature
#         intro = item["intro"]
#         intro =  formatData(intro)
#         data["intro"] = intro
#         city = item["city"]
#         data["city"] = city
#         grouped_films_count_description = item["grouped_films_count_description"]
#         data["grouped_films_count_description"] = grouped_films_count_description
#         business_name = item["business_name"]
#         data["business_name"] = business_name
#         career_years = item["career_years"]
#         data["career_years"] = career_years
#         has_freetime = item["has_freetime"]
#         if has_freetime:
#             data["has_freetime"] = "1"
#
#         else:
#             data["has_freetime"] = "2"

        # save_result_album(data)
        # print(id,nonblank_name,avatar_url,signature,intro,city,grouped_films_count_description,business_name,career_years)




# url = "https://paipianbang.com/api/v3/homepages/search?token=8be3ee559aaf08c6de44&page=1&per_page=20"
# url = "https://paipianbang.com/api/v3/homepages/search?token=8be3ee559aaf08c6de44&page=2&per_page=20 "
# url = "https://paipianbang.com/api/v3/members/infos?token=token&id=1256"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
# }
# # res = requests.get(url,headers=headers)
# # print(res.text)
# # for item in range(1,10000):
# #     url = "https://paipianbang.com/api/v3/members/infos?token=token&id={}"
# #     res = requests.get(url.format(item),headers=headers)
# #     print(res.text)
#
#
# url = "https://paipianbang.com/api/v2/members/1281121"
#
# # PUT /api/v2/members/1281121 HTTP/1.1
# headers = {
# "X-DEVICE-ID":"23424174",
# "X-Access-Token": "8be3ee559aaf08c6de44",
# "UA": "CineHello ANDROID APP ver 20200208",
# "X-APP-VER": "5.5.8",
# "X-Member-UUID": "5748d541-8bf7-4383-b7ba-6662811f1e55",
# "X-Member-Token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MTI4MTEyMSwidXVpZCI6IjU3NDhkNTQxLThiZjctNDM4My1iN2JhLTY2NjI4MTFmMWU1NSIsImV4cCI6MTYxNDkzOTc1MX0._MUDFXikmcYyAA5cIeQAMTIAAl5Ep9nYcHtpGIp_ytY",
# "Content-Type": "application/json; charset=utf-8",
# "Content-Length": "34",
# "Host": "paipianbang.com",
# "Connection": "Keep-Alive",
# "Accept-Encoding": "gzip",
# "User-Agent": "okhttp/3.11.0",
# }
#
#
#
# data = {
#     "jpush_id": "1104a897923c96248e6"
# }
# res = requests.put(url,data=json.dumps(data),headers=headers)
# print(res.text)


url = 'https://coop.incopat.com/appservice/patentBazaar/findAll.json'

headers = {
"Host": "coop.incopat.com",
"Connection": "keep-alive",
"Content-Length": "176",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
"content-type": "application/x-www-form-urlencoded",
"Referer": "https://servicewechat.com/wxe401d5b43c80899d/158/page-frame.html",
"Accept-Encoding": "gzip, deflate, br",
}
# data = {"pageNumber":"5&pageSize=10&shopName=%E5%85%A8%E9%83%A8&patentType=%E5%85%A8%E9%83%A8&payType=%E5%85%A8%E9%83%A8&orderBy=%E9%BB%98%E8%AE%A4&orderByType=%E5%8D%87%E5%BA%8F&keyword="}
data = {"token=&secretKey=&patentBazaarId=9922"}

res = requests.post(url,headers=headers,data=data)
print(res.text)

url = "https://coop.incopat.com/appservice/patentBazaar/detail.json"
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "65",
"Host": "coop.incopat.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.0",

}
# data = {"token=&secretKey=pZzYZNc6JiWFaWgXzJJ5JQ==&patentBazaarId=9996"}
data = {
        "token":"",
        "secretKey":"",
        "patentBazaarId":"123"
}
res = requests.post(url,headers=headers,data=data)
print(res.text)
