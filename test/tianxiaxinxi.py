import requests

url = 'https://cn.bykszb.com/app/index.php?i=6&t=0&v=1.8.44&from=wxapp&c=entry&a=wxapp&do=ApiGetTelInfo&state=we7sid-25845ad231e8fddc553a0fb0aa95007e&sign=99722d8610b03aa305414e3c43f27f72&m=amouse_tel114&id=437124'

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'User-Agent': 'ttnet okhttp/3.10.0.2'

}

res = requests.get(url, headers=headers)
print(res.text)
