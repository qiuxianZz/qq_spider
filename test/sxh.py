import json

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Host': 'appwechat.shixh.com',
    'Connection': 'keep-alive',
    'Content-Length': '24',
    'content-type': 'application/json',
    'sessionId': 'xcx.sxh.sid.14160600.26b790b9-cf0a-412c-ac79-263cf5f7b21e',
    'xcxType': '0',
    'Referer': 'https://servicewechat.com/wxafd63987bad96c1f/236/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'

}
data = {"soInfoId":"110715000"}
res =  requests.post("https://appwechat.shixh.com/soInfo/querySoInfoDetail", headers=headers,data=json.dumps(data))
print(res.text)
