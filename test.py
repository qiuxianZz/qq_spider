import requests

url = 'https://www.toutiao.com/i6803166284327420429/'
headers = {

    'Host': 'www.toutiao.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.toutiao.com/i6803166284327420429/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__ac_nonce=05eb665a700edadb7c627; __ac_signature=fl93mAAgEBAtDMMOoD9V.35edoAACDrxYq6XMGoJhPzOtSwouGhnMnciV7cLEZHduMofUHIveMU6o9b7Qkkah8vWaJbzvsV.FnmCLYSWE8ijqm2KArmotlsfWPwa3l8Kag9'
}



res = requests.get(url, headers=headers)
print(res.text)