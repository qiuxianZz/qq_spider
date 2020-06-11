import time

import requests
import json

url = 'https://restapi.ele.me/swarm/shops/recommend?extras[]=identification&extras[]=coupon&scene=app:homepage&latitude=30.626431982964277&longitude=104.00696787983179&cityId=14&=ef3b1e84f7784201aef36839a86e0739&offset=40&limit=20&extraFilters=home&weatherCode=CLOUDY&orderBy=5&os=Android%2F5.1.1&network=WIFI&networkOperator=46000&deivce=SM-G925F'

headers = {
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.7.1500(0x27000730) Process/appbrand0 NetType/WIFI Language/zh_CN",

    # "User-Agent": "Rajax/1 SM-G925F/SM-G925F Android/5.1.1 Display/samsung-user_5.1.1_20171130.276299_release-keys Eleme/8.26.4 Channel/360 ID/ecefd2be-0893-3885-b4e5-944c89a2db21; KERNEL_VERSION:4.0.9 API_Level:22 Hardware:cec9a9a72ac0e2ccc32db86c6ddcecf9",
    # "X-DeviceInfo": "aW1laTo4Njc2NTMyMzQyODA0MzQgc2VyaWFsOjIzNDI0MTc0IGFuZHJvaWRfaWQ6MjA2MjA0MjIyODE0NTg5NCBicmFuZDpzYW1zdW5nIG1vZGVsOlNNLUc5MjVGIG5ldHdvcmtPcGVyYXRvcjo0NjAwMCBtYWNBZGRyZXNzOmRhXzUxXzJlXzAzXzYyX2EzIG5ldFR5cGU6V0lGSSBzaW1TZXJpYWxOdW1iZXI6ODk4NjAwNDcwMjQ0NzE3NTE1OTQgc2ltU3RhdGU6MCBsYXRpdHVkZTozMC42MjY0MzE5ODI5NjQyNzcgbG9uZ2l0dWRlOjEwNC4wMDY5Njc4Nzk4MzE3OSBjaWQ6NDM3MTI0ODQ4IGxhYzowIHdpZmlMaXN0OjAxXzgwX2MyXzAwXzAwXzAzIGhhdmVCbHVldG9vdGg6dHJ1ZSB0cmFja19pZDogbWVtb3J5Ojk2MyBlbmVyZ3lfcGVyY2VudDoxMDAgZmlyc3Rfb3BlbjoxNTg0OTQ5OTMwIGxhc3Rfb3BlbjoxNTg0OTQ5OTMwIG5ldF90eXBlOldJRkkgaGFyZHdhcmVfaWQ6Y2VjOWE5YTcyYWMwZTJjY2MzMmRiODZjNmRkY2VjZjk=",
    # "x-utdid": "Xl8DPJv7gbUDAGbdTyMxDmUW",
    # "x-umt": "znhL47JLOk7VCDVxBu5cMaC5YKgiFP6l",
    # "X-Shard": "loc=104.00696787983179,30.626431982964277",
    # "X-Eleme-RequestID": "FFA6953563C745708E8C73250AE0EEDD|1584950120620",
    # "X-Sopush-Appkey": "24895413",
    # "X-Sopush-Appversion": "8.26.4",
    # "ex_r": "156026350",
    # "ex_dc": "GyWCmjyn6F+FdxCYQ4PDE9nBL7dUx7foP2toHmkIGHMMHlitUql8keXBbxb5KC1busBxjFOTvxCWDUO4GUb9x4hxaFx6vuXeILmrVb8Aj5kqQqsw5E7fBb8rTjaT47bjEHumz+BXRSCTuSZigOaBMFjyUywvSAcbZr8I6ilxEJdqQOyY/nqPhHzT0xNH0lFHgWAi8t/R0Wt5CdVulZixNjO1OU6O1AHOFH0Js3VBIQ/pcBcSvEuavW1csNVKKmKLBtMKjF3xX5cOT3hA2dpBjdlFIzY43RW2SQFEyoGt3yQ=OjpAgX",
    # "ex_d": "aa1000100024981f7362031e8dea86d76539bc65e4216a422f",
    # "Host": "restapi.ele.me",
    # "Connection": "Keep-Alive",
    # "Accept-Encoding": "gzip",
    "Cookie": "USERID=2000005745685; UTUSER=2000005745685; x5check_ele=BBJoyxK7lBNkTk%2BkAdt25hXyTPCLCCzZH1xITt2H%2F2Y%3D; ZDS=1.0|1584949969|IZo9X9HOoH5MSHNfYwyz3tzhrol47f+B3A9rtd4d+H/aIQhCxXkoVzPx6T9wdB5r6iBDMmv+SJ3AqT5/BdSAzg==; track_id=1584949969|0c491d11f6c258c823299830e7f68d44752fad41d5ae326974|4f8ed106979fb91d0d9054ae65b1bd13; SID=k7WR49KWEsCUjDN84M3F5fNXkkAHEATFSkRg29; tzyy=e082d11cf2fb0c6cca4c8853a11972ea"
}

