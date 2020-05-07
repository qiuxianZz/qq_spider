import  requests

# url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzI2MzE2NDczMw==&hid=1&sn=82535620c0eac83006257862b2d9ebd8&scene=18&devicetype=android-22&version=27000d34&lang=zh_CN&nettype=WIFI&ascene=7&session_us=gh_08ed98f9b74c&pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt%2BNs8APNgZhFQLh32CTEGZ&wx_header=1&cid=0&begin=21&count=5&action=appmsg_list&f=json&r=0.024120185543300865&appmsg_token=1057_AGK4TfDqGQkMiz50XN53QxeotirMj9phisDS1A~~'


# url = 'https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&appmsgid=2649738930&idx=1&comment_id=1097406944232570880&offset=0&limit=100&send_time=&uin=777&key=777&pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt%25252BNs8APNgZhFQLh32CTEGZ&wxtoken=777&devicetype=android-22&clientversion=27000d34&__biz=MzI2MzE2NDczMw%3D%3D&appmsg_token=1057_qculFP%252BC8Dl5o2CYJI-O25un5naNVM7aH-_YfyJsm5eenSrKcRwU5-fGaNLslRBnQaEeVRv-UeY90mdk&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/s?__biz=MzI2MzE2NDczMw==&mid=2649738930&idx=1&sn=a0e0b60f984be179d4017a954dc4535e&scene=19&ascene=59&devicetype=android-22&version=27000d34&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AS5m%2F9z%2BLDmVinLqc7zVA2c%3D&pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt%2BNs8APNgZhFQLh32CTEGZ&wx_header=1'
# header = {
#     "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; TAS-AN00 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 MMWEBID/9379 MicroMessenger/7.0.13.1640(0x27000D34) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm32 WeChat/arm32",
#      "Cookie":"wxtokenkey=777;wap_sid2=CPzrpKQCElxXamVubmVLTC1NdHZWTk9yOHdkR2NYTXhrbFk0NWlEN1UzRFZlMXlBTEhMZUV1LXRGM0d4WUZCWWVfb196YVRqZUh6UEdZZ3FubHZHa2JqYVg0SkZnaUVFQUFBfjC3ifT0BTgNQAE=;pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt+Ns8APNgZhFQLh32CTEGZ;lang=zh_CN;version=27000d34;devicetype=android-22;wxuin=612972028;rewardsn="
# }
# data={}
# res = requests.get(url,headers=header)
# print(res.text)


# 阅读数 在看数 url = 'https://mp.weixin.qq.com/mp/getappmsgext?f=json&mock=&fasttmplajax=1&f=json&uin=&key=&pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt%25252BNs8APNgZhFQLh32CTEGZ&wxtoken=&devicetype=android-22&clientversion=27000d34&__biz=MzI2MzE2NDczMw%3D%3D&enterid=1587349940&appmsg_token=&x5=0&f=json&wx_header=1&pass_ticket=TOkXrHt7eHuTWsHxICW8TBF9Nt1H2jreRENIPM03Dyt+Ns8APNgZhFQLh32CTEGZ'


# url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={}&count=5&fakeid={}==&type=9&query=&token=817780164&lang=zh_CN&f=json&ajax=1'
url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=10&count=5&fakeid=MzI2MzE2NDczMw==&type=9&query=&token=1661245175&lang=zh_CN&f=json&ajax=1'

headers = {
    "Host": "mp.weixin.qq.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "*/*",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=817780164&lang=zh_CN",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "cookie": "noticeLoginFlag=1; pgv_pvi=7875631104; RK=VS16IL7/PO; cuid=1055402300; tvfe_boss_uuid=6047678a352d0121; mobileUV=1_1633e2246de_7a338; ue_uid=053e6c36ef5c2eadb67399032d60a7ac; ue_ts=1526528756; ue_uk=0ea230a206defcedd9d3e80f8e5a08f2; ue_skey=14ba8d16995489dc83800820780668be; pac_uid=1_843694650; ua_id=g3q0DguOheBnW1zJAAAAAMs-vwwwcUqQEHMw75n9ONU=; mm_lang=zh_CN; ptcz=572f224da02ff9a0d4709e307150f88c99c5bf3cd8c29264db904839c8cba2d8; pgv_pvid=609154372; XWINDEXGREY=0; 3g_guest_id=-8616001766456033280; eas_sid=L1O5F5X956O2p860v2b723J3U0; ied_qq=o0843694650; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b408c21a6557-0631dc27d0406f-b781636-2073600-16b408c21a7d83%22%2C%22%24device_id%22%3A%2216b408c21a6557-0631dc27d0406f-b781636-2073600-16b408c21a7d83%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _ga=GA1.2.19196003.1574669531; ptui_loginuin=498801451; psrf_qqrefresh_token=54A07D9E2F8950428C24F70BE72739D3; psrf_access_token_expiresAt=1591755535; psrf_qqunionid=D13A3ECD2AA34A6CDAEFEEF16CBECE39; psrf_qqopenid=6257690786C767495DB4C60B49164C71; psrf_qqaccess_token=5DA4C31F38E045ED385B302C1B04A6D8; o_cookie=498801451; noticeLoginFlag=1; ts_uid=2652097440; _gid=GA1.2.1531946643.1587346221; pgv_si=s7413900288; _qpsvr_localtk=0.5450834873255102; uin=o0498801451; skey=@BmjEqK4Z6; cert=8LZvLddHEdcXAohXwTg0r5VFNFu6MTcE; uuid=4f355e1202ab6675302d040d71b3799e; bizuin=3264625595; ticket=55cd303c698d9d40a031d74dac8639a9705e7e7e; ticket_id=gh_9e0178445111; rand_info=CAESIKWHXTViJMJuQr4mSej0HH0p/OcjaJpYLw6mQAzkFTfD; slave_bizuin=3264625595; data_bizuin=3264625595; data_ticket=/eZSrenQnZ2lp30P28PRelNKiYauDAe9vFxyNC0mrpyuOluF9X/5Q9DRfADTpfIV; slave_sid=SVd6XzNLUThPYkVsOVpTdHFrNTh2dzBoUk5zWF93QUlCSTlFTzdqQ1BJdjljMGhjMlpMa3ZsMXMybjFTb0ZHbmZtUE9XZFNQY2NYZFg0ODlWN1IwaEpNV1ozQ085N0pMNFpMSVdpeDZZUXhtVGhNcTJEamhiRTkyV05YaUNuWHpEaXhzVkhhdkMzeW1PVzZK; slave_user=gh_9e0178445111; xid=006422cb029d6e7e103e973e3599f496; openid2ticket_ouzuWwp8doihp9B3dk4U0PdK8rQw=sDm/P+o9MuHM5rO8cYRNm9uKTsXatdXKMuhKdoZrcO4=; sig_login=h01fd8ed9defbc3271d4d6d08bbfcbbf70dfc5a7d79493f4b36c32fe131c1367e33ed9caf9bad16c7c9"

}

res = requests.get(url,headers=headers)
print(res.text)
