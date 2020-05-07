import time

import requests
import execjs
import json

'''
https://www.toutiao.com/ch/news_hot/
'''

def get_cpas():
    with open('ascp.js','r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a')

def get_sign():
    with open('sign.js','r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a')

url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time={}&max_behot_time_tmp={}&tadrequire=true&as={}&cp={}&_signature={}'
# url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A195CE1023318FE&cp=5E0331182F1EBE1&_signature=mdVRNAAgEB1r-mNz8uoVzJnVUCAAMfi'
dic = get_cpas()
as1 = dic['as']
cp = dic['cp']
_signature = get_sign()
url = url.format(round(time.time()) * 1000,round(time.time()) * 1000,as1,cp,_signature)
print(as1,cp,_signature)
print(url)

header = {
    "Connection":"keep-alive",
    "Pragma":"no-cache",
    "Cache-Control":"no-cache",
    "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded",
    "Referer":"https://www.toutiao.com/ch/news_hot/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
}

res = requests.get(url,headers=header)
print(res.text)
# json_res = json.loads(res.text)
# for item in json_res['data']:
#     print(item)

print(round(time.time()) * 1000)
# 1577261262657
# 1577261992000