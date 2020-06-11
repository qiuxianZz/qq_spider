import requests
import time
import random
import execjs
import re


url = "https://www.toutiao.com/i6822064864119226883/"
tasessionId = "ppemh4qt51589013543155"
headers1 = {
    "cookie": "__tasessionId=" + tasessionId,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

res = requests.get(url, headers=headers1)
cookies = str(res.cookies)
print(cookies)

nonce = re.findall(r'__ac_nonce=(.*?) for', cookies, re.S)[0]
print(nonce)


res = requests.get("http://127.0.0.1:8080/?id="+nonce)
sign = (res.text)
print(sign)



headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__tasessionId=fpa83ktfq1579496267779; tt_webid=6783884760198759950; s_v_web_id=k5lzaodq_gvGnm79d_agqY_4Uk7_AF1F_xlTOhcR2huJn; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6783884760198759950; csrftoken=86433716ce2242c1e021648752c6ff09',
    'pragma': 'no-cache',
    # 'referer': 'https://www.toutiao.com/',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    # "cookie": "__ac_nonce=" + nonce + "; __ac_signature=" + sign,
    # "cookie": "s_v_web_id=verify_k9za4nho_gCRKFQLD_NWQe_4LWh_8hSR_8dvydi9AgGVf; tt_webid=6824735850564814350; csrftoken=7b2c56668ff8c8b8f38d87eb1f37c42a; ttcid=cb6dd004f15e4b8b8ed8cf04df59799637; SLARDAR_WEB_ID=f5b884fe-7d31-422d-83d8-cb5634025f2b; UM_distinctid=172030d06d371f-0d12b934881caf-b781636-1fa400-172030d06d49ea; CNZZDATA1259612802=1733248640-1589187245-%7C1589187245; _ga=GA1.2.410576440.1589189085; _gid=GA1.2.1744715171.1589189085; __utma=24953151.410576440.1589189085.1589199075.1589199075.1; __utmc=24953151; __utmz=24953151.1589199075.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); passport_csrf_token=5374da05fce701e45cf01afeec3c3047; __tasessionId=owow6dcws1589266212708; __ac_nonce=05eba4728008330abab66; __ac_signature=YIcdGAAgEBAz1KmOW.7V1mCGHAAAD5BuAlN0Y36bHqEoy5wqJ-3U61vKeZqYUie6svw7tdP.6gCvxlmqa7sEzNKGoa2VqZFEGPLciIx0.-iiO4yiUywBweO3AYG-e1MS79V; tt_scid=7JWpJPVxD8zIfVkcvM2Q6MaV8dmqAsTXyfew5nufFc7rWh1vS89HSOiF9mcoMoiTa772",
    'x-requested-with': 'XMLHttpRequest',
}
res = requests.get(url, headers=headers)
print(res.text)

