import requests



url = 'http://api3.ksapisrv.com/rest/n/user/profile/v2?mod=Xiaomi%28MI%209%29&lon=112.569077&country_code=CN&kpn=KUAISHOU&oc=GENERIC&egid=&hotfix_ver=&sh=1600&appver=6.9.2.11245&max_memory=192&isp=CMCC&browseType=1&kpf=ANDROID_PHONE&did=ANDROID_1c1b0da3d0e18717&net=WIFI&app=0&ud=1695078392&c=GENERIC&sys=ANDROID_5.1.1&sw=900&ftt=&language=zh-cn&iuid=&lat=29.998528&did_gt=1579400527351&ver=6.9'



header = {
    "Accept-Language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "Referer": "https://live.kuaishou.com/",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 6 Build/NMF26X) NewsArticle/7.2.8 cronet/TTNetVersion:4df3ca9d 2019-11-25",

}

data = {
    "Date": "Sun, 19 Jan 2020 02:25:17 GMT",
    "Content-Type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "X-KsResult": "1",
    "X-KSLOGID": "579400717200592136",
    "Content-Length": "4071"

}

res = requests.post(url,headers=header,data=data)

print(res.text)