# url = 'https://h5.ele.me/pizza/shopping/restaurants/E15812718472240672901/batch_shop?user_id=2000005745685&code=0.100087204148261&extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D&terminal=h5&latitude=30.626432&longitude=104.006968'
# res = requests.get(url,headers=headers)
# print(res.text)

# url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.626432&longitude=104.006968&offset=24&limit=8&extras[]=activities&extras[]=tags&extra_filters=home&terminal=h5'
url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.655822&longitude=104.081534&offset=8&limit=8&extras[]=activities&extras[]=tags&extra_filters=home&terminal=h5'
# 104.081534
# 30.655822

headers = {
    "Host": "h5.ele.me",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "X-Shard": "loc=104.006968,30.626432",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "x-ua": "RenderWay/H5 AppName/wap",
    "x-uab": "122#A3EgNJ5KEEaAVEpZy4p0EJponDJE7SNEEP7ZpJRBuDPpJFQLpCGwpoZDpJEL7SwBEyGZpJLlu4Ep+FQLpoGUEELon4yE7SNEEP7ZpERBuDPE+BQPpC76EJponDJLKMQEI1IX0DnTtBOmKBTba9ASRzQ6CvFaYAR1jRw+cmt9urFVHrV2RD4/h3kPibnLEaTi8oL6+YnEYOndzWUNy5bIlSp4uljb1h9uC5HZJhRJyZsVqWfoEEpanSp1ulIEELXrGCpUJDbbRDao2SAbE5btngL1ul8pDLVr8CpUJ4bEyF3DqW3oEEpanSp1uOIEELXZ8op6JNEEyBfDqMfbHzpangtzuljEEWfYGFLUJmk+NftG7gcGEODn5NftM0J04+F1uiT4WQjAUWB3sqC2eHioBkBllcOQn21jiCHKRZDR51MH1QoJhcE8ZWqit1FXz3cjlZpRGSkkPcQszAvORfaIf7I3Cg5YADwtr2e5r9bkq1uXdKLuEm7oA+rflIKu6G/tBv5QXI2b0B9NELrYCuIsidpyOiFGk8h3KfoJFMudGvH3G3quyOXCv/mJaMsxnotU6KVFC95xyhToY43CQdn/Sk1ZezS+BqtMpuGayjgwj9g+Aks5QTHk7h1Ncatm+kWTAWOpyWp5+W3/6PAZB+VMLIqlhbJ7fHh8PrJgb09SAukrkzmIiEmAOELd3vHqIOgmsqnCRZZe2qBYAcjVvEDyV4W8dJ45HRtP3DcLmRvF",
    "Referer": "https://h5.ele.me/msite/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "ubt_ssid=haaawx28ke8sbiu3eo7t0g443tkm2jl4_2020-03-11; cna=9S+uEoBdokcCAdpYG4whEJSq; _utrace=e10c633374fd60d68cbc1ab6496a1826_2020-03-11; __wpkreporterwid_=64a7ddaf-dc0c-4334-9d4a-0a714f71bdf0; perf_ssid=ri6mhq9uviwjgemyg9zu891sqqfh8w9e_2020-03-23; ut_ubt_ssid=govyf9ufls9fcj7dfhp7ialugqeo22y2_2020-03-23; _bl_uid=s3kR28qC4s18zji5Fs2O75Lravsq; track_id=1584953877|8f279c676f0324f23f9aee20d6d330ee7d097fff4424d49ff7|618d24aaa03e5bda4a028294a96bacb4; USERID=2000005745685; UTUSER=2000005745685; ZDS=1.0|1584953877|IZo9X9HOoH5MSHNfYwyz3t96mTt6OYMIz0/hxAg+D74MFNi1jztuRIhNdEVSXXZdMSfpvNSt2tOTO2eiF92uwQ==; tzyy=e082d11cf2fb0c6cca4c8853a11972ea; _samesite_flag_=true; cookie2=16c0cef1d19b463ce334d4d16ff35056; t=8ebd6f4a799b1a4affb848cad1dc0b48; _tb_token_=b81bf7d535e3; csg=13bbacaf; t_eleuc4=id4=0%40BA%2FvuHCrrRtWTmAQg7OgQUChnnZfoPagkhrRGQ%3D%3D; munb=2206370031993; SID=ylzgHNWyLdS3JviYzVD3vtTBrzCtsXN4LUwQ29; x5check_ele=BBJoyxK7lBNkTk%2BkAdt25oY7QMyk2jjnMMD%2FUE8RV7Y%3D; l=dBQqnpNrQFOPJ5Y1BOfZqKo80E_9VQAffsPPu4LDFICPOvWRyz_VWZfj9ztvCnGV3sCMR3z5HU7TBXLo2PziQxv9-e9bMdFsHdTeo; isg=BLa21ae79IDGt4ANx3iP0gLMB-y41_oR2RJNsSCftBk0Y1D9iGeYInRSfxkPS_Ip"

}

