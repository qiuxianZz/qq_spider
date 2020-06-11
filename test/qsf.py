
import requests

url = 'http://www.qsf111.com/api/WebApi/getansfInfo'
headers = {
'Content-Length': '81',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'www.qsf111.com',
'Connection': 'Keep-Alive',
'User-Agent': 'android-async-http/1.4.4 (http://loopj.com/android-async-http)',
'Accept-Encoding': 'gzip'
}

data = 'types=1&city=%E5%85%A8%E5%9B%BD&userno=&page_index=3&source=Android&page_count=100'
res = requests.post(url,headers=headers,data=data)
print(res.text)