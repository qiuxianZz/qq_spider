# from xlwt import *
# #需要xlwt库的支持
# #import xlwt
# file = Workbook(encoding = 'utf-8')
# #指定file以utf-8的格式打开
# table = file.add_sheet('data')
# #指定打开的文件名
#
# data = {
#     "1":["张三",150,120,100],
#     "2":["李四",90,99,95],
#     "3":["王五",60,66,68],
#     "4":[63439, '1E1914048496E1CF65AAA6F791E2F22F', 'wxf52daf77fffdcc13', 0, 1, 'ProWine', 'gh_bf94a678e29f', 'International Trade Fair for Wines and Spirits   国际葡萄酒和烈酒贸易展览会', '会展服务', '生活服务', 0, '杜塞尔多夫展览(上海)有限公司', None, None, '91310115692911015J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM4IIBk2b7icgicweGts5k1Z6swlDvDCdC46ibW26PncSX4gA/0', 'https://prowine.winewin9.com', '2019, 11, 1, 12, 30, 57', None, None, '2019, 10, 7, 5, 22, 16', '2019, 11, 7, 0, 0, 57', None, None, 0, None]
#
#     # "5":[63439, '1E1914048496E1CF65AAA6F791E2F22F', 'wxf52daf77fffdcc13', 0, 1, 'ProWine', 'gh_bf94a678e29f', 'International Trade Fair for Wines and Spirits   国际葡萄酒和烈酒贸易展览会', '会展服务', '生活服务', 0, '杜塞尔多夫展览(上海)有限公司', None, None, '91310115692911015J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM4IIBk2b7icgicweGts5k1Z6swlDvDCdC46ibW26PncSX4gA/0', 'https://prowine.winewin9.com', (2019, 11, 1, 12, 30, 57), None, None, (2019, 10, 7, 5, 22, 16), (2019, 11, 7, 0, 0, 57), None, None, 0, None]
#
# }
# #字典数据
#
#
#
# ldata = []
# num = [a for a in data]
# #for循环指定取出key值存入num中
# num.sort()
# #字典数据取出后无需，需要先排序
#
# for x in num:
#     #for循环将data字典中的键和值分批的保存在ldata中
#     t = [int(x)]
#     for a in data[x]:
#         t.append(a)
#     ldata.append(t)
#
# for i,p in enumerate(ldata):
#     #将数据写入文件,i是enumerate()函数返回的序号数
#     for j,q in enumerate(p):
#         # print i,j,q
#         table.write(i,j,q)
# file.save('./d.xls')
#
import json

# url = 'https://api.boxmed.ia.vip/bizEvents/60'

import requests

#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; DUK-AL20 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/WIFI Language/zh_CN'
# }


# res = requests.get(url, headers=header)
# print(res.text)
# print(res.status_code)
# con = json.loads(res.text)
# # print(con)
# data = (con['data'])
# print(data)
# for item in data:
#     print(item)

header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
    "referer": "https://servicewechat.com/wx244d19eefdd79491/31/page-frame.html",
    "client-key": "wxmp_red",
    "x-requested-with": "XMLHttpRequest",
    "client-version": "1.2.0",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJveG1lZGlhLnZpcFwvYXV0aG9yaXphdGlvbnNcL2N1cnJlbnQiLCJpYXQiOjE1ODI2MTkzMDcsImV4cCI6MTU4Mjg3NDExNSwibmJmIjoxNTgyODcwNTE1LCJqdGkiOiJWN25yY2MwWWJEdVdKc0p6Iiwic3ViIjozNDM3NiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.SoV-P9P0pWtNIT5ZFd9TLEqhas99ZF9LxyjW-wAnVfE",
    "content-type": "application/json",
    "Content-Length": "2",
}
data = {
}

# data  = {
#     "Server": "nginx",
#     "Content-Type": "application/json",
#     "Connection": "keep-alive",
#     "Cache-Control": "no-cache, private",
#     "Date": "Mon, 02 Mar 2020 02:03:05 GMT",
#     "X-RateLimit-Limit": "60",
#     "X-RateLimit-Remaining": "57",
#     "X-Frame-Options": "SAMEORIGIN",
#     "X-XSS-Protection": "1; mode=block",
#     "X-Content-Type-Options": "nosniff",
#     "Content-Length": "9204",
#
# }


# url = "https://api.boxmedia.vip/bizEvents/9600/attend/YL6m5RgK"
# # url = "https://api.boxmedia.vip/bizEvents/9483/attend/YL6m5RgK HTTP/1.1"
# res = requests.get(url=url, headers=header, data=data)
# print(res.text)


# headers = {
#     "charset": "utf-8",
#     "Accept-Encoding": "gzip",
#     "referer": "https://servicewechat.com/wx244d19eefdd79491/31/page-frame.html",
#     "client-key": "wxmp_red",
#     "x-requested-with": "XMLHttpRequest",
#     "client-version": "1.2.0",
#     "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJveG1lZGlhLnZpcFwvc29jaWFsc1wvd3htcF9yZWRcL3ByZUF1dGhvcml6YXRpb25zIiwiaWF0IjoxNTgzMTE0MTg1LCJleHAiOjE1ODMxMTc3ODUsIm5iZiI6MTU4MzExNDE4NSwianRpIjoicTRVZnkxWkIwa2VEejhGZyIsInN1YiI6MzQzNzYsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.GSR5fOGwdMrnGUBvbcRjQdm1FRMxXrycIlFIl-P1_8s",
#     "content-type": "application/json",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",
#     "Host": "api.boxmedia.vip",
#     "Connection": "Keep-Alive"
#
#
# }
#
# url = "https://api.boxmedia.vip/bizEvents/9600"
url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",

}
res = requests.get(url,headers=headers)
print(res.text)