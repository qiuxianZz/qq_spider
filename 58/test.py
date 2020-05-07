import requests
import json


# url = 'https://housewechat.58.com/house/Api_get_zufang_detail?infoId=41650263182977&openId=7054088ECB889F4FF8C120341211A9C17CCDD3D0A8DA5DF23789B9A4F60FFA70&signature=a82f9631b82d130e05f0af86899d10de&city_id=102&isAuction=&source_type='
url = 'https://housewechat.58.com/house/Api_get_zufang_detail?infoId=41679992567437&openId=7054088ECB889F4FF8C120341211A9C17CCDD3D0A8DA5DF23789B9A4F60FFA70&signature=f4b670442819be1d28e78c37685bba05&city_id=102&isAuction=&source_type='
url = 'https://appgongyu.58.com/house/detail_v2/gongyu/41703712954502?v=1&platform=android&signature=f076b3ff809870021d0dbf130642ab22&version=8.6.5&commondata=%7B%22tracekey%22%3Anull%2C%22gongyu_type%22%3A%22apartment%22%2C%22isMonthly%22%3A0%7D&sidDict=%7B%22PGTID%22%3Anull%2C%22GTID%22%3Anull%2C%22a2%22%3A1%2C%22tid%22%3A%2228389294-3251-455c-a76a-9adca96bf5c3%22%2C%22pagesource%22%3A%22gy_10_zfindlzhengzu_no_no_no%22%2C%22abVersion%22%3A%22%22%2C%22slotid%22%3A1002195%2C%22productid%22%3A%2210043%22%2C%22info_houseID%22%3A%2241703712954502%22%7D&format=json&localname=sh'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "ppu": "UID=42772818388239&UN=kh7rxd&TT=346461537b72f79cb048aba73463e5e2&PBODY=WBGKfkI_9DtMs4-7F_xVbJ0yyYPquJZ2S332aolzqs1PnBUqK1j4u_9Ib7jJP8IWgTmcSR1EINLSEqtFhtdUcmarsHQqSSWKC_gqrhAbPgvek4XV5V2bM8_lHqtHKqkz1Xh7Ag9JLY6sApgk2Nofd5l3i7yTRf-rOUndw5OLHPU&VER=1"
}

res = requests.get(url,headers=headers)
print(res.text)


# url = 'https://rentercenter.58.com/call/api_get_privacy_phone?infoId=41650263182977&source=1&platform=wechat&pageSource=detail&phone=18215621840'
# res = requests.get(url,headers = headers)
# print(res.text)