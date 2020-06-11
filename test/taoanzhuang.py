import requests

# for id in range(10000):
# url = 'http://47.104.181.33/IOS_port/selectApp_userByIDSingle.do?App_u_id={}&type=1'.format(id)
url = 'http://47.104.181.33/IOS_port/selectApp_userByIDSingle.do?App_u_id=1431&type=1'
# url = 'http://47.104.181.33/IOS_port/service/selectOrdersById.do?Order_id=15464&App_u_id=76247'
headers = {
    'ulr_type': '1',
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.4; HD1910 Build/KTU84P)',
    'Host': '47.104.181.33',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '0'
}

res = requests.post(url, headers=headers)
print(res.text)