# res = requests.get(url,headers=headers)
# print(res.text)
# data = json.loads(res.text)
# items = data["items"]
# for i in items:
#     print(i["restaurant"]["id"])

# E2926708086660275558
# E16974470788204516708
# E7515835038823025237
# E3075540104490146875
# E6936453613087239571
# E7914608692846847835
# E889081877134164159
# E14225119517680066393
url = 'https://h5.ele.me/pizza/shopping/restaurants/E14225119517680066393/batch_shop?user_id=2000005745685&code=0.100087204148261&extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D&terminal=h5&latitude=30.626432&longitude=104.006968'
url = 'https://h5.ele.me/pizza/shopping/restaurants/E1650974346708109725/batch_shop?user_id=2000005745685&code=0.100087204148261&extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D&terminal=h5&latitude=30.626432&longitude=104.006968'
# res = requests.get(url, headers=headers)
# print(res.raw._connection.sock.getpeername()[0])

# address = '成都市'
# url= 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
# response = requests.get(url)
# answer = response.json()
# lon = float(answer['result']['location']['lng'])
# lat = float(answer['result']['location']['lat'])
# print(lon)
# print(lat)
headers = {
    "Host": "h5.ele.me",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "X-Shard": "loc=104.006968,30.626432",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "x-ua": "RenderWay/H5 AppName/wap",
    "x-uab": "122#A3EgNJ5KEEaAVEpZy4p0EJponDJE7SNEEP7ZpJRBuDPpJFQLpCGwpoZDpJEL7SwBEyGZpJLlu4Ep+FQLpoGUEELon4yE7SNEEP7ZpERBuDPE+BQPpC76EJponDJLKMQEI1IX0DnTtBOmKBTba9ASRzQ6CvFaYAR1jRw+cmt9urFVHrV2RD4/h3kPibnLEaTi8oL6+YnEYOndzWUNy5bIlSp4uljb1h9uC5HZJhRJyZsVqWfoEEpanSp1ulIEELXrGCpUJDbbRDao2SAbE5btngL1ul8pDLVr8CpUJ4bEyF3DqW3oEEpanSp1uOIEELXZ8op6JNEEyBfDqMfbHzpangtzuljEEWfYGFLUJmk+NftG7gcGEODn5NftM0J04+F1uiT4WQjAUWB3sqC2eHioBkBllcOQn21jiCHKRZDR51MH1QoJhcE8ZWqit1FXz3cjlZpRGSkkPcQszAvORfaIf7I3Cg5YADwtr2e5r9bkq1uXdKLuEm7oA+rflIKu6G/tBv5QXI2b0B9NELrYCuIsidpyOiFGk8h3KfoJFMudGvH3G3quyOXCv/mJaMsxnotU6KVFC95xyhToY43CQdn/Sk1ZezS+BqtMpuGayjgwj9g+Aks5QTHk7h1Ncatm+kWTAWOpyWp5+W3/6PAZB+VMLIqlhbJ7fHh8PrJgb09SAukrkzmIiEmAOELd3vHqIOgmsqnCRZZe2qBYAcjVvEDyV4W8dJ45HRtP3DcLmRvF",
    "Referer": "https://h5.ele.me/msite/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cookie": "ubt_ssid=haaawx28ke8sbiu3eo7t0g443tkm2jl4_2020-03-11; cna=9S+uEoBdokcCAdpYG4whEJSq; _utrace=e10c633374fd60d68cbc1ab6496a1826_2020-03-11; __wpkreporterwid_=64a7ddaf-dc0c-4334-9d4a-0a714f71bdf0; perf_ssid=ri6mhq9uviwjgemyg9zu891sqqfh8w9e_2020-03-23; ut_ubt_ssid=govyf9ufls9fcj7dfhp7ialugqeo22y2_2020-03-23; _bl_uid=s3kR28qC4s18zji5Fs2O75Lravsq; track_id=1584953877|8f279c676f0324f23f9aee20d6d330ee7d097fff4424d49ff7|618d24aaa03e5bda4a028294a96bacb4; USERID=2000005745685; UTUSER=2000005745685; SID=vkts1x2NJLmvvHZphJObYUEmWQhDRZmygp8A29; ZDS=1.0|1584953877|IZo9X9HOoH5MSHNfYwyz3t96mTt6OYMIz0/hxAg+D74MFNi1jztuRIhNdEVSXXZdMSfpvNSt2tOTO2eiF92uwQ==; tzyy=e082d11cf2fb0c6cca4c8853a11972ea; x5check_ele=BBJoyxK7lBNkTk%2BkAdt25ptp23a30lIarfn5CKC5VtY%3D; l=dBQqnpNrQFOPJbI0BOfgZKoJyM79uIRfhsPPu4H-XICP9J5HJHkAWZ4gDoLMCnGVH6WyR3z5HU7TBLeWDyCSnxv9-CJMVImoUF1..; x5sec=7b227466653b32223a223537643932633433373563333430373932643230626139323739393633643039434b693537504d46454d375235376249687350376b51453d227d; isg=BBERR1JHK1uDSEdc9CEgUwFVIB2rfoXwuvtKwPOmDVjGmjHsO86VwL_0OGh8kh0o"
    "Cookie": "ubt_ssid=haaawx28ke8sbiu3eo7t0g443tkm2jl4_2020-03-11; cna=9S+uEoBdokcCAdpYG4whEJSq; _utrace=e10c633374fd60d68cbc1ab6496a1826_2020-03-11; __wpkreporterwid_=64a7ddaf-dc0c-4334-9d4a-0a714f71bdf0; perf_ssid=ri6mhq9uviwjgemyg9zu891sqqfh8w9e_2020-03-23; ut_ubt_ssid=govyf9ufls9fcj7dfhp7ialugqeo22y2_2020-03-23; _bl_uid=s3kR28qC4s18zji5Fs2O75Lravsq; track_id=1584953877|8f279c676f0324f23f9aee20d6d330ee7d097fff4424d49ff7|618d24aaa03e5bda4a028294a96bacb4; USERID=2000005745685; UTUSER=2000005745685; ZDS=1.0|1584953877|IZo9X9HOoH5MSHNfYwyz3t96mTt6OYMIz0/hxAg+D74MFNi1jztuRIhNdEVSXXZdMSfpvNSt2tOTO2eiF92uwQ==; tzyy=e082d11cf2fb0c6cca4c8853a11972ea; _samesite_flag_=true; cookie2=16c0cef1d19b463ce334d4d16ff35056; t=8ebd6f4a799b1a4affb848cad1dc0b48; _tb_token_=b81bf7d535e3; csg=13bbacaf; t_eleuc4=id4=0%40BA%2FvuHCrrRtWTmAQg7OgQUChnnZfoPagkhrRGQ%3D%3D; munb=2206370031993; SID=ylzgHNWyLdS3JviYzVD3vtTBrzCtsXN4LUwQ29; x5check_ele=BBJoyxK7lBNkTk%2BkAdt25oY7QMyk2jjnMMD%2FUE8RV7Y%3D; l=dBQqnpNrQFOPJ5Y1BOfZqKo80E_9VQAffsPPu4LDFICPOvWRyz_VWZfj9ztvCnGV3sCMR3z5HU7TBXLo2PziQxv9-e9bMdFsHdTeo; isg=BLa21ae79IDGt4ANx3iP0gLMB-y41_oR2RJNsSCftBk0Y1D9iGeYInRSfxkPS_Ip"

}


