import datetime
import random
import time

import requests





url = 'https://is-lq.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid=3200725091&stream_api_version=47&count=20&offset=0&channel=lite2_tengxun&aid=35&app_name=news_article_lite&version_code=728&device_platform=android&device_type=MI+6&os_version=5.1.1'

header = {
    'Accept': 'image/webp,image/*;q=0.8',
    'User-Agent': 'News/6.9.8.36 CFNetwork/975.0.3 Darwin/18.2.0',
    # "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 6 Build/NMF26X) NewsArticle/7.2.8 cronet/TTNetVersion:4df3ca9d 2019-11-25",
    'Accept-Language': 'zh-cn',


}
proxies = {"http": "http://116.16.179.170:41301"}
res = requests.get(url, headers=header,)
print(res.status_code)
print(res.json())

#
# import time
#
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# file_handle = open('toutiao.txt', mode='w')
# file_handle.write("3242342")
# file_handle.write('\r\n')

# with open('toutiao.txt','w') as f:    #设置文件对象
#     f.write("qwerqwerqwe")


# file_handle=open('tt.txt',mode='a')
# file_handle.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# file_handle.write('\r\n')
# file_handle.close()

