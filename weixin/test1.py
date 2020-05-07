import random
import re
import time
from bs4 import BeautifulSoup

import requests
import json

# MjM5NjAxOTU4MA MzI2MzE2NDczMw MzIxNTAzNzU0Ng
biz = 'MzI2MzE2NDczMw'

url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={}&count=5&fakeid={}==&type=9&query=&token=817780164&lang=zh_CN&f=json&ajax=1'

headers = {
    "Host": "mp.weixin.qq.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "*/*",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=817780164&lang=zh_CN",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "rewardsn=; wxtokenkey=777; pgv_info=ssid=s9994475674; pgv_pvid=3115944578; pac_uid=0_5e857917c9954; wxuin=1966586115; devicetype=iPhoneiOS13.3.1; version=17000c27; lang=zh_CN; pass_ticket=16n2kIXK3NX/RZHaIOIt7fe29o0g1JPs9WxUiLoQ430/lp4hbYPytzpCdSNPah; wap_sid2=CIPy3qkHElxsbG1jblYtdG5uMmhjbmg5SkJ2SWlTZjIzc0NjbTQtU3RfaUVraFVOSUtFcTlxWkxjRmN2Um40bHllLVVTVUI3VTV1YlpXdnNVOVF2S3J3SkJ5SW5UQjhFQUFBfjC/s5r0BTgNQJVO"
}

proxies = {'http': "http://115.216.77.107:27546"}


# p = requests.get('http://icanhazip.com', headers=headers, proxies=proxies)
# print(p.status_code)

def getDetails(biz, mid, sn):
    url = 'https://mp.weixin.qq.com/mp/getappmsgext?f=json&mock=&uin=MTk2NjU4NjExNQ%253D%253D&key={}&pass_ticket=4y8tGt7nk6a3pYuu8Q9XD%25252FJotHyThug5pMo7VG7YxPWjXkCNkiCPMywo9K8KLJAL&wxtoken=777&devicetype=Windows%26nbsp%3B10&clientversion=62080079&__biz={}%3D%3D&appmsg_token=1054_stDP5q4TdYnkB9u24Vbc5LU1cNsUaMFSTXPP7ZPH6eN347Pfvzf0y0p_C65QUxtCyQ6GJbLEbU7V5UQA&x5=0&f=json'.format(
        '861420a46a8ac7f7748289c82aeda527e79fdf73ad8542d7aa0211c666eb92e99bfeda0387be8d17759c74ffd6fdb6ee57a06e94b2be7e26c1278ddb565539804b23c2c392c065f105e8e0daac4ab967',
        biz)
    # url = 'https://mp/getappmsgext?f=json&mock=&fasttmplajax=1&f=json&uin=&key=&pass_ticket=1b6MifRiv73Q%25252Fnzn20JRw3Im1pfT4y%25252B6OEd6Gwpz3vzErUyoxTNRJJoR9hbo0vXK&wxtoken=&devicetype=android-22&clientversion=27000634&__biz=MzI2MzE2NDczMw%3D%3D&appmsg_token=&x5=0&f=json&wx_header=1&pass_ticket=1b6MifRiv73Q/nzn20JRw3Im1pfT4y+6OEd6Gwpz3vzErUyoxTNRJJoR9hbo0vXK'
    data = 'r=0.8858750940048443&__biz={}%3D%3D&appmsg_type=9&mid={}&sn={}&idx=1&scene=38&title=%25E7%25BD%2597%25E6%25B0%25B8%25E6%25B5%25A9%25E7%259C%259F%25E8%25B4%25B5%25EF%25BC%258C%25E4%25BD%2586%25E6%258A%2596%25E9%259F%25B3%25E4%25B8%258D%25E8%25B4%25B5&ct=1585714363&abtest_cookie=&devicetype=Windows%2010&version=62080079&is_need_ticket=0&is_need_ad=0&comment_id=1277116789050277888&is_need_reward=0&both_ad=0&reward_uin_count=0&send_time=&msg_daily_idx=1&is_original=0&is_only_read=1&req_id=0113KfAOkJNsrUlvMR9WEKHz&pass_ticket=4y8tGt7nk6a3pYuu8Q9XD%25252FJotHyThug5pMo7VG7YxPWjXkCNkiCPMywo9K8KLJAL&is_temp_url=0&item_show_type=0&tmp_version=1&more_read_type=0&appmsg_like_type=2&related_video_sn=&vid=&is_pay_subscribe=0&pay_subscribe_uin_count=0&has_red_packet_cover=0'.format(
        biz, mid, sn)
    res = requests.post(url, data=data, headers=headers)
    print(res.text)
    # data = json.loads(res.text)
    # appmsgstat = data["appmsgstat"]
    # like_num = appmsgstat["like_num"]
    # read_num = appmsgstat["read_num"]
    # print(like_num)
    # print(read_num)
    #


def getContent(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    for l in soup.select('#js_content'):
        print(l.get_text())


def getlist(num, biz):
    res = requests.get(url.format(num, biz), headers=headers, proxies=proxies)
    data = json.loads(res.text)
    print(res.text)
    app_msg_list = data["app_msg_list"]
    if app_msg_list == []:
        return 'end'
    for item in app_msg_list:
        link = item["link"]
        patterns = re.compile('&sn=(.*?)&chksm', re.S)
        name = patterns.findall(link)
        sn = name[0]
        mid = item["appmsgid"]
        getDetails(biz=biz, mid=mid, sn=sn)
        getContent(link)


for item in range(0, 175, 5):
    res = getlist(item,biz)
    if res == 'end':
        break
    time.sleep(10)


# url = 'https://mp.weixin.qq.com/mp/getappmsgext?f=json&mock=&fasttmplajax=1&f=json&uin=&key=&pass_ticket=1b6MifRiv73Q%25252Fnzn20JRw3Im1pfT4y%25252B6OEd6Gwpz3vzErUyoxTNRJJoR9hbo0vXK&wxtoken=&devicetype=android-22&clientversion=27000634&__biz=MzI2MzE2NDczMw%3D%3D&appmsg_token=&x5=0&f=json&wx_header=1&pass_ticket=1b6MifRiv73Q/nzn20JRw3Im1pfT4y+6OEd6Gwpz3vzErUyoxTNRJJoR9hbo0vXK'
#
# headers = {
#     "Cookie": "rewardsn=; devicetype=android-22; version=27000634; lang=zh_CN",
#     "X-WECHAT-KEY": "90d8abf12e099198f0c9e66cbee0afedbfe7b240098d118cfa110ab49bd04e0ea88b046826e93988c3a80fa8ecff92a518adb168586c23ffed1c3521ac9baf82f2475dacf73a0f919166318aecd0dd7e",
#     "X-WECHAT-UIN": "NjEyOTcyMDI4",
#     "User-agent": "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R11 Plus Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 MMWEBID/9379 MicroMessenger/7.0.6.1460(0x27000634) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.6.1460(0x27000634) Process/toolsmp NetType/WIFI Language/zh_CN",
#     "Host": "mp.weixin.qq.com",
#     "Connection": "Keep-Alive",
#     "Accept-Encoding": "gzip",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Content-Length": "800",
#
# }
#
# data = 'r=0.8134008270297557&__biz=MzI2MzE2NDczMw==&appmsg_type=9&mid=2649740017&sn=5b2fca6525982b834ab722af7e36f866&idx=1&scene=126&title=%E7%BD%97%E6%B0%B8%E6%B5%A9%E7%9C%9F%E8%B4%B5%EF%BC%8C%E4%BD%86%E6%8A%96%E9%9F%B3%E4%B8%8D%E8%B4%B5&ct=1585714363&abtest_cookie=&devicetype=android-22&version=27000634&is_need_ticket=0&is_need_ad=0&comment_id=1277116789050277888&is_need_reward=0&both_ad=0&reward_uin_count=0&send_time=&msg_daily_idx=1&is_original=0&is_only_read=1&req_id=&pass_ticket=1b6MifRiv73Q%252Fnzn20JRw3Im1pfT4y%252B6OEd6Gwpz3vzErUyoxTNRJJoR9hbo0vXK&is_temp_url=0&item_show_type=0&tmp_version=1&more_read_type=0&appmsg_like_type=2&related_video_sn=&vid=&is_pay_subscribe=0&pay_subscribe_uin_count=0&has_red_packet_cover=0'
# res = requests.post(url, data=data, headers=headers)
# print(res.text)


