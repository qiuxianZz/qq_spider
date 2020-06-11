import json

import requests

url = 'https://mpapi.baixing.com/v1.3.6/'
headers = {
'Host': 'mpapi.baixing.com',
'Connection': 'keep-alive',
'Content-Length': '39',
'BAIXING-SESSION': '$2y$10$2P7KX6LgBnHL687BQxYKGe/wFtdaDIhR41ZVU7cf.QnTt8PQZuxAK',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
'content-type': 'application/json',
'env_version': '7.0.4',
'model': 'microsoft',
'network_type': 'wifi',
'os': 'win10',
'source': '1007',
'source_params': 'ald_share_src=f3a2cdf553731dd0a75b52a099c00420&id=2126893272',
'source_path': 'pages/BXViewAd/BXViewAd',
'template_version': 'Ver1.3.6',
'track_id': '1590824923412-8776768-0249bccf3cb633-16419474',
'udid': 'b9b2a2fb-ee6f-4fcd-81b2-8da6732d64ff',
'Referer': 'https://servicewechat.com/wxd9808e2433a403ab/42/page-frame.html',
'Accept-Encoding': 'gzip, deflate, br'
}
data = {"viewAd.getVad":{"adId":"2179205282"}}
data = {"listing.getAds":{"adId":"2179205282"}}
#
res = requests.post(url,headers=headers,data=json.dumps(data))
# print(res.text)



url = 'https://mpapi.baixing.com/v1.3.6/'
# Host: mpapi.baixing.com
# Connection: keep-alive
# Content-Length: 87
# BAIXING-SESSION: $2y$10$2P7KX6LgBnHL687BQxYKGe/wFtdaDIhR41ZVU7cf.QnTt8PQZuxAK
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat
# content-type: application/json
# env_version: 7.0.4
# model: microsoft
# network_type: wifi
# os: win10
# source: 1007
# source_params: ald_share_src=f3a2cdf553731dd0a75b52a099c00420&id=2126893272
# source_path: pages/BXViewAd/BXViewAd
# template_version: Ver1.3.6
# track_id: 1590824923412-8776768-0249bccf3cb633-16419474
# udid: b9b2a2fb-ee6f-4fcd-81b2-8da6732d64ff
# Referer: https://servicewechat.com/wxd9808e2433a403ab/42/page-frame.html
# Accept-Encoding: gzip, deflate, br

# data = {"listing.getAds":{"areaId":"m35","categoryId":"fuwu","page":963321}}
data = {"listing.getAds":{"areaId":"m200","page":"1000","categoryId":"fuwu"}}
print(json.dumps(data))
res = requests.post(url,headers=headers,data=json.dumps(data))
print(res.text)

url = 'https://mpapi.baixing.com/v1.3.6/'


data = {"category.getFuwuMenu":{}}
res = requests.post(url,headers=headers,data=json.dumps(data))
# print(res.text)
