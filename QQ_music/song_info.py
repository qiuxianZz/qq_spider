
import requests
import json
import time

# 欧美榜 3,流行指数榜 4,内地榜 5,港台榜 6,韩国榜 16,日本榜 17,专辑畅销榜 23,热歌榜 26,新歌榜 27,网络歌曲榜28,
# 影视金曲榜 29,人气榜 34,K歌金曲榜 36,腾讯音乐人原创榜 52,电音榜 57,说唱榜 58,香港地区榜 59,抖音排行榜 60,
# 台湾地区榜 61,飙升榜 62,综艺新歌榜 64,国风热歌榜 65,ACG新歌榜 66,听歌识曲榜 67,达人音乐榜 70,
# 台湾Hito中文榜 103,日本公信榜 105,韩国Mnet榜 106,英国UK榜 107,美国公告牌榜 108,香港电台榜 113,香港商台榜 114,
# 美国公告牌榜 121,美国公告牌榜 122,美国iTunes榜 123,JOOX本地热播榜 126,台湾KKBOX榜 127 YouTube音乐排行榜 128,
# 韩国Melon榜 129


# 飙升榜规则：更新时间：每天更新 歌曲数量：100首
# 热歌榜规则:更新时间：每周四更新 排名数量：300首
# 新歌榜规则：每天更新：100首
# 流行指数榜规则：更新时间：每天更新 歌曲数量：100首


t = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# 优化格式化化版本
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))



type_list = [3,4,5,6,16,17,23,26,27,28,29,34,36,52,57,58,59,60,61,62,64,65,66,67,70,103,105,106,107,108,113,114,123,126,127,128,129]

i = 23
n = 100
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
def getinfo(i,n,t):
    """
    获取榜单歌曲
    :param i:榜单类型
    :param n: 榜单歌曲数量
    :param t: 当天时间
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI69200144588595&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":%s,"offset":0,"num":%s,"period":"%s"}},"comm":{"ct":24,"cv":0}}'% (i,n,str(t))
    print(url)
    # url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI3844255468162199&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":34,"offset":0,"num":20,"period":"2020"}},"comm":{"ct":24,"cv":0}}'
    res = requests.get(url,headers=headers)
    print(res.text)
    data = json.loads(res.text)
    return data



getinfo(62,20,t)
# for item in type_list:
#     getinfo(item,50)


# getinfo()

mid = '000rpN3i1m2rmS'
id = 255402348

def getdetails(mid,id):
    """
    获取歌曲详情
    :param mid: 歌曲的mid
    :param id: 歌曲的id
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI9336468939437326&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22songinfo%22%3A%7B%22method%22%3A%22get_song_detail_yqq%22%2C%22param%22%3A%7B%22song_type%22%3A0%2C%22song_mid%22%3A%22'+mid+'%22%2C%22song_id%22%3A{}%7D%2C%22module%22%3A%22music.pf_song_detail_svr%22%7D%7D'.format(id)
    res = requests.get(url,headers=headers)
    print(res.text)
    # data = json.loads(res.text)
# getdetails()



def getcomment(id):
    """
    获取评论数
    :param id: 歌曲的id
    :return:
    """
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'.format(id                                                                                                                                                                                                                                                                                                                                )
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    print(data)

# getcomment(255380547)


# //y.gtimg.cn/music/photo_new/T002R300x300M000000hrBlD2EWvrv.jpg?max_age=2592000 歌曲图片url


# mv 榜单
# area_type 总榜 0,内地榜 1,日本榜 5,欧美榜 3,港台榜 2,韩国榜 4

def getmv(i):
    """
    获取mv榜单
    :param i:MV类型id
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6465917711479467&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"comm":{"ct":24,"cv":0},"request":{"method":"get_video_rank_list","param":{"rank_type":0,"area_type":%d,"required":["vid","name","singers","cover_pic","pubdate"]},"module":"video.VideoRankServer"}}'% i
    res = requests.get(url,headers=headers)
    print(res.text)



# getmv(0)


def  getmvcomment(vid):
    """
    获取mv的评论数
    :param vid: 每首mv的vid
    :return:
    """
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=5&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'.format(vid)
    res = requests.get(url,headers=headers)
    print(res.text)

# getmvcomment("u00336fqv1a")

# 人气 日榜
url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=1&daystr=0&_=1584001744456'
# 人气 周榜
url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=2&weeklist=1&year=2020&week=11&_=1584001693045'
# 人气 年榜
url= 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=3&year=2020&_=1584001817866'
# 人气 总榜
url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=0&weeklist=0&year=2020&week=11&daystr=0&_=1584002135364'

def getpopularity():
    url = 'https://c.y.qq.com/rsc/fcgi-bin/fcg_global_gift_rank_list.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&reqtype=1&daystr=0&_=1584001744456'
    res = requests.get(url,headers=headers)
    print(res.text)
# getpopularity()



# 数字专辑畅销榜
# 日榜
url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=day_sale_toplist&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584002531680'
# 周榜
url= 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=week_sale_toplist&week=202009&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584003033113'
# 年榜
url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=year_sale_toplist&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584002591395'
# 总榜
url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?g_tk=571650490&uin=498801451&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&cmd=sales_album&week=&year=2020&weeklist=1&yearlist=1&sin=0&ein=19&_=1584002645232'

# res = requests.get(url,headers=headers)
# print(res.text)

# 专辑详情url

def get_album_details(mid):
    """
    获取专辑信息详情数据
    :param mid:album_id
    :return:
    """
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?cmd=get_album_buy_page&albumid=10658260&p=0.36231180386133865&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    url = 'https://c.y.qq.com/v8/fcg-bin/musicmall.fcg?cmd=get_album_buy_page&albumid=7156278&p=0.08771381709891224&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    res = requests.get(url,headers=headers)
    print(res.text)
#  专辑评论数url

def get_album_comment(id):
    """
    获取专辑评论数
    :param id: 专辑id album_id
    :return:
    """
    url= 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=1&biztype=2&topid=10658260&cmd=4&needmusiccrit=0&pagenum=0&pagesize=0&lasthotcommentid=&domain=qq.com'
    url= 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=2&topid=7156278&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'
    res = requests.get(url,headers=headers)
    print(res.text)