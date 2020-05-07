import json

import requests

url = 'https://www.yuedaoapp.com/app/demandNew/get_list'

headers = {
    "Host": "www.yuedaoapp.com",
    "accept-language": "zh-CN,zh;q=0.8",
    "user-agent": "Android/3.8.6/20200420/samsungSM-N960F/5.1.1/IMEI:null",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "content-length": "260",
    "accept-encoding": "gzip"
}
# data = 'akey=&bkey=36%2C16%2C0%2C10%2C23&ckey=a5f4fdg24ek85bc9qfc014bxbafd521d&os=1&page=9&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
# data = 'akey=1587740221&bkey=219%2C25%2C13%2C23%2C4&ckey=3561eb952f439n6aac1t897xbz8d4f78&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=9&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
#        'akey=1587740219&bkey=020,9,14,0,11&ckey=a2c210f55j7l50o2c87cu48756d602ea&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=8&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
#        'akey=1587740219&bkey=020,9,14,0,11&ckey=a2c210f55j7l50o2c87cu48756d602ea&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=8&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
#        'akey=1587740482&bkey=123,24,22,23,6&ckey=0bd471g01ecb229953faacwxy6726142&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=12&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
# data = 'akey=1587740219&bkey=020%2C9%2C14%2C0%2C11&ckey=a2c210f55j7l50o2c87cu48756d602ea&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=8&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)

# data = 'akey=1587740219&bkey=020%2C9%2C14%2C0%2C11&ckey=a2c210f55j7l50o2c87cu48756d602ea&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page={}&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
data = 'page=4&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=813e5d1h8cbl7ce6e9ef7bwfyzb35b8d&akey=1587741004&bkey=122%2C24%2C25%2C7%2C11&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'


def getData(page):
    res = requests.post(url, headers=headers, data=data)
    print(res.text)


# getData(1)

# page = 1
# while True:
#     print(page)
#     getData(page)
#     page += 1
url = 'https://www.yuedaoapp.com/app/SkillServerNew/getList'
headers = {
    "Host": "www.yuedaoapp.com",
    "user-agent": "Android/3.8.6/20200420/samsungSM-N960F/5.1.1/IMEI:null",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "content-length": "239",
    "accept-encoding": "gzip"
}


# data = 'page=4&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=2bcaed22729473oa664edv7cy3692601&akey=1587741596&bkey=421%2C2%2C14%2C24%2C1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


# url = 'https://www.yuedaoapp.com/app/SkillServer/skillDetail'
# data  = 'server_id={}&longitude=107.56763094985698&latitude=25.997886363608302&ckey=a307af01b1028ce073et57wxdz18da7a&akey=1587742243&bkey=125,22,23,0,19&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


def getUser(uid):
    res = requests.post(url, headers=headers, data=data.format(uid))
    con = json.loads(res.text)
    print(con)


#
# uid = 10000
# while True:
#     getUser(uid)
#     uid +=1


# url = 'https://www.yuedaoapp.com/app/demandNew/get_info'
url = 'https://www.yuedaoapp.com/app/SkillServer/skillDetail'

data = 'demand_id={}&longitude=107.56763094985698&latitude=25.997886363608302&ckey=28d79c2h5168cb8f18studc0yd30129a&akey=1587754896&bkey=319%2C7%2C24%2C18%2C20&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'

headers = {
    "Host": "www.yuedaoapp.com",
    "user-agent": "Android/3.8.6/20200420/samsungSM-N960F/5.1.1/IMEI:null",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "content-length": "247",
    "accept-encoding": "gzip"
}


def getcon(uid):
    res = requests.post(url, headers=headers, data=data.format(uid))
    print(res.text)


# getcon("25648")
# uid = 26564
# while True:
#     getcon(uid)
#     uid+=1


headers = {
    "user-agent": "Android/3.8.6/20200420/samsungSM-N960F/5.1.1/IMEI:null",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "content-length": "247",
    "accept-encoding": "gzip"
}


