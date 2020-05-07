import requests

url = 'http://app.zx5880.com/app/chuzu.aspx'
headers = {
    "Accept-Encoding": "gzip",
    "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36",
    "Charset": "UTF-8",
    "Connection": "Keep-Alive",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "app.zx5880.com",
    "Content-Length": "26"
}

# data = 'id=561&action=getChuzuInfo'
#
# res = requests.post(url,headers=headers,data=data)
# print(res.text)

url = "http://app.zx5880.com/app/jiyouquan.aspx"

data = 'fid=&uid=3299&action=getUinfo'

# res = requests.post(url, headers=headers, data=data)
# print(res.text)

url = 'https://solarapi.cehome.com//app/superman/bbsapi?otherId=11201698&rtype=one&surl=%2Fother%2Fcenter'
headers = {
    "uid": "",
    "mobilemodel": "TAS-AN00",
    "latitude": "31.247221",
    "client": "android",
    "appSource": "bbs",
    "udid": "ODYxMTQzMjQ3Nzg0MTY0MDQyNWVlYmUzMzI2YjljMmRjOjY4OmQ0Ojc4Ojk1OjY1",
    "version": "3920",
    "token": "2ODzi6XUD7ar1D/d8b0aJBm93RVmz6bDl6guaaHcGAQa28da5u0ATyPL61/yWCey",
    "visitorid": "e19c91e7-7126-474c-8a84-a9a2d4a1e1af",
    "mobilebrand": "HUAWEI",
    "longitude": "121.492479",
    "Accept-Encoding": "identity",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; TAS-AN00 Build/LMY48Z)",
    "Host": "solarapi.cehome.com",
    "Connection": "Keep-Alive"
}
#
# res = requests.get(url, headers=headers)
# print(res.text)

url = 'https://solarapi.cehome.com/app/superman/bbsapi'
headers = {
    "Host": "solarapi.cehome.com",
    "Connection": "keep-alive",
    "Content-Length": "66",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "appsource": "cehome",
    "client": "mp",
    "content-type": "application/x-www-form-urlencoded",
    "latitude": "30.64242",
    "longitude": "104.04311",
    "token": "6KVHfBqudr3RwpiLea33kTmgIn95s3cX3BAzoutE6EQEbsWnmPSLLF+QbvINTDBI",
    "udid": "1588734858227-661132-025478daabf178-26621334",
    "uid": "",
    "version": "122",
    "visitorid": "2eca74f7-0d5a-41a2-bbe0-a63471636c8d",
    "Referer": "https://servicewechat.com/wx927d1a78c8c74c36/7/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}
data = 'surl=%2Fother%2Fcenter&rtype=cone&otherId=7uJ3o%2B7VUP%2FNOszITfZJ6g'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


url = 'https://appadmin.tiebijixie.com/api/machine/machine_detail'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; TAS-AN00 Build/LMY48Z) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "68",
    "Host": "appadmin.tiebijixie.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}
data = "member_id=1973&machine_id=358&token=256f729a27feaf2437e32f787186ffb4"
res = requests.post(url,headers=headers,data=data)
print(res.text)