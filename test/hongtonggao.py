import json

import requests

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx244d19eefdd79491/31/page-frame.html",
    "client-key": "wxmp_red",
    "x-requested-with": "XMLHttpRequest",
    "client-version": "1.2.0",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJveG1lZGlhLnZpcFwvc29jaWFsc1wvd3htcF9yZWRcL3ByZUF1dGhvcml6YXRpb25zIiwiaWF0IjoxNTgzMTE0MTg1LCJleHAiOjE1ODMxMTc3ODUsIm5iZiI6MTU4MzExNDE4NSwianRpIjoicTRVZnkxWkIwa2VEejhGZyIsInN1YiI6MzQzNzYsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.GSR5fOGwdMrnGUBvbcRjQdm1FRMxXrycIlFIl-P1_8s",
    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
    "Host": "api.boxmedia.vip",
    "Connection": "Keep-Alive"

}

# url = "https://api.boxmedia.vip/bizEvents/1"
# res = requests.get(url=url,headers=headers)
# print(res.text)



#
headers = {
    # "charset": "utf-8",
    # "Accept-Encoding": "gzip",
    "referer": "ttps://servicewechat.com/wx244d19eefdd79491/31/page-frame.html",
    "client-key": "wxmp_red",
    "x-requested-with": "XMLHttpRequest",
    "client-version": "1.2.0",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJveG1lZGlhLnZpcFwvc29jaWFsc1wvd3htcF9yZWRcL3ByZUF1dGhvcml6YXRpb25zIiwiaWF0IjoxNTgzODA1NjQyLCJleHAiOjE1ODM4MDkyNDIsIm5iZiI6MTU4MzgwNTY0MiwianRpIjoiUlBiblVrV1ZuZDNPbjNiTiIsInN1YiI6MzQzNzYsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.iCKKm64PZTeDgxQ6G1HgYaW1gdtkj0NlAW7osC47HJQ",

    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
    # "Content-Length": "2",
    # "Host": "api.boxmedia.vip",
    # "Connection": "Keep-Alive",

}
#
data = {
}

url = "https://api.boxmedia.vip/bizEvents/9639/attend/YL6m5RgK"
res = requests.post(url=url, headers=headers)
print(res.text)

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",

    # "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://www.ingtube.com",
    "Referer": "http://www.ingtube.com/share/index.html?",
    #              "Access-Control-Allow-Credentials": "true",
    #              "Access-Control-Allow-Headers": "Authorization,Content-Type,Origin",
    # "Access-Control-Allow-Methods": "POST",
    # "Access-Control-Allow-Origin": "http://www.ingtube.com",
    # "Connection": "keep-alive",
    # "Content-Length": "5764",
    # # "Content-Type": "application/json; charset=utf-8",
    # "Date": "Tue, 03 Mar 2020 02:12:19 GMT",
}
#
# payloadHeader = {
#     "data": "{campaign_id: 23405}"
# }

#
# data = {
#     "campaign_id": "23405"
# }
#
# payload = {
#     "campaign_id": "23413"
# }
# payload = {"data": {"campaign_id": "23413"}}
#
# res = requests.post("https://api.yingtu.co/app/web/v1/share_campaign_detail",headers=headers,data=json.dumps(payload))
# print(res.text)

# for i in range(22000):
#     payload = {"data":{"campaign_id":i}}
#
#     res = requests.post("https://api.yingtu.co/app/web/v1/share_campaign_detail",headers=headers,data=json.dumps(payload))
#     print(res.text)


# url = "https://api.utrybox.com/product/getBrandInfo"
# url = "https://api.utrybox.com/product/getProductInfo"
# # url = "https://api.utrybox.com/task/search/getTaskSubList"
# # url = "https://api.utrybox.com/task/search/getTaskInfoByTaskId"
#
# headers = {
#     "Host": "api.utrybox.com",
#     "Connection": "keep-alive",
#     "Content-Length": "32",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
#     "accessToken": "8r73s3v2Jl82g1411mQ4T394YC7n950C",
#     "content-type": "application/json",
#     "userAccountId": "SH20200303779588364",
#     "Referer": "https://servicewechat.com/wx913926db9fe68233/65/page-frame.html",
#     "Accept-Encoding": "gzip, deflate, br"
#
# }
# # data = {"taskId": "TK20200228779587003"}
# data =  {"productId":"SH202001166958539026"}
# res = requests.post(url=url, headers = headers, data=json.dumps(data))
# print(res.text)



# POST /app/share/order/v1/apply_count HTTP/1.1
headers =  {
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "238",
"Host": "api.yingtu.co",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.1"
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",


}
data = {
    "app_version": "3.6.0",
    "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
    "sign": "bc60abc14373fe720351a724dcbcde02",
    "source": "android",
    "timestamp": "1583383243",
    "token": "1237195642401464320",
    "user_id": "1234418928222998528"
}
# data = {}
# url = "https://api.yingtu.co/app/share/order/v1/apply_count"
# res =requests.post(url,headers=headers,data=data)
# print(res.text)