# url = 'https://www.yuedaoapp.com/app/demandNew/get_info'
# # 需求详情
#
# data = 'demand_id=11806&longitude=107.56763094985698&latitude=25.997886363608302&ckey=305dfdc0ia7bmf75qb486e5xy1059d2d&akey=1587806841&bkey=116%2C24%2C12%2C8%2C23&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,data=data,headers=headers,verify=False)
# print(res.text)
#
#
# url = 'https://www.yuedaoapp.com/app/SkillServer/skillDetail'
# # 服务详情
# data = 'server_id=125796&longitude=107.56763094985698&latitude=25.997886363608302&ckey=a58d348fi548mbcpff04baa8d0598b33&akey=1587807496&bkey=312%2C3%2C0%2C15%2C8&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data,verify=False)
# print(res.text)
#
# # 服务地址
# url = 'https://www.yuedaoapp.com/app/SkillServer/personal'
# data = 'member_id=1044729&longitude=107.56763094985698&latitude=25.997886363608302&ckey=a8e7eab5f083m7ob5e68afwf11bc1e6a&akey=1587807677&bkey=412%2C14%2C0%2C22%2C4&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data,verify=False)
# print(res.text)
#
#
# url = 'https://www.yuedaoapp.com/app/SkillServerNew/getList'
#
# data = 'page=6&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=9e863f2aiefldf4edad325w6eeea78a9&akey=1587807982&bkey=411%2C8%2C22%2C5%2C22&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,data=data,headers=headers,verify=False)
# print(res.text)
#
# url = 'https://www.yuedaoapp.com/app/demandNew/get_list'
#
# data = 'akey=1587808660&bkey=321%2C22%2C0%2C1%2C16&ckey=abbe22c276eea7fbq5a5evwd6a6650a6&latitude=25.997886363608302&limit=20&longitude=107.56763094985698&os=1&page=3&sort=1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&type=0&version=20200420'
#
# res = requests.post(url,headers=headers,data=data,verify=False)
# print(res.text)
#
#
#
# # url = 'https://www.yuedaoapp.com/app/SkillServer/skillDetail'
# url = 'https://www.yuedaoapp.com/app/demandNew/get_info'
#
# data = 'demand_id=24934&longitude=107.56763094985698&latitude=25.997886363608302&ckey=28d79c2h5168cb8f18studc0yd30129a&akey=1587754896&bkey=319%2C7%2C24%2C18%2C20&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data,verify=False)
# print(res.text)


def getDemandNew(uid):
    url = 'https://www.yuedaoapp.com/app/demandNew/get_info'
    data = 'demand_id={}&longitude=107.56763094985698&latitude=25.997886363608302&ckey=28d79c2h5168cb8f18studc0yd30129a&akey=1587754896&bkey=319%2C7%2C24%2C18%2C20&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
    res = requests.post(url, headers=headers, data=data.format(uid), verify=False)
    print(res.text)
    con = json.loads(res.text)
    data = con["data"]
    id = data["id"]
    sex = data["sex"]
    payment = data["payment"]
    contacts = data["contacts"]
    mobile = data["mobile"]
    address = data["address"]
    service_desc = data["service_desc"]
    status = data["status"]
    sensitive = data["sensitive"]
    username = data["username"]
    share_url = data["share_info"]["share_url"]


url = 'https://www.yuedaoapp.com/app/SkillServerNew/getList'
headers = {
    "Host": "www.yuedaoapp.com",
    "user-agent": "Android/3.8.6/20200420/samsungSM-N960F/5.1.1/IMEI:null",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "content-length": "239",
    "accept-encoding": "gzip"
}
# data = 'page=1&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=2bcaed22729473oa664edv7cy3692601&akey=1587741596&bkey=421%2C2%2C14%2C24%2C1&token=306e0cc4115ef85552d9503af4e950903f6a810409f50b14875f36de1e5b03a4&os=1&version=20200420'
# data = 'page=1&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=ab91ecad56k8ea422rf2acb597d76004&akey=1587897602&bkey=10%2C1%2C17%2C10%2C10&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
# data = 'page=1&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=a6ca2f1eb6k5c14p92f5ev1xd7f96e49&akey=1587897867&bkey=023%2C21%2C0%2C10%2C15&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
data = 'page=1&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=67ce1fdc979l9docbcd1u33eb90a813e&akey=1587898650&bkey=22%2C14%2C11%2C5%2C20&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
# # data = 'page=1&limit=20&condition=%7B%22server%22%3A0%2C%22sort%22%3A2%7D&ckey=d290e68hc5kl5461c8sdaab1cc758e42&akey=1587898799&bkey=47%2C18%2C4%2C10%2C11&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


#
# # getDemandNew(16565)
# uid = 10000
# while True:
#     getDemandNew(uid)
#     uid+=1

#
# url = 'https://www.yuedaoapp.com/app/SkillServer/skillDetail'
# data = 'server_id=1&longitude=111.5690259131373&latitude=28.99809280344978&ckey=2ded2c4e851f2e0aqrs26d3938b48947&akey=1587898089&bkey=318%2C3%2C16%2C17%2C17&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)

# url = 'https://www.yuedaoapp.com/app/SkillServer/personal'
# data = 'member_id=249519&longitude=111.5690259131373&latitude=28.99809280344978&ckey=a9df1fe29bf6mn443945874e0zfbd5fe&akey=1587898230&bkey=10%2C13%2C25%2C13%2C12&token=0776dc5b659b659087f1d00568f913d00b7c76489b071d91b3598cdb0d45ba54&os=1&version=20200420'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


url = 'https://www.yuedaoapp.com/app/demandNew/get_info'
# 需求详情

data = 'demand_id=24000&longitude=111.5690259131373&latitude=28.99809280344978&ckey=ea3e79b61cfaf73fqrs162w1428c94c6&akey=1587977598&bkey=122%2C22%2C18%2C17%2C16&token=6bfe4a03c5af06efa68f5f8ad1ae2ed6afd0e7374e769dd8fb318fcd79df1b44&os=1&version=20200420'
res = requests.post(url, data=data, headers=headers)
# print(res.text)


