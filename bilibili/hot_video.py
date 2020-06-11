# 作品相关
import requests

# url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid=883205933'  # 基本指数
# url = 'https://www.bilibili.com/video/BV18e411W7Q4'  # 发布时间一级二级标签 tags 在源码正则匹配出
# 用户相关
#
# url = 'https://api.bilibili.com/x/relation/stat?vmid=27201651&jsonp=jsonp&callback=__jp3'  # 粉丝and关注
# url = 'https://api.bilibili.com/x/relation/followings?vmid=27201651&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp5'  # 粉丝and关注
# url = 'https://api.bilibili.com/x/space/upstat?mid=1111111111111&jsonp=jsonp&callback=__jp4' # 获赞and播放
# url= 'https://api.bilibili.com/x/space/acc/info?mid=383665157&jsonp=jsonp' # 用.户基本信息
url = 'https://elec.bilibili.com/api/query.rank.do?mid=536029603&type=jsonp&jsonp=jsonp&callback=__jp8'  # 充电模块数据

# url = 'https://api.bilibili.com/x/space/arc/search?mid=2733216&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
# url = 'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=2733216&page_num=0&page_size=30&biz=all'
# url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=1'  # 动画模块

headers = {
    # 'cookie': "fts=1512536357; buvid3=98F07B63-F162-4266-B52E-3A2E59B3DD9547209infoc; pgv_pvi=6066786304; LIVE_BUVID=2b1b2a628039177645c7dbc2be795290; LIVE_BUVID__ckMd5=bdade4501f3ce28c; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(u)l~lmmJk)0J'ullYY|kk||; sid=4n3dlq79; _uuid=965BDB1A-5C7B-8B9C-9706-DED45CAA600C12128infoc; CURRENT_QUALITY=80; im_notify_type_430343910=0; DedeUserID=430343910; DedeUserID__ckMd5=24cad682056a3e26; SESSDATA=7b3bae44%2C1605419935%2C68a41*51; bili_jct=a911ca6cef406f45d7bf55ffe125390d; bp_t_offset_430343910=386857346554106024; bp_video_offset_430343910=386857346554106024; PVID=2; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
    'referer': 'https://space.bilibili.com/',
    # 'referer': 'https://space.bilibili.com/299732210?spm_id_from=333.851.b_62696c695f7265706f72745f72656164.23',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

for i in range(10000):
    proxies = {'http': "http://171.112.170.38:26227"}
    res = requests.get(url, headers=headers, )
    print(res.text)

# 扩号


url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=1'  # 动画模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=168'  # 国产原创相关
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=3'  # 音乐模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=129'  # 舞蹈模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=4'  # 游戏模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=36'  # 科技模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=188'  # 数码模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=160'  # 生活模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=119'  # 鬼畜模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=155'  # 时尚模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=202'  # 资讯模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=5'  # 娱乐模块
url = 'https://api.bilibili.com/x/article/recommends?ps=8'  # 专栏模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=23'  # 电影模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=11'  # 电视剧模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=181'  # 影视模块
url = 'https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=177'  # 模块
