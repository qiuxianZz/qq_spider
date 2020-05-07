import json

import requests

url = 'http://zsf.dahouhou.com/queryneedstatus'
url = 'http://zsf.dahouhou.com/cancelorder'
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",

    # "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; TAS-AN00 Build/LMY48Z)",
    "Host": "zsf.dahouhou.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "130"


}
data = {"token":"E85FBB8AC4B745D39A385411094AA5E49D9D5FADE602E552D4B4372D2C36690E&needId=518139&device_token=8927fd3ef11677c4f48ae78ca23390e6"}
# data = {"token":"E85FBB8AC4B745D39A385411094AA5E468108303638F0FC23A548E6C1763AA2B&needId=518130"}



res = requests.post(url,headers=headers,data=json.dumps(data))
print(res.text)