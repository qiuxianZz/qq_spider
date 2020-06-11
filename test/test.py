import json

import requests



url = 'https://gybapi.kuaibang360.com/v3/weixin/huntingjob/ApplyCalling?t=1590655951778'
headers = {
'Host': 'gybapi.kuaibang360.com',
'Connection': 'keep-alive',
'Content-Length': '37',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
'channel': 'small_program',
'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
'session': 'WXSTATUS_ec3391aa5e40a6bd4cac24f744946f9f82d4134d',
'Referer': 'https://servicewechat.com/wx66afc9c605512b3b/24/page-frame.html',
'Accept-Encoding': 'gzip, deflate, br',

}
data = 'workerid=157887&targetid=76000&type=0'



res = requests.post(url,headers=headers,data=data)
print(res.text)