# POST /app/share/campaign/v1/get_category HTTP/1.1
# Content-Type: application/json; charset=UTF-8
# Content-Length: 238
# Host: api.yingtu.co
# Connection: Keep-Alive
# Accept-Encoding: gzip
# User-Agent: okhttp/3.12.1
#
#
# {
#     "app_version": "3.6.0",
#     "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
#     "sign": "b7f303f01ef68810353784718d919bd3",
#     "source": "android",
#     "timestamp": 1583387987,
#     "token": "1235423351757873152",
#     "user_id": "1234418928222998528"
# }

headers = {
# POST /app/share/campaign/v1/detail HTTP/1.1
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "269",
"Host": "api.yingtu.co",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.12.1"
}


data = {
    "app_version": "3.6.0",
    "data": {
        "campaign_id": "23438"
    },
    # "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
    # "sign": "821c93a6a83855ed4d308d9f83923fa8",
    # "source": "android",
    # "timestamp": 1583387991,
    "token": "1237187776651202560",
    "user_id": "1234418928222998528"
}

data = {
    # "app_version": "3.6.0",
    "data": {
        "campaign_id": "23583"
    },
    # "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
    # "sign": "4e3a9efb7e5406dd0a47270b8f30481e",
    # "source": "android",
    # "timestamp": 1583402356,
    # "token": "1235505120020533248",

    # "token": "1235423351757873152",
    "token": "1237195642401464320",
    # "token": "1235844508936048640",
    "user_id": "1234418928222998528"
}

# data = { "data":{"campaign_id":"23529"},"token": "1235423351757873152", "user_id": "1234418928222998528" }

res = requests.post("https://api.yingtu.co/app/share/campaign/v1/detail",headers=headers,data=json.dumps(data))
print(res.text)


# POST /app/share/campaign/v1/reward HTTP/1.1

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "278",
    "Host": "api.yingtu.co",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1"
}
data = {
    # "app_version": "3.6.0",
    "data": {
        "type": 1,
        "campaign_id": "23583"
    },
    # "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
    # "sign": "4d80d809961fd4c4340ae78ddd343589",
    # "source": "android",
    # "timestamp": 15833828976,
    "token": "1237195642401464320",
    # "1235844508936048640"
    "user_id": "1234418928222998528"
}


url = "https://api.yingtu.co/app/share/campaign/v1/homepage"
res =requests.post("https://api.yingtu.co/app/share/campaign/v1/reward",headers=headers,data=json.dumps(data))
print(res.text)
# http://www.ingtube.com/share/index.html?campaignId=23518
# http://www.ingtube.com/share/index.html?campaignId=23516
# http://www.ingtube.com/share/index.html?campaignId=23485
# http://www.ingtube.com/share/index.html?campaignId=23480
# http://www.ingtube.com/share/index.html?campaignId=23477
# http://www.ingtube.com/share/index.html?campaignId=23474
# http://www.ingtube.com/share/index.html?campaignId=23466
# http://www.ingtube.com/share/index.html?campaignId=23459
# http://www.ingtube.com/share/index.html?campaignId=23458
# http://www.ingtube.com/share/index.html?campaignId=23539
# http://www.ingtube.com/share/index.html?campaignId=23530http://www.ingtube.com/share/index.html?campaignId=23454

url = "https://api.yingtu.co/app/share/campaign/v1/homepage"
# data = {
#     "app_version": "3.6.0",
#     "data": {
#         "page_id": 1,
#         "timestamp": 1583397799
#     },
#     # "device_id": "I_M_m_b_2062042228145894_da512e0362a3_SM-G925F_samsung",
#     # "sign": "2e0f5ae306f6e6e9fae15a8e4e02d3e0",
#     # "source": "android",
#     # "timestamp": 1583397792,
#     "token": "1235423351757873152",
#     "user_id": "1234418928222998528"
# }
data = {"data": { "page_id": 2, "timestamp": 1583400507 },"token": "1237195642401464320", "user_id": "1234418928222998528"}
res = requests.post(url,data=json.dumps(data))
print(res.text)
# http://www.ingtube.com/share/index.html?campaignId=23518  附带 关键词
# http://www.ingtube.com/share/index.html?campaignId=23477 附带优惠信息s
# http://www.ingtube.com/share/index.html?campaignId=23466 话题
# http://www.ingtube.com/share/index.html?campaignId=23459 关键词
# http://www.ingtube.com/share/index.html?campaignId=23486 发布时间


