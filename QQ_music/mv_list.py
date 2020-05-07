# mv 榜单
# area_type 总榜 0,内地榜 1,日本榜 5,欧美榜 3,港台榜 2,韩国榜 4
import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


def parse_mv(data):
    """
    解析mv
    :param data:
    :return:
    """
    print(data)
    data = json.loads(data)
    rank_list = data["request"]["data"]["rank_list"]
    for item in rank_list:
        video_info = item["video_info"]
        cover_pic = video_info["cover_pic"]
        mv_name = video_info["name"]
        pubdate = video_info["pubdate"]
        vid = video_info["vid"]
        comments = getmvcomment(vid)
        singer_name = video_info["singers"][0]["name"]
        print(cover_pic,mv_name,pubdate,vid,comments,singer_name)


def getmvcomment(vid):
    """
    获取mv的评论数
    :param vid: 每首mv的vid
    :return:
    """
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=5&topid={}&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'.format(
        vid)
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)
    commenttotal = data["comment"]["commenttotal"]
    return commenttotal


def getmv(i):
    """
    获取mv榜单
    :param i:MV类型id
    :return:
    """
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6465917711479467&g_tk=5381&loginUin=498801451&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"comm":{"ct":24,"cv":0},"request":{"method":"get_video_rank_list","param":{"rank_type":0,"area_type":%d,"required":["vid","name","singers","cover_pic","pubdate"]},"module":"video.VideoRankServer"}}' % i
    res = requests.get(url, headers=headers)
    parse_mv(res.text)


getmv(1)