def get_id(offset):
    global num
    url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.655822&longitude=104.081534&offset={}&limit=8&extras[]=activities&extras[]=tags&extra_filters=home&terminal=h5'.format(
        offset)
    res = requests.get(url, headers=headers)
    print(res.text)
    data = json.loads(res.text)
    items = data["items"]
    for i in items:
        print(i["restaurant"]["id"])
        num += 1
        print(num)


offset = 8
num = 0
while True:
    get_id(offset)
    offset += 8
    time.sleep(2)

# url = 'http://api.map.baidu.com/geocoding/v3/?address=西安市&output=json&ak=你的ak&callback=showLocation'
# url = 'http://api.map.baidu.com/geocoder/v2/'
# params = { 'address' : '启东市',           # 以江苏省启东市为例
#            'ak' : 'c0hClkNXlUdAbLdRFM3tUTirQwDydZFB',             # 百度密钥
#            'output': 'json'}
#
# res = requests.get(url,params=params)
# data = json.loads(res.text)
# print(data)

# url= 'http://api.map.baidu.com/geocoder?output=json&key=c0hClkNXlUd34234234A2bLdRFM3tUTirQwDydZFB&address=成都市温江区金马镇东原城'

# url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=c0hClkNXlUdAbLdRFM3tUTirQwDydZFB&output=json&coordtype=wgs84ll&location=30.650647,103.814904'
# res = requests.get(url)
# print(res.text)
# data = json.loads(res.text)
# print(data)
# import requests
# proxies = {
#     'http':"http://113.100.89.215:46198"
# }
# p = requests.get('http://icanhazip.com',proxies=proxies)
# print(p.status_code)
# print(p.text)