url = 'https://api.youbangxin.com/PersonalPage'

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.4; HD1910 Build/KTU84P)",
    "Host": "api.youbangxin.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Length": "314"

}
# data = "CoTo=5210ba110a21b3c3a86723078c5fb4e8&lon=121.492479&YBAppName=%E5%8F%8B%E5%B8%AE&Memberid=100&YBAppVersion=3.6.91&UserId=0fea70b341d9491a945dcf1b739eb005&YBAppbundleid=com.exmart.friendbang&YBDeviceId=866617144056045&YBSysVersion=19&YBSysName=android&Spm=646413669766496&YBSyssn=HD1910&language=1&lat=31.247221&"
# data = "YBSysVersion=19&lon=121.492479&YBAppName=%E5%8F%8B%E5%B8%AE&SkillId=1234&YBSysName=android&YBAppVersion=3.6.91&YBSyssn=HD1910&PartType=1&language=1&UserId=0fea70b341d9491a945dcf1b739eb005&YBAppbundleid=com.exmart.friendbang&lat=31.247221&YBDeviceId=866617144056045&"
data = 'YBSysVersion=125&lon=121.492479&YBAppName=%E5%8F%8B%E5%B8%AE&SkillId=125&YBSysName=android&YBAppVersion=3.6.91&YBSyssn=HD1910&PartType=2&language=1&UserId=0fea70b341d9491a945dcf1b739eb005&YBAppbundleid=com.exmart.friendbang&lat=31.247221&YBDeviceId=866617144056045&'
url = 'https://api.youbangxin.com/SkillDetail'
# data = 'YBSysVersion=19&lon=104.04339&YBAppName=%E5%8F%8B%E5%B8%AE&SkillId=10338&YBSysName=android&YBAppVersion=3.6.91&YBSyssn=HD1910&PartType=1&language=1&UserId=0fea70b341d9491a945dcf1b739eb005&YBAppbundleid=com.exmart.friendbang&lat=30.641982&YBDeviceId=866617144056045&'
# res = requests.post(url,headers=headers,data=data)
# print(res.text)


url = 'https://api.daoway.cn/daoway/rest/technician/9323/by_buyer?lng=121.49701108831299&lat=31.247219444934505&userId=05a81899293f44349f76813f0073aeef&udid=866617144056045&appVersion=5.9.6'
# url = 'https://api.daoway.cn/daoway/rest/technicians/nearby/list?userLng=121.49701108831299&userLat=31.247219444934505&lng=121.49701108831299&lat=31.247219444934505&start=150&size=50&sortBy=fast&city=%E4%B8%8A%E6%B5%B7&userId=05a81899293f44349f76813f0073aeef&udid=866617144056045&appVersion=5.9.6'
headers = {
    "Charset": "utf-8",
    "appVersion": "5.9.6",
    "User-Agent": "DWBA/5.9.6(Linux; U; Android 4.4.4; HD1910 Build/KTU84P)",
    "Cookie": "manualCity=5LiK5rW3; token=5444ae578b838ab108bf74175a29727c; city=5LiK5rW3; Path=/daoway; Expires=Tue, 28-Apr-2020 04:31:15 GMT",
    "Host": "api.daoway.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

# res =requests.get(url,headers=headers)
# print(res.text)
#

url = "http://tyungaoku.weichuangbang.cn/xdnphb/yungao/article/published/zhaohang"
url = "http://tyungaoku.weichuangbang.cn/xdnphb/yungao/article/getAccount/zhaohang"

data = {
        "datas":[{"publishTime":"2019-10-26 09:55:53","author":"539d2e74af473f9682e1fc29e2c7d6c9","authorName":"北京吃货小分队","link":"https://res.cc.cmbimg.com/fsp/File/AtpResource/539d2e74af473f9682e1fc29e2c7d6c9/d2bcb63412d047ee85dc4eb42570a0d6.html","title":"所有女生！是时候去这家店了"},{"publishTime":"2019-10-27 16:27:09","author":"539d2e74af473f9682e1fc29e2c7d6c9","authorName":"北京吃货小分队","link":"https://res.cc.cmbimg.com/fsp/File/AtpResource/539d2e74af473f9682e1fc29e2c7d6c9/f2c02b798b14480da8494b0237cfee4e.html","title":"抖音年度爆款美食,这些北京能吃到!"},{"publishTime":"2019-08-22 19:54:37","author":"539d2e74af473f9682e1fc29e2c7d6c9","authorName":"北京吃货小分队","link":"https://res.cc.cmbimg.com/fsp/File/AtpResource/539d2e74af473f9682e1fc29e2c7d6c9/e2aefb5d1ae748f38e97f7d326781803.html","title":"居酒屋专题③｜干杯，朋友"}]


}

headers = {
    "Content-Type": "application/json",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
res = requests.post(url,headers=headers)
print(res.text)
