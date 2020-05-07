import json
import time

import requests

url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A62%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-03-11%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI4517569888510551&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A27%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-03-11%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI7581969292614168&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A26%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020_10%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI42496843856521194&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3a100%2c%22period%22%3A%222020-03-11%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'

# 热歌榜 url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI08088743888293748&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":26,"offset":0,"num":300,"period":"2020_10"}},"comm":{"ct":24,"cv":0}}'
url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":27,"offset":0,"num":20,"period":"2020-03-11"}},"comm":{"ct":24,"cv":0}}'


# url   = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={'detail': {'module': 'musicToplist.ToplistInfoServer', 'method': 'GetDetail', 'param': {'topId': 27, 'offset': 0, 'num': 0, 'period': '2020-03-11'}}, 'comm': {'ct': 24, 'cv': 0}}'
# # 详情song_mid%22%3A%22 url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI2137817013323291&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22songinfo%22%3A%7B%22method%22%3A%22get_song_detail_yqq%22%2C%22param%22%3A%7B%22song_type%22%3A0%2C%22song_mid%22%3A%22000S7TGL43hhBO%22%2C%22song_id%22%3A244712794%7D%2C%22module%22%3A%22music.pf_song_detail_svr%22%7D%7D'
#
# # 评论数topid url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=255402348&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#
# }
#
# res = requests.get(url,headers=headers)
# print(res.text)

# 欧美榜:3,流行指数榜:4,内地榜:5,港台榜:6,韩国榜:16,日本榜:17,专辑畅销榜:23
# 热歌榜:26,新歌榜:27


for i in range(100,200):
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":%s,"offset":0,"num":20,"period":"2020-03-11"}},"comm":{"ct":24,"cv":0}}'% i
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    title = data["detail"]["data"]["data"]["title"]
    print(title,i)
    time.sleep(2)

# 欧美榜 3,流行指数榜 4,内地榜 5,港台榜 6,韩国榜 16,日本榜 17,专辑畅销榜 23,热歌榜 26,新歌榜 27,网络歌曲榜28,
# 影视金曲榜 29,人气榜 34,K歌金曲榜 36,腾讯音乐人原创榜 52,电音榜 57,说唱榜 58,香港地区榜 59,抖音排行榜 60,
# 台湾地区榜 61,飙升榜 62,综艺新歌榜 64,国风热歌榜 65,ACG新歌榜 66,听歌识曲榜 67,达人音乐榜 70,达人音乐榜 82,
# 台湾Hito中文榜 103,日本公信榜 105,韩国Mnet榜 106,英国UK榜 107,美国公告牌榜 108,香港电台榜 113,香港商台榜 114,
# 美国公告牌榜 121,美国公告牌榜 122,美国iTunes榜 123,JOOX本地热播榜 126,台湾KKBOX榜 127 YouTube音乐排行榜 128,
# 韩国Melon榜 129



# url = 'https://i.y.qq.com/n2/m/share/details/toplist.html?hosteuin=oK6koeoz7wc5Nn**&type=0&id=427&ADTAG=wxfshare&appshare=iphone_wx'
# res = requests.get(url,headers=headers)
# print(res.text)
#
#
# url= 'https://i.y.qq.com/n2/m/share/details/toplist.html?hosteuin=oK6koeoz7wc5Nn**&type=0&id=427&ADTAG=wxfshare&appshare=iphone_wx'
# headers = {
# "Host": "i.y.qq.com",
# "Connection": "keep-alive",
# "Cache-Control": "max-age=0",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
# "Sec-Fetch-Dest": "document",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "Sec-Fetch-Site": "none",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-Use": "1",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cookie": "pgv_info=ssid=s4311605690; ts_last=i.y.qq.com/n2/m/share/details/toplist.html; ts_refer=ADTAGwxfshare; pgv_pvid=291971950; ts_uid=5957508060"
# }
# res = requests.get(url,headers=headers)
# print(res.text)