# POST /man/api?ak=23356390&s=6754480311463694536c623676c235d75a43436b HTTP/1.1
# Content-Type: multipart/form-data; boundary====1583484655397===
# User-Agent: Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/LMY48Z)
# Host: adash.man.aliyuncs.com
# Connection: Keep-Alive
# Accept-Encoding: gzip
# Content-Length: 177
#
# {"t":1583484666187,"ret":"","success":"success"}

# f6e7669fdc518844d6961b5610947cb7eb93df2f
# 9da4156f6f7d4819eb871ac558ea9be0
'申请人数:124;映币/人:;测评内容:null;测评形式:null;品牌话题:null;优惠信息:null;发布时间:null;附带关键词:null;测评指引:["·点击“申请”参与活动","·无发货，无发货，无发货","·请将参与活动的链接提交至此处"];不支持以下地区收货:null'
# http://www.ingtube.com/share/index.html?campaignId=23589
# http://www.ingtube.com/share/index.html?campaignId=23587
# http://www.ingtube.com/share/index.html?campaignId=23583





# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJveG1lZGlhLnZpcFwvYXV0aG9yaXphdGlvbnNcL2N1cnJlbnQiLCJpYXQiOjE1ODM4OTQxNDUsImV4cCI6MTU4Mzg5NzgxNywibmJmIjoxNTgzODk0MjE3LCJqdGkiOiJIeDdHaHFMdWs3QTZnSmdrIiwic3ViIjozNDM3NiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.ZaHZNLUEqYYPGZZWujUVykC0GN8SORt-TWR7_COu0P8"
#
# headers = {
#     "charset": "utf-8",
#     "Accept-Encoding": "gzip",
#     "referer": "https://servicewechat.com/wx244d19eefdd79491/31/page-frame.html",
#     "client-key": "wxmp_red",
#     "x-requested-with": "XMLHttpRequest",
#     "client-version": "1.2.0",
#     # "authorization": "Bearer" + access_token,
#     "authorization": "Bearer "+ access_token,
#     "content-type": "application/json",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
#     # "Content-Length": "2",
#     "Host": "api.boxmedia.vip",
#     "Connection": "Keep-Alive"
# }
#
# url = "https://api.boxmedia.vip/authorizations/current"
# res = requests.put(url=url, headers=headers)
# print(res.text)
# data = json.loads(res.text)
# access_token = data["access_token"]
# print(access_token)
# "https://ic.snssdk.com/api/feed/profile/v1/?category=profile_article&visited_uid=5954781019&stream_api_version=88&count=20&offset=1583919522&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A1%22%7D&iid=106932394204&device_id=56392426097&ac=wifi&mac_address=da%3A51%3A2e%3A03%3A62%3Aa3&channel=baidu_0411&aid=13&app_name=news_article&version_code=755&version_name=7.5.5&device_platform=android&ab_version=821965%2C857804%2C660830%2C1479497%2C1434496%2C1527881%2C662176%2C801968%2C1419041%2C668775%2C1462526%2C1469462%2C1529246%2C1190525%2C1157750%2C1157634%2C1419598%2C1493796%2C1439625%2C1469498%2C668779%2C662099%2C1504927%2C668774%2C1531100%2C1446849&ab_feature=102749%2C94563&ssmix=a&device_type=SM-G925F&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=867653234280434&openudid=2062042228145894&manifest_version_code=7550&resolution=720*1280&dpi=192&update_version_code=75515&_rticket=1583920482340&plugin=18762&tma_jssdk_version=1.46.0.12&rom_version=22&cdid=b7423b30-0d79-44e9-86ac-a799c705da8a"
# "https://ic.snssdk.com/api/feed/profile/v1/?category=profile_article&visited_uid=5954781019&stream_api_version=88&count=20&offset=1583918502&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A1%22%7D&iid=106932394204&device_id=56392426097&ac=wifi&mac_address=da%3A51%3A2e%3A03%3A62%3Aa3&channel=baidu_0411&aid=13&app_name=news_article&version_code=755&version_name=7.5.5&device_platform=android&ab_version=821965%2C857804%2C660830%2C1479497%2C1434496%2C1527881%2C662176%2C801968%2C1419041%2C668775%2C1462526%2C1469462%2C1529246%2C1190525%2C1157750%2C1157634%2C1419598%2C1493796%2C1439625%2C1469498%2C668779%2C662099%2C1504927%2C668774%2C1531100%2C1446849&ab_feature=102749%2C94563&ssmix=a&device_type=SM-G925F&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=867653234280434&openudid=2062042228145894&manifest_version_code=7550&resolution=720*1280&dpi=192&update_version_code=75515&_rticket=1583920484836&plugin=18762&tma_jssdk_version=1.46.0.12&rom_version=22&cdid=b7423b30-0d79-44e9-86ac-a799c705da8a"
