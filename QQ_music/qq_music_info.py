import datetime
import time

import requests
import json

current_time = datetime.date.today()  # 当前时间
currentYear = datetime.datetime.now().year  # 当前时间年份
week_num = int(time.strftime("%W"))  # 当前时间第几周
print(week_num)
parameter_1 = str(currentYear) + '_' + str((week_num + 1))
print(parameter_1)
parameter = str(currentYear) + '_' + str((week_num))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


def getdetails(mid, id):
    """
    获取歌曲详情
    :param mid: 歌曲的mid
    :param id: 歌曲的id
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI9336468939437326&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22songinfo%22%3A%7B%22method%22%3A%22get_song_detail_yqq%22%2C%22param%22%3A%7B%22song_type%22%3A0%2C%22song_mid%22%3A%22' + mid + '%22%2C%22song_id%22%3A{}%7D%2C%22module%22%3A%22music.pf_song_detail_svr%22%7D%7D'.format(
        id)
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)
    data = data["songinfo"]["data"]
    track_info = data["track_info"]
    info = data["info"]
    song_name = track_info["name"]
    singer_name = track_info["singer"][0]["name"]
    album_name = track_info["album"]["name"]
    lan = info["lan"]["content"][0]["value"]
    company = info["company"]["content"][0]["value"]
    pub_time = info["pub_time"]["content"][0]["value"]
    comments = getcomment(id)
    print(song_name, singer_name, album_name, lan, company, pub_time, comments)


def getcomment(id):
    """
    获取评论数
    :param id: 歌曲的id
    :return:评论总数
    """
    # url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'.format(id)
    # url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid={}&reqtype=2&biztype=1&topid={}&cmd=4&needmusiccrit=0&pagenum=0&pagesize=0&lasthotcommentid=&domain=qq.com".format(id,id)
    url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid={}&reqtype=1&biztype=1&topid={}&cmd=4&needmusiccrit=0&pagenum=0&pagesize=0&lasthotcommentid=&domain=qq.com".format(id,id)
    print(url)
    res = requests.get(url, headers=headers)
    print(res.text)
    # data = json.loads(res.text)
    # commenttotal = data["comment"]["commenttotal"]
    # return commenttotal

getcomment("248470640")


def getinfo(i, n, t):
    """
    获取榜单歌曲
    :param i:榜单类型
    :param n: 榜单歌曲数量
    :param t: 当天时间
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=571650490&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":%s,"offset":0,"num":%s,"period":"%s"}},"comm":{"ct":24,"cv":0}}' % (
        i, n, str(t))
    # url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8366788915686378&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A{}%2C%22offset%22%3A0%2C%22num%22%3A{}%2C%22period%22%3A%22{}%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'.format(i,n,t)
    print(url)
    res = requests.get(url, headers=headers)
    print(res.text)
    data = json.loads(res.text)
    songInfoList = data["detail"]["data"]["songInfoList"]

    for item in songInfoList:
        mid = item["mid"]
        id = item["id"]
        getdetails(mid, id)

        # print(rank,rankType,rankValue,songId,vid,albumMid,title,singerName,singerMid,songType,uuidCnt)
    # return data

# getinfo(62, 100, current_time)  # 飙升榜时间 100 每天更新
# getinfo(26, 300, parameter)  # 热歌榜时间 300 每周四更新


# getinfo(62, 100,current_time)# 飙升榜时间 100 每天更新
# getinfo(26, 300, parameter)  # 热歌榜时间 300 每周四更新
# getinfo(27, 100, '2020-03-13')# 新歌歌榜时间 100 新歌日榜
# getinfo(4, 100, '2020-03-13')# 流行指数榜时间 100 每天更新
# getinfo(67, 100, '2020-03-13')# 听歌识曲榜 100 每天更新
# getinfo(5, 100, '2020_11')# 内地榜 100 每周四更新
# getinfo(61, 100, '2020_11')# 台湾榜 100 每周四更新
# getinfo(3, 100, '2020_11')# 欧美榜 100 每周四更新
# getinfo(16, 100, '2020_11')# 韩国榜 100 每周四更新
# getinfo(17, 100, '2020_11')# 日本榜 100 每周四更新
# getinfo(60, 100, '2020_11')# 抖音排行榜 100 每周四更新
# getinfo(28, 100, '2020_11')# 网络歌曲榜 100 每周四更新
# getinfo(57, 50, '2020_11')# 电音榜 50 每周四更新
# getinfo(58, 50, '2020_11')# 说唱榜 50 每周四更新
# getinfo(66, 50, '2020_11')# AGG新歌榜 100 每周四更新
# getinfo(65, 100, '2020_11')# 国风热歌榜 100 每周四更新
# getinfo(64, 100, '2020_11')# 综艺新歌榜 100 每周四更新
# getinfo(29, 100, '2020_11')# 影视金曲榜 100 每周四更新
# getinfo(70, 100, '2020_11')# 达人音乐榜 100 每周四更新
# getinfo(52, 100, '2020_11')# 腾讯音乐人 100 每周三更新
# getinfo(36, 100, '2020_11')# 全名k歌 50 每周四更新
# getinfo(108, 100, '2020_10')# 美国公告榜 100 每周二更新
# getinfo(123, 100, '2020_10')# 美国iTunes榜 100 每周周日更新
# getinfo(129, 100, '2020_10')# 韩国melon榜 100 每周一更新
# getinfo(107, 40, '2020_10')# 英国uk榜 40 每周周五更新
# getinfo(105, 20, '2020_10')# 日本公信榜 20 每周三更新
# getinfo(126, 100, '2020_10')# 本地热歌 100 每周四更新
# getinfo(114, 20, '2020_10')# 香港商台榜 20 每周六更新
# getinfo(127, 50, '2020_10')# 台湾kkbox榜 50 每周五更新



